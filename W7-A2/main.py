from factory import ExporterFactory

def main():
    data_set = [
        {"name": "John", "age": 30, "email": "john@example.com"},
        {"name": "Jane", "age": 25, "email": "jane@example.com"},
        {"name": "Jim", "age": 35, "email": "jim@example.com"},
        {"name": "Jill", "age": 40, "email": "jill@example.com"},
        {"name": "Jack", "age": 45, "email": "jack@example.com"},
    ]

    # Prompt the user to enter the type of exporter they want to use (json, csv, or xml)
    choosen_type = input("Enter the exporter type (json/csv/xml): ")
    
    # Create an instance of ExporterFactory to get the corresponding exporter object
    exporter_factory = ExporterFactory()
    
    # Get the exporter based on user selection
    exporter = exporter_factory.get_exporter(choosen_type)
    
    # Use the exporter to export the data_set and get the result as a string
    result = exporter.export(data_set)
    
    # Print the exported result to the console
    print(result)


if __name__ == "__main__":
    main()