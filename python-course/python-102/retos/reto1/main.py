import utils
import read_csv as csv
import charts

def run():
    data = csv.read_csv("./reto/data.csv")
    country_code = input("Type Country Code - CCA3: ")
    country_code = country_code.upper()

    country_data = utils.population_by_country(data, country_code)
    
    if len(country_code) > 0:
        country = country_data[0]
        labels, values = utils.get_population(country)
        print(labels, values)
        charts.generate_bar_chart(labels, values)

if __name__ == "__main__":
    run()