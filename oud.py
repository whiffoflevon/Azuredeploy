from fragrance import Fragrance
import csv


class Oud(Fragrance): # inherits from the Fragrance and Citrus classes
    fragrance_list = [] # list to store the fragrance details
    def __init__(self,house,oud,top, mid, base,concentration,year,perfumer): # constructor to initialize the attributes of the class
        self.oud = oud   # assigns the name of the fragrance
        super().__init__(house,top,mid,base,concentration,year,perfumer) # calls the __init__ method of the Fragrance class
    @classmethod
    def write_to_csv(cls, csv_file, fragrance_list): # class method to write the fragrance details to a csv file 
        with open(csv_file, 'a', newline='') as file: # opens the csv file in append mode and creates a file
            writer = csv.writer(file, delimiter=';') # creates a csv writer object
            for fragrance in fragrance_list:
                writer.writerow([fragrance.house,fragrance.oud, fragrance.top, fragrance.mid, fragrance.base, fragrance.concentration, fragrance.year, fragrance.perfumer])
          
    def __str__(self): # string representation of the class
        return f"House: {self.house}\n Name: {self.oud}\n Top Notes: {self.top}\n Middle Notes: {self.mid}\n Base Notes: {self.base}\n Concentration: {self.concentration}\n Year: {self.year}\n Perfumer: {self.perfumer}"
            

# The purpose of this functionality is to generate a fragrance object based on user input and write the fragrance details to a csv file.
 
        
