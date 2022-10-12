from random import randint

def input_num (message):
    number = int(input(message))
    return number

def create_list_from_minusN_to_N (number):
    list = [i for i in range(-number, number + 1)]
    return list

def create_random_list (length):
    random_list = []
    list_of_elements =[]
    index = 0
    while index < int(length / 2):
        check = False
        while (not check):
            temp = randint(0, length - 1)
            if temp not in list_of_elements:
                random_list.append(temp)
                list_of_elements.append(temp)
                check = True
        index += 1
    return random_list