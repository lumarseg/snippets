import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        data = []
        reader = csv.reader(csvfile, delimiter= ",")
        header = next(reader)
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for (key, value) in iterable}
            data.append(country_dict)
        return data


if __name__ == "__main__":
    data = read_csv("./reto/data.csv")
    country_code="COL"
    country_data=list(filter(lambda item: item["CCA3"] == country_code, data))
    print(country_data)

    