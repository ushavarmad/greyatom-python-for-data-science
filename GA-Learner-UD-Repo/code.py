# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
# Concatenate both the strings
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = class_1 + class_2

# Append the list
print(new_class)
# Print updated list
new_class.append('Peter Warden')
print(new_class)
# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses = {"Math":65,"English":70,"History":80,"French":70,"Science":60}
total = 0
for x in courses:
    total = total + courses[x]
print(total)
percentage = total * 100 / 500
print(percentage)

mathematics = {"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}
max = 0
for x in mathematics:
    if mathematics[x] > max:
        max = mathematics[x]

print(max)
topper=""

def find_max_key(value):
    for key, value1 in mathematics.items():
        if value1== max :
            return key
topper = find_max_key(max)
print(topper)

first_name = topper.split()[0]
last_name = topper.split()[1]
print(first_name)
print(last_name)
full_name=last_name+" "+first_name
certificate_name=full_name.upper()
print(certificate_name)







# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`

# Print the total

# Insert percentage formula

# Print the percentage




# Create the Dictionary
 



# Given string


# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


