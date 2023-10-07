with open("./text.txt", "w+") as file:
    for line in file:
        print(line)
    file.write("New Kids on the Block\n")