## A list is a collecion of data  that stores multiple items in a single variable##

price_usd = [12789.12,34578.32,143675.45]

print(price_usd)

print(price_usd[0])

are_m2 = [185.0,82.0,235.0]
print(are_m2)

#accessing item from the list#

print(are_m2[-3])
print(price_usd[-2])

#adding variable in a list using append#
price_usd = [12789.12,34578.32,14367.45]

print(price_usd)

price_usd.append(47690.67)

print(price_usd)

area_m2 = [187.0,82.5,235.80]
print(area_m2)

area_m2.append(564.78)
print(area_m2)

#Aggregating items#
#sum#

total_usd = sum(price_usd)
print(total_usd)

#Average
average_area_m2 = sum(area_m2)/len(area_m2)
M2 =len(area_m2)
print(M2)

#ZIPPING ITEMS#
Banana = [30,25,65,67]
print(Banana)

Names = ["January","october","April","May"]
print(Names)

#Zipp both Names and Bananas#

Banana_names =zip(Banana,Names)
zipped_list = list(Banana_names)
print(zipped_list)

# zip Age and Name of individuals#

Names = ["emmanuel","Eugine","Mercy","Gedion"]
print(Names)

Age = [ 24,34,56,72]
print(Age)

Names_age = zip(Names,Age)
zipped_variables = list(Names_age)

print(zipped_variables)

variable = type(zipped_variables)
print(variable)

