# rows = int(input("How many rows?"))
# columns = int(input("how many columns?"))
# symbol = input("Enter a symbol to use: ")
#
# for a in range(rows):
#     for b in range(columns):
#         print(symbol, end="")
#     print()


# name = ""
#
# while len(name) == 0:
#     name = input("Enter your name: ")
#
# print("hello" + name)

# while True:
#     name = input("Enter your code: ")
#     if name != "":
#         break

# phone_number = "47637-3873728-93847"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)


# name = "denny"
#
# first_name = name[:2]
# last_name = name[3:]
# reverse_name = name[4:1:-1]
#
# print(first_name)
# print(last_name)
# print(reverse_name)


# website = "www.google.com"
#
# slice = slice(4,-4)
#
# print(website[slice])

# people = ["denny", "mike", "joke", "jordan"]
#
# people[0] = "mariah"
#
# people.append("michal")
# people.remove("joke")
# people.pop()
# people.insert(0, "whitney")
# people.sort()
# people.clear()
#
# for x in people:
#     print(x)

# singer = ["billie", "mariah", "whiney"]
# actor = ["jordan", "jason", "Koe"]
# stranger = ["Sun", "Rise", "Moon"]
#
# list = [singer, actor, stranger]
#
# print(list[1][2])

# student = ("Bro", 21, "male")
#
# print(student.count("Bro"))
# print(student.index("male"))
#
# for a in student:
#     print(a)
#
# if "Bro" in student:
#     print("Bob is here!")

# singer = {"billie", "mariah", "whiney"}
# actor = {"jordan", "jason", "Koe", "whiney"}
# stranger = {"Sun", "Rise", "Moon"}
#
# singer.add("tide")
# singer.remove("mariah")
# #singer.clear()
# #singer.update(actor)
# #ALL = singer.union(actor,stranger)
#
# print(singer.intersection(actor))

# capital = {'USA': 'Washington DC',
#            'India': 'New Dehli',
#            'China': 'Peking',
#            'Russia': 'Moscow'}

# capital.update({'German':'Berlin'})
# capital.update({'USA':'Las Vegas'})
# capital.pop('China')
# capital.clear()

# print(capital['Russia'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key.value in capital.items():
#     print(key, value)

# name = "denny que!"
#
# # if (name[0].islower()):
# #     print(name.capitalize())
#
# first_name = name[:3].lower()
# last_name = name[4:].upper()
# laste_name = name[-1]
#
# print(first_name)
# print(last_name)
# print(last_name)

# def hello(name):
#     print("hello! "+name)
#     print("have a nice day")
#
# my_name = "Denny"
#
# hello(my_name)

# def hello(first_name, second_name, age):
#      print("hello " + first_name + " " + second_name)
#      print("You are " + str(age) + " years old")
#      print("have a nice day")
#
# hello("Denny", "que", 21)

# def multiply(number1,number2):
#     result = number1 * number2
#     return result
#
# x = multiply(6,8)
#
# print(x)

# print (round(abs(float(input("Enter a whole positive number")))))

# name = "Bro" # global scope (available inside & outside functions)
#
# def display_name():
#     name = "code" # local scope (available only inside this function)
#     print(name)
#
# display_name()
# print(name)

# def add(*stuff): ("*" should be very important for this)
#
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5,6))

# def hello(**name):
#     #print ("hello" + name['first'] + " " + name['last'])
#     print("hello", end=" ")
#     for key,value in name.items():
#         print(value, end=" ")
#
# hello(first="denny", second="wu", last="bin")

# # str.format()
# animal = "Cow"
# item = "Moon"
#
# # print("The " + animal + " jumps over the " + item)
# # print("The {} jumps over the {}".format(animal,item))
# # print("The {1} jumped over the {0}".format(animal.item)) #positional argument
# # print("The {animal} jumped over the {cow}".format(animal="Cow", item="moon")) #keyword argument
#
# text= "The {} jumps over the {}"
# print(text.format(animal,item))

# name = "Bro"
#
# print("Hello, my name is {}".format(name))
# print("hello, my name is {:10}, nice to meet you" .format(name)) #{:10} means add 10 paddings here
# print("hello, my name is {:>10}, nice to meet you" .format(name))
# print("hello, my name is {:^10}, nice to meet you" .format(name)) # you can also add some keyword argument or index argument before the name;

# number = 1000
#
# print("The number is {:.2f}".format(number))
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number)) #binary
# print("The number is {:o}".format(number)) #octal
# print("The number is {:X}".format(number)) #hexadecimal
# print("The number is {:E}".format(number)) #scientific notation

# import random
#
# x = random.randint(1,6)
# y = random.random()
#
# mylist = ['Ivan','Denny','HY']
# Z = random.choice(mylist)
#
# cards = ["1","2","3","4","j","k","l"]
#
# random.shuffle(cards)
#
# print(cards)

# try:
#     numerator = int(input("Enter a number to devide:"))
#     denominator = int(input("Enter a number to divide by:"))
#     result = numerator / denominator
#     print(result)
# except ZeroDivisionError as e: # "e" is optional(the detailed problem);
#     print(e)
#     print("You can't devide by zero!Idiot!")
# except ValueError as e:
#     print(e)
#     print("accept only numbers")
# except Exception as e:
#     print(e)
#     print("Something went wrong:(")
# else:
#     print(result)
# finally:
#     print("this will always execute.")
#
# import os
#
# path = "/Users/filmfireworks_edit01/Desktop/test_input"
#
# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
#
# else:
#     print("That location does not exists!")

# try:
#     with open("/Users/filmfireworks_edit01/Desktop/test.tt") as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)

# text = "It does not working"
#
# with open('/Users/filmfireworks_edit01/Desktop/test.txt','w') as file:
#     file.write(text)

