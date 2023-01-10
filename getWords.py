
my_file = open("wordlist.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")
print(data_into_list)
my_file.close()

