def store(extracted):
    with open("data.txt","w") as file:
        file.write(extracted+ "\n")

