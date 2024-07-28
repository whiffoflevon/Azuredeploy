from citrus import Citrus
from oud import Oud
from floral import Floral
import csv
import ast

def main():
    # Generate fragrance based on user input
    
    for _ in range(1):
        fragrance = Citrus.get()
        Citrus.fragrance_list.append(fragrance) # appends the fragrance details to the list
        Citrus.write_to_csv("citrus.csv", Citrus.fragrance_list) # writes the fragrance details to a csv file
    print(fragrance) # prints the fragrance details

def __str__(self): # string representation of the class
        return f"House: {self.house}\n Name: {self.citrus}\n Top Notes: {self.top}\n Middle Notes: {self.mid}\n Base Notes: {self.base}\n Concentration: {self.concentration}\n Year: {self.year}\n Perfumer: {self.perfumer}"


def oud_main():
    for _ in range(1):
        fragrance = Oud.get()
        Oud.fragrance_list.append(fragrance)
        Oud.write_to_csv("oud.csv", Oud.fragrance_list)
    print(fragrance) 

def floral_main():
    for _ in range(1):
        fragrance = Floral.get()
        Floral.fragrance_list.append(fragrance)
        Floral.write_to_csv("floral.csv", Floral.fragrance_list)
    print(fragrance)

# Function to delete a fragrance from the csv file
def delete_fragrance():
    search = input("Enter the name of the fragrance you would like to delete: ").strip().lower()
    found = False
    try:
        with open("citrus.csv", "r") as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)
        with open("citrus.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";") 
            for row in rows:
                if any(search == value.strip().lower() for value in row):
                    found = True
                else:
                    writer.writerow(row)
        if found:
            print(f"The fragrance {search} was deleted successfully.")
        else:
            print(f"No matches found for {search}")
    except FileNotFoundError:
        print("The file 'citrus.csv' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to search a csv file for a fragrance
def find_fragrance(search_term):
    result = []
    search = search.strip().lower()
    found = False
    try:
        with open("citrus.csv", "r") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                if any(search in value.strip().lower() for value in row):
                    cleaned_row = []
                    for value in row:
                        try:
                            evaluated_value = ast.literal_eval(value)
                            if isinstance(evaluated_value, list):
                                cleaned_row.append(", ".join(map(str, evaluated_value)))
                            else:
                                cleaned_row.append(value)
                        except (ValueError, SyntaxError):
                            cleaned_row.append(value)
                    result.append(" | ".join(cleaned_row))
                    found = True
        if not found:
            result.append("No matches found.")
    except FileNotFoundError:
        result.append("File 'citrus.csv' was not found.")
    except Exception as e:
        result.append(f"An error occurred: {e}")
    return result









     
         

