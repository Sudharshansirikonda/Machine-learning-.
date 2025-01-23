#!/usr/bin/env python
# coding: utf-8

# In[1]:


#I am creating a variable named num1 which is having a int value
num1 = 10
num2 = 20


# In[2]:


num1
num2


# In[3]:


''' This is a multli
line comment'''


# In[4]:


user = input("Enter your name: ")


# In[5]:


user


# In[6]:


name = 'Alice'
age = 30
height = 5.5
is_student = True


# In[7]:


type(is_student)


# In[8]:


type(height)


# In[9]:


type(age)


# In[10]:


type(name)


# In[11]:


#Create two variables


# In[1]:


import pandas as pd
reading_time = [10,9,6,11,5]
student_name = ["Shiva","Bhavagna","Snehith","Sudharshan","Sai"]
roll_no = [630,626,629,627,625]
dict1 = {"reading_time":screen_time,"student_name":stu_name,"roll_no":id}
print(dict1)


# In[ ]:


df = pd.DataFrame(dict1)


# In[ ]:


df


# In[ ]:


list1 = [1,2,3,4,5]
res = [i+5 for i in list1]
print(res)


# In[ ]:


list = [1,2,3,4]
a = [i for i in list if i%2==0]
a


# In[ ]:


dict1 = {"a":12,"abc":123,"dfe":45}
res = {value:key for key,value in dict1.items()}
res


# In[ ]:


keys = ["name","age"]
values = ["sudha",20]
dict2 = {k:v for k,v in zip(keys,values)}
dict2


# In[ ]:


import math 
numbers = [1,4,9,16,25]
sq = tuple(math.sqrt(i) for i in numbers)
sq


# In[ ]:


dict3 = [
    {'name':'phone','price':800},
    {'name':'tab','price':500}
]
a = {i['name']:i['price'] for i in dict3 if i['price']<=500}
print(a)
    


# In[ ]:


res = [x**2 for x in range(1,50)]
resu = [x**2 for x in range(1,20)]
print(res)


# In[ ]:


print(resu)


# In[ ]:


a = 'madam'
if a==a[::-1]:
    print(True)
else:
    print(False)


# In[ ]:


words = ['madam','radar','abc']
res = [i for i in words if i==i[::-1]]
res


# In[ ]:


lst = [1,2,3,4]
iteration = iter(lst)
print(iteration)


# In[ ]:


for i in iteration:
    if i%2==0:
        print(i)


# In[ ]:


type(iteration)


# In[ ]:


lst = [1,2,3,4,5,6,7,8,9]
lst1 = lst[3:8]
iteration = iter(lst1)
print(lst1)
print(iteration)


# In[ ]:


type(iteration)


# In[ ]:


for i in iteration:
    if i%2!=0:
        print(i)


# In[ ]:


for i in iteration:
    if i>5:
        print(i+1)


# In[ ]:


def square(i):
    for i in range(i):
        i = i+2
        yield i
square(10)
for i in square(10):
    print(i)


# In[ ]:


def square(i):
    for i in range(i):
        if i>5:
            i = i**2
        yield i
square(10)
for i in square(10):
    print(i)


# In[ ]:


result = lambda x,y,z:x*y*z
print(result(7,8,7))


# In[ ]:


def sample(func):
    def wrapper(item):
        item = item.upper()
        return func(item)
    return wrapper

@sample
def process(item):
    return item

result = process
print(result('Hello'))


# In[ ]:


import pandas as pd
reading_time = [10,9,6,11,5]
student_name = ["Shiva","Bhavagna","Snehith","Sudharshan","Sai"]
roll_no = [630,626,629,627,625]
dict1 = {"reading_time":reading_time,"student_name":student_name,"roll_no":roll_no}
print(dict1)


# In[ ]:


df = pd.DataFrame(dict1)


# In[ ]:


df


# In[ ]:


df.head(3)


# In[ ]:


df.tail(2)


# In[ ]:


def dev_dec(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
@dev_dec
def div(a,b):
    return a/b
div(7,77)


# In[ ]:


def smart_dev(func):
    def inner(a,b):
        if b==0:
            print("Error")
            return
        if a>b:
            a,b=b,a
        return func(a,b)
    return inner
@smart_dev
def div(a,b):
    return a/b
div(22,0)


# In[ ]:


string = "do what i say to the world"
for word in string.split():
    if len(word)%2==0:
        print(word)


# In[ ]:


str1 = "do what you want"
for word in str1.split():
    if len(word)>3:
        print(word[0])
        
        
list1 = list([str1])
list1


# In[ ]:


string2 = "session is going to start"
result = [i for i in string2.split()]
result


# In[ ]:


string3 = "Session is going to start"
res = [word for word in string3.split() if len(word)==5]
res


# In[ ]:


A = "Sudharshan"
print(A[::-1])


# In[ ]:


for i in range(1,21):
    if i%3==0 and i%5==0:
        print("big buzz")
    elif i%3==0:
        print("bizz")
    elif i%5==0:
        print("bigg")
    else:
        print(i)


# # Sales project with pandas 

# In[14]:


import pandas as pd

sales_data = {
    'tranID': [1,2,3,4],
    'custID': [101,102,103,104],
    'Amount': [100,200,300,400],
    'Date': ['12-1-24','12-2-24','12-3-24','12-4-24']
}

customer_data = {
    'custID':[101,102,103,104],
    'customerName':['sudha','bhavagna','shiva','snehith'],
    'Age': [19,20,21,22],
    'City': ['ts','ap','bihar','tamilnadu']
}

sales_df = pd.DataFrame(sales_data)
customers_df = pd.DataFrame(customer_data)
sales_df.head()


# In[15]:


customers_df.head()


# In[16]:


sales_df.shape


# In[17]:


sales_df.describe()


# In[23]:


merged_df = pd.merge(sales_df, customers_df[['custID', 'customerName', 'City']], on='custID', how='left')

merged_df[['tranID', 'customerName', 'City']]


# In[25]:


merged_df = pd.merge(sales_df, customers_df[['custID', 'customerName', 'City']], on='custID', how='inner')
merged_df


# In[26]:


merged_df = pd.merge(sales_df, customers_df[['custID', 'customerName', 'City']], on='custID', how='outer')
merged_df


# In[20]:


filtered_sales = sales_df[sales_df['Amount'] > 400]

filtered_sales['custID']


# # HISTOGRAM

# In[10]:


import matplotlib.pyplot as plt
data = [8,2,1,11,8,3,7,9,3,5,6]
plt.hist(data,bins=7,edgecolor='black')
plt.title('Simple Histogram Example')
plt.xlabel('Numbers')
plt.ylabel('Count')
plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
datf = pd.DataFrame({"Season 1":[5,8,3,2,9,4],
                    "Season 2":[1,5,2,8,6,0]})
p = sns.histplot(data=datf)
p.set(xlabel="X label Value",ylabel = 'Y label Value')
plt.show()


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.randint(20,81,1000)

plt.hist(data,bins=15,edgecolor='black',color='skyblue')

plt.title('Histogram of cancer patients')
plt.xlabel('Age')
plt.ylabel('Number of patients')
plt.show()


# In[ ]:




