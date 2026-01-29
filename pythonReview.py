print()
message = "Forca Barca"
print(len(message))
print(message[0])
print(type(message))
print(type(3))
print(type("3"))
print(3*3)
print(3*"3")
print(len("greg")==4)

a = 10
b = 3

print(a+b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#Lists
professors = ["greg","leo","orlando","kianoosh"]
print(professors[0])
print(professors[-1])
professors.append("alberto")
print(professors)
professors.extend(["richard","jason"])
print(professors)
professors.insert(2,"pedro")
print(professors)
professors[3] = "mark"
print(professors)
print(professors[3:5]) #accessing professors in positions 3 and 4
print(professors[5:]) #starting at 5 all the way to the end
print(professors[:3]) #from 0 all the way to 2
print(professors[:]) #print everything, copy of the original list
print(professors[::-1]) #print backwards
professors.reverse()
professors.remove("kianoosh")
print(professors)
print(professors.index("mark"))
x = professors.pop(6)
print(professors)
print(x)
print(len(professors))
print(type(professors))
professors.sort(reverse=True)
print(professors)

#For loops
for i in professors:
    print(i.title()) #print with capitalized first letter
    print("FIU")
print()
print("FIU")

water_data = {
    "temperature":[78,89,92],
    "pH":[6.5,6.7,6.3],
    "oxygen": [7.2,5.6,3.5]
}

print(water_data["oxygen"])

print(water_data.keys())
print(water_data.values())

import pandas as pd

df = pd.DataFrame(water_data)
print(df)




