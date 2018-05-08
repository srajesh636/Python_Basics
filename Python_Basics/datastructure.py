#there are different data structure in python
'''
List
Tupples
'''

#List are nothng but like arrays in C ,But here we can create a array of different datatypes
#list=[  ,   ,  , ]

a=['a',1,1.0,'hello']
print(a[3])

#tupples are similiar to List but once a element is put in Tupple cannot be modified

d=(1,'hello')
print(d[0])

#List vs tupples

# d[0]=2   (here this gives an error if we try to reassign values in tupples)

a[0]="changed"
