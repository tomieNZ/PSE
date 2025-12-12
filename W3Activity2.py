class ReadFiles:
    """
    A class to read files and perform various operations on file content.
    """
    def __init__(self, file_path, mode="r"):
        """
        Initialize the ReadFiles object with file path and mode.
        
        Args:
            file_path (str): Path to the file to read
            mode (str): File mode, default is 'r' (read mode)
        """
        self.file_path = file_path
        self.mode = mode
        self.file = None
        self.content = None
    
    def read_and_output(self):
        """
        Read the file content and print it to the console.
        
        Returns:
            str: The content of the file
        """
        try:
            # Open and read the file
            with open(self.file_path, self.mode, encoding='utf-8') as self.file:
                self.content = self.file.read()
            
            # Print the file content with separators
            print("=" * 60)
            print(f"Content of file: {self.file_path}")
            print("=" * 60)
            print(self.content)
            print("=" * 60)
            
            return self.content
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found!")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
    
    def count_asterisks(self,character):
        """
        Count the number of '*' characters in the file.
        
        Returns:
            int: The number of '*' characters in the file
        """
        #using try and except to handle the errors
        try:
            # If content hasn't been read yet, read it first
            # the third parameter is the encoding of the file
            if self.content is None:
                with open(self.file_path, self.mode, encoding='utf-8') as self.file:
                    self.content = self.file.read()
            
            # Count the '*' characters
            # the count is a built-in function in Python to count the number of occurrences of a substring in a string
            asterisk_count = self.content.count(character)
            print(f"\nNumber of {character} characters in '{self.file_path}': {asterisk_count}")
            return asterisk_count
        #handle the error if the file is not found
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found!")
            return 0
        # handle the error if the file is not read
        except Exception as e:
            print(f"Error counting asterisks: {e}")
            return 0

    def append_char_to_file(self, char):
        """Appends a specific character to the end of the file."""
        try:
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(char)
            return f"Successfully appended '{char}' to {self.filename}"
        except Exception as e:
            return f"An error occurred while appending: {e}"


if __name__ == "__main__":
    # File path
    file_path = "demo_file.txt"
    
    # Create ReadFiles object
    read_files = ReadFiles(file_path, "r")
    
    # Read and output file content
    read_files.read_and_output()
    
    # Count the number of '*' characters
    read_files.count_asterisks('*')
    #add the information to the file
    #change the mode to append mode
    read_files.mode = "a"
    read_files.add_information("End of File")
    #test the add_information function
    #change the mode to read mode
    read_files.mode = "r"
    read_files.read_and_output()