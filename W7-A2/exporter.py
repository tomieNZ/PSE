from abc import ABC, abstractmethod
import json


class Exporter(ABC):
    """Abstract base class for exporters"""
    # Error message for when no data is provided
    err_for_no_data = "No data to export"

    # Abstract method to export data
    @abstractmethod
    def export(self, data: dict) -> str:
        pass

class JSONExporter(Exporter):
    """Exporter for JSON format"""
    def export(self, data: dict) -> str:
        if not data:
            return self.err_for_no_data
        return json.dumps(data,indent=2)

class CSVExporter(Exporter):
    """Exporter for CSV format"""
    def export(self, data: dict) -> str:
        if not data:
            return self.err_for_no_data
        headers = ",".join(data[0].keys())
        rows = [",".join(str(v) for v in row.values()) for row in data]
        return headers + "\n" + "\n".join(rows)

class XMLExporter(Exporter):
    """Exporter for XML format"""
    def export(self, data: dict) -> str:
        if not data:
            return self.err_for_no_data
        xml_string = "<data>"
        for row in data:
            xml_string += "<row>"
            for key, value in row.items():
                xml_string += f"<{key}>{value}</{key}>"
            xml_string += "</row>"
        xml_string += "</data>"
        return xml_string