from fragrance import Fragrance # imports the Fragrance class from the fragrance module
import csv 

class Citrus(Fragrance): # Citrus inherits from Fragrance
    fragrance_list = [] # list to store the fragrance details
    def __init__(self, house,citrus,top,mid,base,concentration,year,perfumer): # constructor to initialize the attributes of the class
        self.citrus = citrus
        super().__init__(house,top,mid,base,concentration,year,perfumer) # calls the __init__ method of the Vehicle class
   
    @classmethod
    def write_to_csv(cls, csv_file, fragrance_list): # class method to write the fragrance details to a csv file 
        with open(csv_file, 'a', newline='') as file: # opens the csv file in append mode and creates a file
            writer = csv.writer(file, delimiter=';') # creates a csv writer object 
            for fragrance in fragrance_list: # iterates over the list of fragrances  
                writer.writerow([fragrance.house,fragrance.citrus, fragrance.top, fragrance.mid, fragrance.base, fragrance.concentration, fragrance.year, fragrance.perfumer])

    def __str__(self): # string representation of the class
        return f"House: {self.house}\n Name: {self.citrus}\n Top Notes: {self.top}\n Middle Notes: {self.mid}\n Base Notes: {self.base}\n Concentration: {self.concentration}\n Year: {self.year}\n Perfumer: {self.perfumer}"



