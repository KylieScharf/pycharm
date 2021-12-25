from love.adder import adder
from love.heart import heart
from name_check import name_check3

def love(): #this is the main function and gets inpiut from the user and then calls the name check function then passes the list to the adder function
    print("The comparison percentage calculator")
    user_name = input("Input a name here: ")
    word = input("Input a word to compare: ")
    partner_name = input("Input another name here: ")
    user_list = name_check3(user_name, word)
    partner_list = name_check3(partner_name, word)
    sum_list = []
    for index in range(len(word)): #this creates the sum list with the l's and v's added together
        sum = user_list[index] + partner_list[index]
        sum_list.append(sum)
    final_list = adder(sum_list)
    if final_list[0] == 0:
        percent = str(final_list[1])
        space = 1
    else:
        percent = str(final_list[0]) + str(final_list[1])
        space = 0
    heart(percent, space)
    print(user_name + " " + word + " " + partner_name + " " + percent + "%")

love()
