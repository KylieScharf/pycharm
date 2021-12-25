def name_check(name): #this function checks the number of each letter in one name so this is repeated for both names
    l = 0
    o = 0
    v = 0
    e = 0
    s = 0
    for letter in name:
        if letter in "Ll":
            l += 1
        if letter in "Oo":
            o += 1
        if letter in "Vv":
            v += 1
        if letter in "Ee":
            e += 1
        if letter in "Ss":
            s += 1
    love_list = [l, o, v, e, s]
    return love_list

def name_check2(name):
    #do for letter in the word dict[letter.upper and lower] = 0
    dict = {
        "lL": 0,
        "oO": 0,
        "vV":0,
        "eE":0,
        "sS":0
    }
    love_list = []
    for item in dict: #for every item in the dictionary we chek all the letters in the name against it and see if they match and if they do we add one to the letter's score
        for letter in name:
            if letter in " " + str(item):
                dict[item] += 1
        love_list.append(dict[item])
    return love_list


def name_check3(name, word): #this is what is used in the program
    dict = {}
    letter_list = []
    index_list = []
    for i in range(len(word)):
        if word[i] in dict.keys(): # checks to see if the letter is already in the dictionary
            letter_list.append(word[i])
            index_list.append(i)
        else:
            dict[word[i]] = 0
    #for letter in word: #for every letter in the word you put in you create a dictionary element with the value of 0
        #if dict[letter] == 0:
           #letter_list.append(letter)

        #print(letter)
        #if the letter doesn't exist set it to 1 and if it does increment
       # dict[letter] = 0 #the dictionart won't put more than 5 letters bc it can't have repeats
    love_list = []
    for item in dict: #for every item in the dictionary you compare it to every letter in the name
        for letter in name:
            if letter in "" + str(item):
                dict[item] += 1
        love_list.append(dict[item]) # you add the total for the letter into the empty list
    for i in range(len(letter_list)):
        love_list.insert(index_list[i], dict[letter_list[i]])
    return love_list

