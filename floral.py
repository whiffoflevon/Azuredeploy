from fragrance import Fragrance
import csv

class Floral(Fragrance):
    fragrance_list =[]
    def __init__(self,house,floral,top,mid,base,concentration,year,perfumer,):
        self.floral = floral 
        super().__init__(house,top,mid,base,concentration,year,perfumer)
    @classmethod
    def write_to_csv(cls,csv_file,fragrance_list):
        with open(csv_file,'a',newline='') as file:
            writer = csv.writer(file,delimiter=';')
            for fragrance in fragrance_list:
                writer.writerow([fragrance.house,fragrance.floral,fragrance.top,fragrance.mid,fragrance.base,fragrance.concentration,fragrance.year,fragrance.perfumer])
    def __str__(self): # string representation of the class
        return f"House: {self.house}\n Name: {self.floral}\n Top Notes: {self.top}\n Middle Notes: {self.mid}\n Base Notes: {self.base}\n Concentration: {self.concentration}\n Year: {self.year}\n Perfumer: {self.perfumer}"
    

        
        
        
 







