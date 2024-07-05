# LAB-Python-Functional-Programming-and-Error-Handling
![](https://user-images.githubusercontent.com/970858/63474771-d6734700-c469-11e9-83bb-9429da563909.png)

# LAB-Python-Data-Structures-and-Functions

## Introduction

> ***Note:*** _This can be a pair programming activity or done independently._

In the hidden village of Konoha, the Fifth Hokage faced a new threat, but this time not in the form of bijus. The village had suffered a cybernetic ninja attack that damaged and disrupted its communication systems and vital mission data. 
Tsunade has tasked you as the chief ninja programmer of Konoha and you will have to fix all the data errors. 

![Tsunade](https://static.wikia.nocookie.net/naruto/images/3/39/Sello_Fuerza_de_un_Centenar_Anime.png/revision/latest?cb=20130725152120&path-prefix=es)

> ⚠️ **Warning:**  ninjas only use the functions lambda, map, reduce and filter any other way of doing the mission will not be approved by Tsunade.

*Do not fail us shinobi !!!!*

## Requirements

- [Learn how to fork this repo](https://guides.github.com/activities/forking/)
- Clone this repo into your `code/labs` folder


---
## Iteration 1 / **Add_the_positives_results**

<img src="https://narutoversity.wordpress.com/wp-content/uploads/2017/11/mission-rankings.jpg" height="200" />

 It helps to analyze the results of the missions, the enemy has damaged it by adding negative numbers in the list, create a new list with only the positive results and add them up.
 Creates an error handling for data other than numbers!!
```
input => output

[1,-4,7,Katana,-2, -7,10,-1,shuriken] => 1 + 7 + 10 = 21
```

## Iteration 2
<img src="https://static.wikia.nocookie.net/naruto/images/2/20/Sakura_Haruno_Parte_II_Anime.png/revision/latest?cb=20140318191249&path-prefix=es" height="200" />
### Iteration 2.1 / **Count_the_color**

Sakura needs to know how many times a specific color has been used in medical reports.Write a function that prompts the user for a color and counts the number of times it appears in the list.
Creates an custom error handling for input data other than strings or are not in the list. !!
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

<img src="https://img.wattpad.com/cover/359580473-288-k223324.jpg" height="200" />


Tsunade needs to organize the missions by name length to prioritize them.Write a function that takes a list of strings as an argument and returns an ordered list containing the same strings, sorted from shortest to longest.

```
input => output

["Rescue", "Infiltrate", "Guard", "Retrieve", "Investigate", "Defend", "Escort", "Patrol", "Eliminate", "Capture"] => ["Guard", "Rescue", "Defend", "Escort", "Patrol", "Retrieve", "Capture", "Eliminate", "Infiltrate", "Investigate"]

```

### Iteration 4 / **Calculate Total Strength**



 You need to calculate the total strength of the konoha ninja for the 5th ninja war. For this Tsunade has given you a quick list of the best ninja, make sure it contains no mistakes.
 
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
5. Handles the error of strength being a string
6. Print the total strength of the ninjas.

### Iteration 5 / **Calculate who are the strongest**
<img src="https://i.redd.it/v87hd4k0wno61.jpg" height="200" />
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
### Iteration 6 / **Get the Ninja Names**

Use lambda and map to get a list of the names of the ninjas in capital letters.

## BONUS - **get_best_students**

Create a function get_best_students that takes a dictionary of students. The function must return a dictionary with the emails and the average of the students. These students must have a average value of 9 or more in their subjects. The output have to be orderer by average mark.
For example:
```
students = [
    {"name": "Naruto", "age": 17, "email": "naruto@konoha.com", "subjectsMarks": [9, 8, 10, 5, 10]},
    {"name": "Sasuke", "age": 17, "email": "sasuke@konoha.com", "subjectsMarks": [9, 8, 10, 9, 10]},
    {"name": "Sakura", "age": 17, "email": "sakura@konoha.com", "subjectsMarks": [9, 10, 10, 9, 10]},
    {"name": "Shikamaru", "age": 17, "email": "shikamaru@konoha.com", "subjectsMarks": [8, 8, 7, 6, 8]}
]
getBestStudents(students)
returns [
    {"email": "sakura@konoha.com", "average": 9.6},
    {"email": "sasuke@konoha.com", "average": 9.2},
    {"email": "naruto@konoha.com", "average": 8.4}
]

```
<img src="https://i.pinimg.com/736x/20/12/66/2012668cdd0a8b4d53bd106ac5626443.jpg" />


## Submission

Upon completion, run the following commands:

```
$ git add .
$ git commit -m "done"
$ git push origin main
```

Then create a Pull Request!!

![happy_coding](https://user-images.githubusercontent.com/970858/63899010-c23fc480-c9ea-11e9-84a2-542907e42362.png)
