# LAB-Python-Functional-Programming-and-Error-Handling
![](https://user-images.githubusercontent.com/970858/63474771-d6734700-c469-11e9-83bb-9429da563909.png)

# LAB-Python-Data-Structures-and-Functions

## Introduction

> ***Note:*** _This can be a pair programming activity or done independently._

In the hidden village of Konoha, the Fifth Hokage, Tsunade, faced a new threat, not in the form of bijus or colossal beasts, but in a challenge that demanded technological skills. The village had suffered a cybernetic ninja attack that compromised its communication systems and vital mission data. The digital firewalls protecting sensitive village information were compromised, and the data had become damaged and disorganized.
Tsunade has tasked you as the chief ninja programmer of Konoha and you will have to fix all the data errors. 

> ⚠️ **Warning:**  ninjas only use the functions lambda, map, reduce and filter any other way of doing the mission will not be approved by Tsunade.
> 
![Tsunade](https://static.wikia.nocookie.net/naruto/images/3/39/Sello_Fuerza_de_un_Centenar_Anime.png/revision/latest?cb=20130725152120&path-prefix=es)

## Requirements

- [Learn how to fork this repo](https://guides.github.com/activities/forking/)
- Clone this repo into your `code/labs` folder


---
## Iteration 1 / **Add_the_positives**

Create a function in which you get a tuple of numbers, and return the sum of all positive numbers:
```
input => output

[1,-4,7,-2, -7,13] => 1 + 7 + 13 = 21
```

## Iteration 2

### Iteration 2.1 / **Count_the_color**

Write a function that asks the user for a color and counts the number of times it appears in the list.
```
["red", "blue", "red", "white", “green”, “black”, “orange”, “black”, “red”]

input => output

blue => the color blue appears 2 times.
```
### Iteration 2.2 / **Count_the_color_multidimensional** 

try now to search in a multidimensional list
```
[
["red", "blue", "red", "white"],
["yellow", "red", "blue", "green"],
["white", "red", "blue", "yellow"],
["green", "black", "orange", "orange"]
]
```
## Iteration 3 / **strings_order**

Write a function that takes a list of strings as an argument and returns a sorted list containing the same strings, ordered from shortest to longest.
```
input => output

["Multidimensional", "Earth", "Try", "Banana"] => ["Try", "Earth", "Banana", "Multidimensional"]
```

## Iteration 4

### Iteration 4.1 / **Fix_the_string**

This function has to return the join of the firstName and the lastName attributes of the person argument with a space between them. Also it has to transform the first letter of both values to upperCase if necessary.
```
input --> output

{ firstName : 'Luis' , lastName: 'burón' } => "Luis Burón"
```
### Iteration 4.2 / **Fix_the_dictionary**

This function has to return the join of the firstName and the lastName attributes of the person argument with a space between them. Also it has to transform the first letter of every word of both values to upperCase if it is necessary. In this case, you can receive as lastName or firstName value a compound name.
```
input => output

{ firstName : 'Luis Álvaro' , lastName: 'burón mejías' } => "Luis Álvaro Burón Mejías"
```
## Iteration 5


### Iteration 5.1 / **Calculate Total Strength**

The Hokage of Konoha has assigned you an important mission. You need to calculate the total strength of the konoha ninja for the 5th ninja war. For this Tsunade has given you a quick list of the best ninja, make sure it contains no mistakes.
```
ninjas = [
    {'name': 'Naruto', 'strength': 9000},
    {'name': 'Sasuke', 'strength': 8500},
    {'name': 'Sakura', 'strength': 'high'},
    {'name': 'Kakashi', 'strength': 9500},
    {'name': 'Rock Lee', 'strength': 8000},
    {'name': 'Hinata', 'strength': 'unknown'}
]
```

1. Import the necessary module (reduce from functools).
2. Copy the list of ninjas.
3. Make a function that receives the ninja object and checks with a try if it is a number or not. 
4. Use reduce into the function together with a lambda function to sum the strength.
5. Print the total strength of the ninjas.

### Iteration 5.2 / **Calculate Total Strength**

We already know the total strength of konoha but now we will need to know who are the strongest .
Make a function that receives the object and a strength number.
The function should return the ninjas that have a strength equal to or greater than what you have passed to the function. 

Example : 
```
def filter_ninjas_by_strength(ninjas, threshold):
    try:
     return 
    except ValueError:
        return "Error: strength threshold must be a number."

print(filter_ninjas_by_strength(ninjas, 8000)) # Output: [{'name': 'Naruto', 'strength': 9000}]]
print(filter_ninjas_by_strength(ninjas, 'high')) # Output: "Error: strength threshold must be a number."
```
### Iteration 5.2 / **Get the Ninja Names**

Use lambda and map to get a list of the names of the ninjas in capital letters.

## BONUS - **get_best_students**

Create a function get_best_students that takes a dictionary of students. The function must return a dictionary with the emails and the average of the students. These students must have a average value of 9 or more in their subjects. The output have to be orderer by average mark.
For example:
```
getBestStudents([
  {name : "Luis", age : 20, email : "luis@gmail.com", subjectsMarks : [9, 8, 10, 5 , 10]},
  {name : "Luigi", age : 14, email : "luigi@gmail.com", subjectsMarks : [9, 8, 10, 9 , 10]},
  {name : "Mario", age : 25, email : "mario@gmail.com", subjectsMarks : [9, 10, 10, 9, 10]},
])

returns [
  {email : "mario@gmail.com", average : 9.6 }, 
  {email : "luis@gmail.com", average : 9.2 }
 ]
```
## Submission

Upon completion, run the following commands:

```
$ git add .
$ git commit -m "done"
$ git push origin main
```

Then create a Pull Request!!

![happy_coding](https://user-images.githubusercontent.com/970858/63899010-c23fc480-c9ea-11e9-84a2-542907e42362.png)
