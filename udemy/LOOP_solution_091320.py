#!/usr/bin/env python
# coding: utf-8

# In[17]:


### Task 1 to convert from for loop to while loop with desired outcome
numbers = list(range(0, 110, 10))
x = 0
newlist = []
while x < len(numbers):
    t = int(numbers[x]*2.5)
    
    # this is modolo function checking even number and added to newlist 
    if t % 2 == 0:
        newlist.append(t)
    x += 1

newlist


# In[24]:


### Task 2 Use LEN with control flow with for loop 
### Answer 1 using LEN

rep = ["Joe", "K", "Mike", "Joi", "Luv", "Deckard", "Wallace", "Rachel"]

for i in rep:
    if len(i) == 3 or len(i) == 6 or len(i) == 1:
        print (i, "is a replicant")
    
    else: 
        pritn(i, "is NOT a replicant")



### Answer2 without using LEN

rep = ["Joe", "K", "Mike", "Joi", "Luv", "Deckard", "Wallace", "Rachel"]

for i in range(rep):
    if i == 0 or i == 3 or i == 4 or i == 7:
        print (rep[i],"is a replicant")
    elif i == 2 or i == 5 or i == 6:
        print (rep[i], "is NOT a replicant")


# In[26]:


### Task 3 using nested for and while loop to create desired outcome

print("Human")
for r in range(2):
    k = 0
    while k < 8:

        if k % 2 == 0:

            print("Question")

        elif k > 3 and k < 7:

            print("CELL")

        elif k == 3:

            print("INTERLINKED")

        else:

            print("CELL WITHIN CELLS")

        k+= 1

print("Time to Finish")


# In[ ]:




