class Crop:
    def __init__(self, name, acres, yield_per_acre, price_per_tonne, ):
       
        self.name = name
        self.acres = acres
        self.yield_per_acre = yield_per_acre
        self.price_per_tonne = price_per_tonne
        

    def total_yield(self):
        #Apart from tomatao, all crops have uniform yield"
        if not self.name == "Tomato":
            return self.acres * self.yield_per_acre
        
        total = 0
        for percent, yld in [
            (0.30, 10),
            (0.70, 12)
        ] :
            total += (percent * self.acres) * yld
        return total

    def revenue(self):
        return self.total_yield() * self.price_per_tonne



class Farm:

    def __init__(self):
        self.crops = {}

        #farm:
        # crops: dict of Crop objects
        # EXAMPLE: {"Tomato": Crop(...), 
        #           "Potato": Crop(...)}

    def add_crop(self, crop):
        self.crops[crop.name] = crop

    def total_revenue(self):
        return sum(self.crops[name].revenue() for name in self.crops.keys())

    def chemical_free_revenue(self, month):
        """Calculates reveneue in accordance with time taken for chemical free crops"""
        chemical_free_crops = []
        if month >= 6:
            chemical_free_crops += ["Tomato", "Potato", "Cabbage"]
        if month >= 10: #next 4
            chemical_free_crops += ["Sunflower"]
        if month >= 14:  #next 4 months
            chemical_free_crops += ["Sugarcane"]

        return sum(self.crops[name].revenue() for name in chemical_free_crops)


if __name__ == "__main__":
    farm = Farm()

    #each segment = 16 acres , reason : 80/5 = 6 because equal distribution
    acres = 16

    tomato = Crop(
        name="Tomato",
        acres=acres,
        yield_per_acre=None,
        price_per_tonne=7000
    )

    potato = Crop("Potato", acres, 10, 20000)
    cabbage = Crop("Cabbage", acres, 14, 24000)
    sunflower = Crop("Sunflower", acres, 0.7, 200000)
    sugarcane = Crop("Sugarcane", acres, 45, 4000)

    # Add crops to farm
    farm.add_crop(tomato)
    farm.add_crop(potato)
    farm.add_crop(cabbage)
    farm.add_crop(sunflower)
    farm.add_crop(sugarcane)

    # Outputs
    print("Total Revenue:", farm.total_revenue())
    print("Chemical-free revenue at 11 months:", farm.chemical_free_revenue(11))

