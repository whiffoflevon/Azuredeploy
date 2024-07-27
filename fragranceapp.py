import tkinter as tk
from tkinter import messagebox
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

        self.search_button = tk.Button(root, text="Search Fragrance", command=self.search_fragrance)
        self.search_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Fragrance", command=self.delete_fragrance)
        self.delete_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)

        self.results_listbox = tk.Listbox(root, width=50, height=10)
        self.results_listbox.pack(pady=10)

    def add_fragrance(self):
        # Implement your logic for adding fragrance here
        pass
 
    def search_fragrance(self):
        search_term = self.simple_input_dialog("Search Fragrance", "Enter fragrance name:") 
        if search_term: # Check if search term is not empty
            results = find_fragrance(search_term)  # Call the find_fragrance function and place the results in the listbox
            self.results_listbox.delete(0, tk.END)
            for row in results:
                self.results_listbox.insert(tk.END, row) #

    def delete_fragrance(self):
        # Implement your logic for deleting fragrance here
        pass

    def simple_input_dialog(self, title, prompt):  
        def on_ok():
            nonlocal result
            result = entry.get()
            dialog.destroy()

        result = None
        dialog = tk.Toplevel(self.root)
        dialog.title(title)

        label = tk.Label(dialog, text=prompt)
        label.pack(pady=5)

        entry = tk.Entry(dialog)
        entry.pack(pady=5)
        
        ok_button = tk.Button(dialog, text="OK", command=on_ok)
        ok_button.pack(pady=5)
        
        self.root.wait_window(dialog)
        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = FragranceApp(root)
    root.mainloop()
