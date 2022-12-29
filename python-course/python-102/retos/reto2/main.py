import utils
import read_csv as csv
import charts

def run():
    data = csv.read_csv("./reto/data.csv")
    data = list(filter(lambda item: item["Continent"] == "South America", data))
    world_population, labels = utils.get_world_population(data)
    charts.generate_pie_chart(labels,world_population)

if __name__ == "__main__":
    run()