"""
This file is used to convert the temperature from Fahrenheit to Celsius and vice versa.
@author: Yaohui Zhang (tomie)
Date: 2025-12-01
"""

class TemperatureConverter:
    """
    This class is used to convert the temperature from Fahrenheit to Celsius and vice versa.
    """
    def __init__(self, temperature:str):
        """
        This method is used to initialize the class.
        """
        self.original_temperature = temperature.upper()
        self.temperature = temperature.upper()
        #check the temperature
        if self._check_temperature():
            #Fahrenheit to Celsius
            #if return True, then convert the temperature to Celsius
            self.temperature = float(self.temperature[1:])
            self.converted_temperature = self.convert_to_celsius()
            self.original_temperature += f" degrees Fahrenheit is converted to {self.converted_temperature} degrees Celsius."
            
        else:
            #Celsius to Fahrenheit
            #if return False, then convert the temperature to Fahrenheit
            self.temperature = float(self.temperature[1:])
            self.converted_temperature = self.convert_to_fahrenheit()
            self.original_temperature += f" degrees Celsius is converted to {self.converted_temperature} degrees Fahrenheit."
    
    def _check_temperature(self):
        """
        This method is used to check the temperature.
        """
        #check if the temperature is a string
        if not isinstance(self.temperature, str) or len(self.temperature) < 2:
            raise ValueError("Invalid input. Please enter the temperature with the correct 'C' or F' prefix.")
        #check if the temperature starts with F
        if self.temperature[0] == 'F':
            #print the message
            print("🔔 Your input is in Fahrenheit! We will convert it to Celsius!")
            #return True
            return True
        elif self.temperature[0] == 'C':
            print("🔔 Your input is in Celsius! We will convert it to Fahrenheit!")
            #return False
            return False
        else:
            raise ValueError("Invalid input. Please enter the temperature with the correct 'C' or F' prefix.")


    def convert_to_fahrenheit(self):
        """
        This method is used to convert the temperature from Celsius to Fahrenheit.
        """
        #using the formula to convert the temperature from Celsius to Fahrenheit
        #round the result to 2 decimal places
        return round((self.temperature * 9/5) + 32, 2)

    def convert_to_celsius(self):
        """
        This method is used to convert the temperature from Fahrenheit to Celsius.
        """
        #using the formula to convert the temperature from Fahrenheit to Celsius
        #round the result to 2 decimal places
        return round((self.temperature - 32) * 5/9, 2)

if __name__ == "__main__":
    print("-" * 30)
    print("🌡️ Temperature Converter 🌡️")
    print("-" * 30)
    #get the temperature from the user
    # initialize the TemperatureConverter class
    temperature = TemperatureConverter(input("🔔 Enter the temperature: "))
    print("-" * 30)
    #print the result
    print(f"🤖{temperature.original_temperature}")
    print("-" * 30)