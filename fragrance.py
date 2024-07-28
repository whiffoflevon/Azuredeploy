class Fragrance:
    def __init__(self,house,top,mid,base,concentration,year,perfumer): # constructor to initialize the attributes of the class
        self.house = house
        self.top = top 
        self.mid = mid
        self.base = base
        self.concentration = concentration
        self.year = year
        self.perfumer = perfumer
    @classmethod # class method to get the fragrance details without having to create an object
    def get(cls):
        house = input("Enter the name of the house/brand: ")
        name = input("Enter the name of the fragrance: ") 
        top = input("Enter the top notes of the fragrance(seperate by commas): ").split(",")
        mid = input("Enter the middle notes of the fragrance(seperate by commas): ").split(",")
        base = input("Enter the base notes of the fragrance(seperate by commas): ").split(",")
        concentration = input("Enter the concentration of the fragrance: ")
        year = int(input("Enter the release year of the fragrance: "))
        perfumer = input("Enter the name of the perfumer: ")
        return cls(house,name,top,mid,base,concentration,year,perfumer) # returns the object of the class
