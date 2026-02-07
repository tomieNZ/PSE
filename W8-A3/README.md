# CV ATS Optimization Agent

> AI-powered CV analyzer that compares your resume against a Job Description and delivers actionable ATS optimization recommendations.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white)
![PDF](https://img.shields.io/badge/PDF-Parser-EC1C24?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## Architecture

The project applies three OOP design patterns built on top of LangChain's LCEL (LangChain Expression Language) chain:

| Pattern | Class | Role |
|---|---|---|
| **Facade** | `CVAgent` | Single entry point — orchestrates the full workflow |
| **Strategy** | `PromptBuilder` | Encapsulates prompt construction, easy to swap |
| **Chain of Responsibility** | LCEL pipe | `prompt \| model \| parser` processing pipeline |

```
PDF File ──► PDFReader ──► cv_text ─┐
                                     ├──► LCEL Chain ──► ATS Report
JD Text ────────────────────────────┘
```

## Project Structure

```
W8-A3/
├── main.py              # Main application (all OOP classes)
├── requirements.txt     # Python dependencies
├── .env                 # API key config (git-ignored)
├── .env.example         # API key template
├── Dockerfile           # Docker build config
├── .dockerignore        # Docker build exclusions
├── docs/
│   ├── Yaohui_AI.pdf    # Sample CV (PDF)
│   └── sample_jd.txt    # Sample Job Description
└── README.md
```

## Analysis Output

The agent produces a structured report covering:

1. **ATS Compatibility Score** (0–100)
2. **Keyword Gap Analysis** — missing keywords from the JD
3. **Section-by-Section Review** — per-section feedback
4. **Formatting Recommendations** — ATS-friendly layout tips
5. **Content Optimization** — concrete rewrite suggestions
6. **Priority Action Items** — top 5 changes ranked by impact

---

## Getting Started

### Prerequisites

- Python 3.10+
- An OpenAI-compatible API key

### 1. Install Dependencies

```bash
cd W8-A3
pip install -r requirements.txt
```

### 2. Configure API Key

Copy the example env file and fill in your credentials:

```bash
cp .env.example .env
```

Then edit `.env`:

```env
OPENAI_API_KEY=sk-your-api-key-here
```

### 3. Prepare Your Files

Place your files in the `docs/` directory:

| File | Description |
|---|---|
| `docs/your_cv.pdf` | Your CV in PDF format |
| `docs/sample_jd.txt` | The target Job Description (plain text) |

Update the file paths in `main.py` if your filenames differ:

```python
CV_PDF_PATH = "docs/your_cv.pdf"
JD_FILE_PATH = "docs/sample_jd.txt"
```

### 4. Run

```bash
python main.py
```

### Example Output

```
📄 Reading CV from PDF...
   ✅ Extracted 3842 characters

🔍 Analyzing CV against Job Description...
   ✅ Analysis complete

======================================================================
          ATS OPTIMIZATION REPORT
======================================================================
1. ATS Compatibility Score: 62/100
2. Keyword Gap Analysis: ...
   ...
======================================================================
```

---

## Docker Deployment

### Build

```bash
docker build -t cv-ats-agent .
```

### Run

Use `--env-file` to inject API keys and `-v` to mount your docs:

```bash
docker run --rm --env-file .env -v $(pwd)/docs:/app/docs cv-ats-agent
```

This way you can swap CV and JD files without rebuilding the image.

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| LLM Framework | LangChain (LCEL) |
| PDF Parsing | PyPDF via `langchain-community` |
| LLM Provider | OpenAI GPT-4o-mini |
| Config Management | python-dotenv |
| Containerization | Docker |

## License

This project is for educational purposes as part of the PSE coursework.
