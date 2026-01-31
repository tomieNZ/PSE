from exporter import JSONExporter, CSVExporter, XMLExporter

class ExporterFactory:
    def get_exporter(self, exporter_type: str):
        if exporter_type == "json":
            return JSONExporter()
        elif exporter_type == "csv":
            return CSVExporter()
        elif exporter_type == "xml":
            return XMLExporter()
        else:
            raise ValueError("Invalid exporter type")