class Country:
    def __init__(self, country_name):
*        self.country_name = country_name

    def Country_detials(self):
        print(f"the name of the country is {self.country_name}")

class Happiest_country(Country):
    def __init__(self, country_name, continent):
        super().__init__(country_name)
        self.continent = continent

    def happydetials(self):
        print(f"Happiest country is {country_name} from{self.continent}")

def main():
    Nepal = Happiest_country('Nepal','Asia')
    Nepal = happydetials()

if __name__ == "__main__":
    main()


