#Append Items

list = ["apple", "banana", "cherry"]
list.append("orange")
print(list)

#Insert Items

list = ["apple", "banana", "cherry"]
list.insert(1, "orange")
print(list)

#Extend List

list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
list.extend(tropical)
print(list)

#Add Any Iterable

list = ["apple", "banana", "cherry"]
tuple = ("kiwi", "orange")
list.extend(tuple)
print(list)