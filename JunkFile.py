def find_fragrance(search):
    result = []
    search = search.strip().lower()
    found = False
    try:
        with open("citrus.csv", "r") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                if any(search in value.strip().lower() for value in row):  # Use 'in' for partial matches
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






    def find_fragrance():
    result=[]
    search = input("Enter the name of the fragrance you would like to search for: ").strip().lower()
    found = False
    try:
        with open("citrus.csv", "r")as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                if any(search == value.strip().lower() for value in row): #checks if the search term is in the row
                    cleaned_row =[] #list to store the cleaned row
                    for value in row:
                        try:
                            evaluated_value = ast.literal_eval(value) # evaluates the value
                            if isinstance(evaluated_value, list): # checks if the value is a list
                                cleaned_row.append(", ".join(evaluated_value)) # appends the value to the cleaned row
                            else:
                                cleaned_row.append(value) # appends the value to the cleaned row
                        except (ValueError, SyntaxError):
                            #if it is not a list, add the value as is
                            cleaned_row.append(value)
            result.append(cleaned_row)
            found = True
        if not found:
            messagebox.showinfo("No Matches", "No matches found.")
    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"The file '{"citrus.csv"}' was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return result




while True:
    print("Welcome to the fragrance store!")
    print()
    print("""
    Press (1) To Add a fragrance | Press (2) To Search for a fragrance 
    | Press (3) To Delete a fragrance | (4) Display List | (5) Exit""")
    print()
    try:
        ops=int(input("Select: "))
    except ValueError:
        print("Please enter a valid integer.")
    if ops ==5:
        break
    elif ops == 2:
        find_fragrance()
    elif ops == 3:
        delete_fragrance()
    elif ops == 1:
        sel = int(input("What type of fragrance would you like to add?: (1) Citrus | (2) Oud | (3) Floral: "))
        print()
        if sel == 1:
            main()
        elif sel == 2:
            oud_main()
        elif sel == 3:
            floral_main()



import tkinter as tk
from tkinter import messagebox
from citrus import Citrus
from main import find_fragrance
import csv

class FragranceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fragrance Store")

        self.label = tk.Label(root, text="Welcome to the Fragrance Store!")
        self.label.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Fragrance", command=self.add_fragrance)
        self.add_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Fragrance", command=self.search_fragrance) # 
        self.search_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Fragrance", command=self.delete_fragrance)
        self.delete_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)

        self.results_listbox = tk.Listbox(root, width=50, height=10)
        self.results_listbox.pack(pady=10)

    def add_fragrance(self):
        fragrance = Citrus.get()
        Citrus.fragrance_list.append(fragrance)
        Citrus.write_to_csv("citrus.csv", Citrus.fragrance_list)
        messagebox.showinfo("Fragrance Added", "Fragrance added successfully!")

    def search_fragrance(self):
        search_term = self.simple_input_dialog("Search Fragrance", "Enter fragrance name:")
        if search_term: 
            results = find_fragrance()
            self.results_listbox.delete(0, tk.END)
            if results:
                for row in results:
                    self.results_listbox.insert(tk.END, row)
            else:    
                messagebox.showinfo("No Matches", "No matches found.")

    def delete_fragrance(self):
        delete_term = self.simple_input_dialog("Delete Fragrance", "Enter fragrance name:")
        if delete_term:
            self.delete_from_csv("citrus.csv", delete_term)

    def simple_input_dialog(self, title, prompt):
        def on_ok(): # function to get the input from the entry widget
            nonlocal results #
            results = entry.get()
            dialog.destroy()

        results = None
        dialog = tk.Toplevel(self.root)
        dialog.title(title)

        label = tk.Label(dialog, text=prompt)
        label.pack(pady=5)

        entry = tk.Entry(dialog)
        entry.pack(pady=5)
        
        ok_button = tk.Button(dialog, text="OK", command=on_ok)
        ok_button.pack(pady=5)
        
        self.root.wait_window(dialog)
        return results

    def delete_from_csv(self, csv_file, delete_term):
        found = False
        try:
            with open("citrus.csv", "r") as file:
                reader = csv.reader(file, delimiter=";")
                rows = list(reader)
            with open("citrus.csv", "w", newline="") as file:
                writer = csv.writer(file, delimiter=";")
                for row in rows:
                    if any(delete_term.strip().lower() in value.strip().lower() for value in row):
                        found = True
                    else:
                        writer.writerow(row)
            if found:
                messagebox.showinfo("Deleted", f"The fragrance '{delete_term}' was deleted successfully.")
            else:
                messagebox.showinfo("No Matches", "No matches found.")
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"The file '{csv_file}' was not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FragranceApp(root)
    root.mainloop()
