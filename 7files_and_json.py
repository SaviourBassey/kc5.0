# # # text document

# # # open(file location, mode) it used to open text document (any file with an extension .txt)

# # # "r" - read (defualt)
# # # 'w' - write (overwrite exiting text)
# # # "a" - append (adds to the exiting text)
# # # "x" - create (fail if exist)

# # # FIRSTLY, OPEN THE FILE


# # file = open("")

 


# # name = ["kodecamp", "kodecamp 1.0"]


# # with open("namesssss.txt", "x") as file:
# #     file.write(name)

# # with open("name.txt", "r") as file:
# #     print(file.read())

# # # READ FROM THE FILE
# # # .read() - reads the entire file
# # # .readline() - read the first line of the line
# # # .readlines() - readd all the line into a list


# # # \n - special string charater that signifies a newlion
# # # # .strp()
# # # init_reading = file.readlines()
# # # stripped_reading = []

# # # for line in init_reading:
# # #     stripped_reading.append(line.strip())

# # # print(stripped_reading)


# # # WRITING TO FILE
# # # .write() - writes a string to the file 
# # # writelines() - writes a list of string



# # # in a case where we need to store  a strucutred data, then we can use JSON (JavaScript Object Notation)

# # # it is standardized means of storeing and exchanging structue data



# file = open("name.txt")


# print(file.read())

# file.close()

with open("name.txt") as file:
    print(file.read())