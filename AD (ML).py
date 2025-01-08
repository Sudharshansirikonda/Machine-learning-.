#!/usr/bin/env python
# coding: utf-8

# In[10]:


#I am creating a variable named num1 which is having a int value
num1 = 10
num2 = 20


# In[11]:


num1
num2


# In[12]:


''' This is a multli
line comment'''


# In[1]:


user = input("Enter your name: ")


# In[2]:


user


# In[4]:


name = 'Alice'
age = 30
height = 5.5
is_student = True


# In[6]:


type(is_student)


# In[7]:


type(height)


# In[8]:


type(age)


# In[9]:


type(name)


# In[10]:


#Create two variables


# In[6]:


import pandas as pd
reading_time = [10,9,6,11,5]
student_name = ["Shiva","Bhavagna","Snehith","Sudharshan","Sai"]
roll_no = [630,626,629,627,625]
dict1 = {"reading_time":screen_time,"student_name":stu_name,"roll_no":id}
print(dict1)


# In[7]:


df = pd.DataFrame(dict1)


# In[8]:


df


# In[13]:


list1 = [1,2,3,4,5]
res = [i+5 for i in list1]
print(res)


# In[19]:


list = [1,2,3,4]
a = [i for i in list if i%2==0]
a


# In[22]:


dict1 = {"a":12,"abc":123,"dfe":45}
res = {value:key for key,value in dict1.items()}
res


# In[23]:


keys = ["name","age"]
values = ["sudha",20]
dict2 = {k:v for k,v in zip(keys,values)}
dict2


# In[24]:


import math 
numbers = [1,4,9,16,25]
sq = tuple(math.sqrt(i) for i in numbers)
sq


# In[25]:


dict3 = [
    {'name':'phone','price':800},
    {'name':'tab','price':500}
]
a = {i['name']:i['price'] for i in dict3 if i['price']<=500}
print(a)
    


# In[30]:


res = [x**2 for x in range(1,50)]
resu = [x**2 for x in range(1,20)]
print(res)


# In[31]:


print(resu)


# In[47]:


a = 'madam'
if a==a[::-1]:
    print(True)
else:
    print(False)


# In[50]:


words = ['madam','radar','abc']
res = [i for i in words if i==i[::-1]]
res


# In[ ]:




