#!/usr/bin/env python
# coding: utf-8

# # creating dictionary

# In[ ]:


atif={"name":"saeed","age":20,"addres":"lodhran","email":"abc@gmail.com","a":"apple","b":"aeroplane","a":"aunty"}


# In[ ]:


atif


# In[ ]:


atif["email"]


# In[ ]:


atif["age"]


# In[ ]:


atif


# In[ ]:


atif


# In[ ]:


atif


# In[ ]:


atif


# # Adding value in Dictionary

# In[ ]:


atif


# In[ ]:


atif["class"]="phd"
print(atif)


# # Update a key value in dictionary

# In[ ]:


atif["class"]="ilama iqbal"
print(atif)


# # ACCESS VALUE IN DICTIONARY

# In[ ]:


atif["b"]


# # DELETING A VALUE

# In[ ]:


del[atif]


# In[ ]:





# In[ ]:


atif={"name":"saeed","age":20,"addres":"lodhran","email":"abc@gmail.com","a":"apple","b":"aeroplane","a":"aunty"}


# In[ ]:


del atif["email"]


# In[ ]:


atif


# # key are in dictionary or not

# In[ ]:


"class" in atif


# In[ ]:


"a" in atif


# # Condition structure

# In[ ]:


patient = "schizophrenia"

if patient == "schizophrenia":
    
    print("schizophrenia patient.")


# # else and elif statements

# In[ ]:



patient=input("Enter disorder or normal:")

if patient == "schizophrenia":
  
    print("person is in schizophrenia disorder" )
else:
    print("person is in normal" )


# # Python if...elif...else Statement

# In[ ]:


patient=input("Enter disorder or normal:")

if patient == "schizophrenia":
    print("person is in schizophrenia disorder" )
elif patient =='bipolar' or  patient =='depression'or patient =='neurodevelopment' or  patient =='anxiety':
    print("sorry i can't identify")

else:
    print("person is in normal")


# # For LOOP

# In[ ]:


mental_disorder = ["bipolar", "depression", "anxiety","autism spectrum", "antisocial personality disorder"]
checked_disorder = "depression"

for a_mental_disorder in mental_disorder:
    if checked_disorder == a_mental_disorder:
        print("patient have mental disorder")


# # creating table in loop

# In[ ]:


table = int(input("Enter the number"))

for num in range(0,9):
    print(f" {table} * {num} = {table*num}")


# # nested loop in python

# In[ ]:


table = int(input("Enter the number"))

for table in range(2,table+1):
    print(" ")
    for num in range(1,15):
        
        print(f" {table} * {num} = {table*num}")


# In[ ]:




