    # def weather_cond(temp):
    #     if temp > 7:
    #         return "Warm"
    #     else:
    #         return "Cold"

    # user_input = float(input("text"))

    # print(type(user_input))


# def get_name(name):
# name = input("Name: ")
# surname = input("Surname: ")
# print("Hi {} {}".format(name, surname))

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

# for key, values in phone_numbers:
#     print("{}".fabric(value))


# def SentenceMaker(phrase):
#     capitalized = phrase.capitalize()
#     interrogatives = ("how", "what", "why", "where", "how")
#     if phrase.startswith(interrogatives):
#         return "{}?".format(capitalized)
#     else:
#         return "{}.".format(capitalized)

# results = []
# while True:
#     user_input = input("Say something: ")
#     if user_input == "\end":
#         break
#     else:
#         results.append(SentenceMaker(user_input))

# print(results)

# results = []
# def sentence_maker(phrase):
#     interrogatives = ("who", "what", "where", "how")
#     capitalized = phrase.capitalize()
#     if phrase.startswith(interrogatives):
#         return "{}?".format(capitalized)
#     else:
#         return "{}.".format(capitalized)
    
# print(sentence_maker("how are you"))

# while True:
#     user_input = input("Say something: ")
#     if user_input == "\end":
#         break
#     else:
#         results.append(sentence_maker(user_input))

# print(" ".join(results))


temps = [230, 222, 231, 320, 9999, "no data"]

# new_temps= []
# for temp in temps:
#     new_temps.append(temp / 10)

# new_temps = [temp / 10 for temp in temps if temp != -9999]

# print(type(new_temps))
# print(new_temps)

# def start_list(index):
#     for i in index:
#         if isinstance(i, int):
#             print(i)
            
#         # else:
#         #     return(i)

#         # print(i)
#         # x = isinstance.(i, int)
#         # if x:
#         # print(x)
            
# start_list([temps])

# def foo(lst):
#     return [i for i in lst if isinstance(i, int)]

def foo(lst):
    return [i for i in lst if  isinstance(i, int)]

foo(["ana", 123, 32, 45])

# def foo(lst):
#     return [i for i in lst if i > 0]

# foo([-5, 6, 100])
