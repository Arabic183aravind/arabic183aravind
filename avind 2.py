#!/usr/bin/env python
# coding: utf-8

# In[1]:


# function of the list
lst1 = [5,2]
print(min(lst1)) # min item/element of the list
print(max(lst1)) # max element of the list
print(sum(lst1)) # sum of all the elements of the list
print(sum(lst1)//len(lst1)) # average of list elements
print(sum(lst1[1::2])/len(lst1[1::2])) # average of all the elements


# In[2]:


# methods of list object
lst1
lst1.append(24) # adding a new element at the end of the given list
lst1
lst1.insert(2,56) # adding an element at a particular index
lst1
lst1.count(18) # return the value how many times the object is repeated
lst1.index(56)
lst1.sort() # it's sorts the list in ascending order
lst1
lst1.pop() # remove the last element from the list
lst1
lst1.pop(1) # remove an element from a particular index
lst2 = [123,23,45]
lst1.extend(lst2) # merge lst2 into lst1
lst1


# In[3]:


li = [1,9,8,2,6,3]
print(li[-1::-2])


# In[4]:


# function to find second large item from the list
# input - [1,19,6,2,8,18,3]
# output - 18
def secondlarge(li):
    li.sort()
    return li[-2]
def genericlarge(li,n):
    li.sort()
    return li[-n]
li = [1,19,6,2,8,18,3]
genericlarge(li,4)


# In[5]:


# function
# input : list
# output : formatted output
# test cases :
# [1,6,9,4,16,19,22] -- 1 9 19 22
def linearsearch6(li):
    # implement the logic
    for x in range(len(li)):
        if x == 0 or x == len(li) - 1:
            
    return
li = [1,6,9,1,16,19,22]
linearsearch6(li) # 1 9 19 22



# 

#  # number to list
# - input as a number
# - expected output will be a list

# In[ ]:


# function for conversation - number to list
# input -- number
# output -- list
# test cases:-
# 14569 -- [1,4,5,6,9]
# 1990 -- [1,9,9,0]
def numberlistconversation(n):
    li = []
    while n != 0:
        r = n % 10
        li.append(r)
        n = n // 10
    li.reverse()
    return li
numberlistconversation(14569)#[1,4,5,6,9]


# In[ ]:


# function to count the OCCURANCES of a character in a string
# "python programming", p -> 2
# "python programming", m -> 2
def countofcharoccurance(s,c):
    cnt = 0
    for ch in s:
        if ch == c:
            cnt += 1
    return cnt
def countofcharoccurance(s,c):
    return s.count(c)
countofcharoccurance("python programming",'m')


# In[ ]:


# function to count the OCCURANCES of a character in a string
# "python programming", p -> 2
# "python programming", m -> 2
def countofcharoccurance(s,c):
    cnt = 0
    for ch in s:
        if ch == c:
            cnt += 1
    return cnt
countofcharoccurance("python programming",'b')


# # STRING TO LIST CONVERTION
# 
# - input will be a string
# 
# - expected output will be a list

# In[ ]:


# function to convert the string
# test case
# "1 2 3 4 5 6" -- [1,2,3,4,5,6]
def stringtolistconversion(s):
    li = s.split()
    numberslist = []
    for i in li:
        numberslist.append(int(i))
    return numberslist
s = "1 2 3 4 5 6"
stringtolistconversion(s) # [1,2,3,4,5,6]


# # SORTING ALGORITHMS
# * ALL SORTING ALGORITHMS MAKES THE LIST INTO ASCENDING ORDER
# * BUBBLE SORT
# * SELECTION SORT
# * INSERTION SORT
# 

# In[ ]:


# FUNCTION TO REPRESENT THE BUBBLE SORT
def bubblesort(li):
    for i in range(len(li)-1):
            for j in range(len(li)-1):
                if li[j] > li[j+1]:
                    li[j],li[j+1] = li[j+1],li[j]
    return li
li = [19,1,25,6,18,3]
bubblesort(li)


# # Dictionaries
# - it works on the concept of set unique data
# - keys,values is the unique identifier for a value
# - each key is separated from the values with colon(:)
# - each key and value is separated bya comma(,)
# - dictionaries are enclosed in curly brackets({})

# In[ ]:


MEHER = {"name":"gitam","email":"gitam@gmail.com","address":"hyderabad"}
print (MEHER)


# In[ ]:


MEHER["name"] # access the specific key value


# In[ ]:


MEHER.keys() # returns the list of keys


# In[ ]:


MEHER.values() # returns the values


# In[ ]:


MEHER.items() 


# # Tuples
# - t1 parenthesis() li square brakets []
# - difference between list and tuples
#      - list are muatble -  can be changed/modified
#             - used to access modify,add,delete data
#       - tuples are immutable - canot be changed
#             - used to access data only

# In[ ]:


t1 = (1,2,3,4,5)
t1
type(t1)


# # CONTACT APPLICATION
# * Add contact
# * Search the contacts
# * list all contacts
#    - name1 : phone1
#    - name2 : phone2
# * Modify the contact
# * Remove the contact
# * Import the contact
# 

# In[6]:


# add contact
contacts = {} # creating a dict object
def addcontacts(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("contact details are added")
    else:
        print("contact details are already exists")
    return
addcontacts('meher','9110788336')
addcontacts('aravind','9876543210')
addcontacts('kohli','9210788336')


# In[7]:


# search for contact details
def searchcontact(name):
    if name in contacts:
        print(name," : " , contacts[name])
    else:
        print("%s does not exists" % name)
    return
searchcontact('aravind')
searchcontact('meher')
searchcontact('kohli')


# In[1]:


# delete a contact 
def deletecontact(name):
    if name in contacts:
        del contacts[name]
        print(name,"deleted successfully")
    else:
        print(name,"not exists")
    return
deletecontact('ajay')


# ### packages and modules
# 
# * packages: * *
#        - a collection of modules(single python file .py) and subpackages
# * module: * *
#        - a single python file containing set functions
# * packages -->subpackers-->modules-->functions-->statements

# In[1]:


# import the externals packages to python file
import math
math.floor(123.45)


# In[3]:


from math import factorial as fact
fact(5)


# In[4]:


from math import gcd as gcd
gcd(10,15)


# In[7]:


# function to generate N randon numbers in given range
import random
def randomNnumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub) ,end=" ")
    return
randomNnumbers(10,0,100)


# In[21]:


# CREATE A SAMPLE GAME
# GENERATE 20 RANDOM NUMBERS 0 TO 500 
# INPUT : NUMBER
# OUTPUT : CONGRATS ! ! ! ! ! !
# - - - - - TRY ONCE AGAIN ! ! ! ! ! ! ! ! ! ! ! ! !

def generatenumbers(n,lb,ub):
    li = []
    for i in range(0,n):
        li.append(random.randint(lb,ub))
    return li
def check(n):
    if n in li :
        return "congrats  ! ! ! ! !"
    else:
        return "try once again ! ! ! ! ! ! ! !! ! ! ! ! ! ! ! ! ! ! ! "
    return

check(15)
    
    


# In[ ]:





# In[ ]:





# In[ ]:




