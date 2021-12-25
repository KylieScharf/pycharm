import math
def adder(list): #this function iterates through the added list 1 less than the length of the list times and adds the item at index i with the next item together until the length of the list is less than 2
    while len(list) > 2:
        skip = 0 #this is a skip which is when there are more than one numbers greater than 10 then you need to skip over the new number added so skip inceases by 1
        for i in range(len(list) - 1): #this goes through the list and creates a new list with the sums
            added = list[i] + list[i + 1]
            list[i] = added
            if i == len(list) - 2:
                list.pop()
        for i in range(len(list)): #this goes through all the numbers in the new list to see if they are greater than 10
            if list[i + skip] > 9:
                ones = list[i + skip] % 10
                tens = math.floor((list[i + skip] - ones)/10) #floor gets rid of decimals
                list[i + skip] = tens
                list.insert(i + skip + 1, ones)
                skip += 1

    return list