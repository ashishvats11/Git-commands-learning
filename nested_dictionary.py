# in this we will be looking at the nested dictionaries and how we can create nested dictionay and loop them

# creating a nested dictionary

myfamily = {
    "child1":{"name":"Ashish","age" : 24},
    "child2":{"name":"Palak", "age":24},
    "child3":{"name":'Ashu',"age":100}

}

print(f'This is the nested loop {myfamily}\n')

# We can aslo create a dictionary that will contain other dictionaries

d1 = {"name":'Homelander', 'age':32}
d2 = {"name":'Butcher', 'age':40}
d3 = {"name":'Queen Maeve', 'age':37}

supes = {
    "supe1":d1,
    "supe2":d2,
    "supe3":d3
}

print(f'The supes dictionary created by using three differenet dictionaries {supes}')

# Access the item in a nested dictionary
print(f'Accessing the nested dictionary value \'{supes['supe2']["name"]}\'') # in this we passed the key name

# Accessing the nested dictionary elements using the .get()
print(f'Accesing the nested dictionary value \'{supes.get("supe1").get('name')}\'') # notice we have used .get() two times to get the key of the nested key


#length of the nested dictionary 
print(f'Length of the nested dictionary {len(supes)}') # the length is based on how many key value pair is there in the dictionary

# Looping through the nested dictionaries
print("The for loop in nested dictionay")
for i, obj in supes.items():
    print(i, end = '--> ')
    for j in obj:
        print(j,':',obj[j])
