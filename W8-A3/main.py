"""
CV ATS OPTIMIZATION AGENT

Uses LangChain LCEL chain to analyze a CV (PDF) against a Job Description
and provide ATS optimization recommendations.

Design Patterns:
- FACADE (CVAgent): Single entry point orchestrating the full workflow
- STRATEGY (PromptBuilder): Swappable prompt construction logic
- CHAIN OF RESPONSIBILITY (LCEL): prompt | model | parser pipeline

Data Flow:
    PDF → PDFReader → cv_text ─┐
                                ├→ LCEL Chain → ATS Report
    JD text ───────────────────┘
"""
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


class PDFReader:
    """Extracts text content from a PDF file via PyPDFLoader."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> str:
        """Load all pages and return concatenated text."""
        loader = PyPDFLoader(self.file_path)
        pages = loader.load()
        return "\n".join(page.page_content for page in pages)


class PromptBuilder:
    """Builds the ChatPromptTemplate for ATS analysis (Strategy pattern)."""

    @staticmethod
    def build() -> ChatPromptTemplate:
        """Return a prompt template with {cv_content} and {jd_content} variables."""
        system_message = (
            "You are a professional ATS (Applicant Tracking System) optimization "
            "consultant with 15 years of experience in recruitment and HR technology.\n\n"
            "Your task is to analyze a candidate's CV against a specific Job Description "
            "and provide detailed, actionable recommendations to improve the CV's ATS score.\n\n"
            "Please structure your analysis as follows:\n"
            "1. **ATS Compatibility Score** (0-100): Rate the current CV's compatibility.\n"
            "2. **Keyword Gap Analysis**: Identify missing keywords from the JD.\n"
            "3. **Section-by-Section Review**: Analyze each CV section.\n"
            "4. **Formatting Recommendations**: Suggest ATS-friendly formatting changes.\n"
            "5. **Content Optimization**: Recommend specific content improvements.\n"
            "6. **Priority Action Items**: List top 5 changes ranked by impact.\n\n"
            "Be specific and give concrete examples of how to rewrite sections."
        )

        user_message = (
            "=== CANDIDATE'S CV ===\n"
            "{cv_content}\n\n"
            "=== TARGET JOB DESCRIPTION ===\n"
            "{jd_content}\n\n"
            "Please analyze this CV against the Job Description and provide "
            "detailed ATS optimization recommendations."
        )

        return ChatPromptTemplate.from_messages([
            ("system", system_message),
            ("user", user_message),
        ])


class ATSAnalyzer:
    """Builds and executes the LCEL chain: prompt | model | parser."""

    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.3):
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            base_url=os.getenv("BASE_URL"),
            api_key=os.getenv("API_KEY"),
        )
        # LCEL chain: prompt → model → string output
        self.chain = PromptBuilder.build() | self.llm | StrOutputParser()

    def analyze(self, cv_text: str, jd_text: str) -> str:
        """Run the chain with CV and JD content, return the analysis report."""
        return self.chain.invoke({
            "cv_content": cv_text,
            "jd_content": jd_text,
        })


class CVAgent:
    """Facade: orchestrates PDF reading and ATS analysis in one call."""

    def __init__(self, cv_path: str, model_name: str = "gpt-4o-mini"):
        self.reader = PDFReader(cv_path)
        self.analyzer = ATSAnalyzer(model_name=model_name)

    def run(self, jd_text: str) -> str:
        """Read CV PDF → analyze against JD → return ATS optimization report."""
        print("📄 Reading CV from PDF...")
        cv_text = self.reader.read()
        print(f"   ✅ Extracted {len(cv_text)} characters\n")

        print("🔍 Analyzing CV against Job Description...")
        report = self.analyzer.analyze(cv_text, jd_text)
        print("   ✅ Analysis complete\n")

        return report


# ============================================================================
# MAIN
# ============================================================================
if __name__ == "__main__":
    CV_PDF_PATH = "docs/Yaohui_AI.pdf"
    JD_FILE_PATH = "docs/sample_jd.txt"

    if not os.path.exists(CV_PDF_PATH):
        print(f"❌ CV file not found: {CV_PDF_PATH}")
        exit(1)

    if not os.path.exists(JD_FILE_PATH):
        print(f"❌ JD file not found: {JD_FILE_PATH}")
        exit(1)

    with open(JD_FILE_PATH, "r", encoding="utf-8") as f:
        jd_text = f.read()

    agent = CVAgent(model_name="gpt-4o-mini", cv_path=CV_PDF_PATH)
    report = agent.run(jd_text)

    print("=" * 70)
    print("          ATS OPTIMIZATION REPORT")
    print("=" * 70)
    print(report)
    print("=" * 70)
