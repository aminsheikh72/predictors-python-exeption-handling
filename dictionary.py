d = {10 : 100, 20 : 200, 30 : 300, 40 : 400, 50 : 500}
# print(d.get(10))
# print(d.keys())
# print(d.values())
# print(d.items())
# d.update({10 : 1000})
# d.pop(10)
# d.popitem()
# d.clear()
# s = d.copy()
# s.clear()
# print(s)
# d[100] = 1000
# d.setdefault(60, 600)
# a = [10,20,30]
# d2 =dict.fromkeys(a,100)
# print(d2)


# Q1. Dictionary banao
# d = {}
# d["name"] = "eskills"
# d["city"] = "barwani"
# print(d)

# Q2. Value access karo
# student = {
# "name": "Rahul",
# "marks": 85,
# "class": 12
# }
# print(student["name"],student["marks"])

# Q3. Value update karo
# product = {"name": "Pen", "price": 100}
# product["price"] = 150
# product.update({"price" : 150})
# print(product)

# Q4. New key add karo
# Dictionary mein "color": "red" add karo.
# Given code:
# car = {"brand": "Tata", "model": "Nexon"}
# car.update({"color": "red"})
# print(car)

# Q5. Key delete karo
# Dictionary se "age" key delete karo.
# Given code:
# person = {"name": "Amin", "age": 20, "city": "Indore"}
# person.pop("age")
# del person["age"]
# print(person)

# Q6. Dictionary par loop lagao
# Har key aur value ko alag-alag print karo.
# Given code:
# fruits = {"apple": 50, "banana": 30, "mango": 80}
# for key,value in fruits.items():
#     print(key,value)


# Q7. Values ka sum nikalo
# Sabhi students ke marks ka total calculate karo.
# Given code:
marks = {"Amit": 70, "Ravi": 80, "Amin": 90}
# sum = 0
# for i in marks.values():
#     sum += i

# print(sum)

# sum = sum(marks.values())
# print(sum)

# Q8. Key exist karti hai ya nahi?
# Check karo ki "email" key dictionary mein hai ya nahi.
# Given code:
# user = {"name": "Amin", "age": 20,"email" : "aminsheikh@gmail.com"}
# if "email" in user:
#     print("Email key exis")
# else:
#     print("Email does not exist")


# Q9. Maximum value nikalo
# Sabse zyada marks kis student ke hain? Uska naam aur marks print karo.
# Given code:
marks = {"Amit": 75, "Ravi": 92, "Amin": 88}

# max = 0
# for i in marks.values():
#     if i > max:
#         max = i

# print(max) 

# max = max(marks.values())
# print(max)

# Q10. keys(), values(), items()
# In teeno methods ka use karke dictionary ki keys, values aur key-value pairs print karo.
# Given code:
# mobile = {"brand": "Samsung", "price": 20000, "ram": "8GB"}
# print(mobile.keys())
# print(mobile.values())
# print(mobile.items())

# Q11. Character frequency
# String ke har character ke aane ki frequency count karke dictionary banao.
# Given code:

text = "banana"

# d = {}
# for i in text:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] +=1

# print(d)

# Q12. Number frequency
# List ke har number ki frequency dictionary mein store karo.
# Given code:
# numbers = [1, 2, 2, 3, 1, 2, 4, 3]
# d = {}
# for i in numbers:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] +=1

# print(d)

# Q13. Do dictionaries merge karo
# Dono dictionaries ko ek dictionary mein merge karo.
# Given code:
# a = {"name": "Amin", "age": 20}
# b = {"city": "Indore", "course": "Python"}

# print(a | b)

# Q14. Nested dictionary
# Har student ke math aur science marks print karo.
# Given code:
# students = {
# "Amin": {"math": 80, "science": 90},
# "Ravi": {"math": 70, "science": 85}
# }
# for name,subject in students.items():
#     print(name)
#     for subject,marks in subject.items():
#         print(subject,marks)
