with open(file="banana.txt", mode="r", encoding="utf-8") as file:
    print(file.read())
    file.seek(0)  # move the file pointer back to the beginning of the file
    print(file.read())

with open("banana.txt", "r") as file:
    # print(file.readline())
    # print(file.readlines())
    for line in file:
        print(line.strip(), end=", ")

# with open("output.txt", "w") as file:
#     content = "This is a new content"
#     file.write(content)

# a- append mode, if the file already exists, the new content will be added to the end of the file
with open("output.txt", "a") as file:
    content = "\nThis is a new line"
    file.write(content)
