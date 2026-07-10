# list
fruits = ['mango', 'orange', 'apple', 'banana']
print(fruits)

# tuple
tuples = ('cars', 'house', 'money')

dic = {'name:', 'ikenna', 'age:', 50, 'course:', 'enterprise python'}

name = "ikenna chibor"
name = name.title()
age = 50
dob = "04/05/1976"

# indentation
if age >30:
    print(age)
    
    # f - strings
    
    print(f"my name is {name}")
    
    list = [1,4,5,7,13,50]
    
    # modify the list using append
    list.append(80)
    print(list)
    
    list.insert(3, 25)
    print(list)
    
    num = [10, 20,30,40,50,60]
    num.remove(40)
    print(num)
    
    fruits = ['orage', 'udara', 'mango', 'ube', 'orji']
    fruits.pop(2)
    print(fruits)
    
    # sort function
    fruits = ['orage', 'udara', 'mango', 'ube', 'orji']
    fruits.sort()
    print(fruits)
    
    # reverse function
    fruits = ['orage', 'udara', 'mango', 'ube', 'orji']
    fruits.reverse()
    print(fruits)

    # len function
    fruits = ['orage', 'udara', 'mango', 'ube', 'orji']
    fruits = len(fruits) # count number of items in fruits
    print(fruits)
    
    # dictionary
    student = {'name': 'ikenna', 'age': 50, 'score': 80.5}
    # access items in a dictionary
    
    # print(student['model'])
    print(student.get('name'))
    
    # Update
    student['grade'] = 'A+'
    student['name']
    student['name'] = 'ikenna chibor'    
    
    print(f'this is my profile: {student}')
    
    # class exercise
    #dictionary
    book = {"title": "fallen heros", "author": "ikenna chibor", "year": "2005", "price": "$1000"}
    # update 
    book["price"] = "$500"
    book["in store"] = "True"
    print(book)
    print(book["title"])
    print(book["author"])
    print(book["year"])
    print(book["price"])