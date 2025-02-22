# (namesofboys) = list name
namesofboys = ['Mike','Elvis','Lewis','Aiden','Prince','Ryan','Charles']
print(namesofboys) #returns the list

#Accessing list

# To access elemnets use the index, starts from 0
# Mike = 0, Elvis = 1, Lewis = 2, Aiden = 3.................
# you can use negative indexes
# Counting from the right side to the left, Charles = -1, Ryan = -2


print(namesofboys[3]) # returns 'Aiden'
print(namesofboys[1]) #returns 'Elvis'

#for negative indexes
print(namesofboys[-1]) #returns Charles
print(namesofboys[-2]) #returns Ryan


#list slicing [start(inclusive):end(exclusive)]
print(namesofboys[0:4]) #returns ['Mike','Elvis','Lewis','Aiden']
print(namesofboys[:5]) # starts from index 0 and ends at index 4
print(namesofboys[1:]) #starts from index 1 to the ending of the list
print(namesofboys[:]) #returns everything in the list


# MANIPULATING LIST
namesofboys[2] = 'Philip' # changes the list elements
print(namesofboys[2]) # returns index 2 as Philip instead of Lewis

namesofboys + ['Sam'] # adds new element to list
print(namesofboys + ['Sam']) #returns list + new element

del(namesofboys[5]) # removes element from list

len(namesofboys) # finds length of list
print(len(namesofboys)) # returns length of the list



namesofboys2 = list(namesofboys) # creating a new list
namesofboys2 = namesofboys[:] #creating a new list
print(namesofboys2)

