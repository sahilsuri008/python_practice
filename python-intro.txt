Printing
Code
Text
[ ]
 print("Hello world")
 Hello world
Create Variable and Use Variable
[ ]
 variable = "armbar"
variable
 
Multiple procedural statements
[ ]
 attack_one = "kimura"
attack_two = "arm triangle"
print("In Brazilian Jiu Jitsu a common attack is a:", attack_one)
print("Another common attack is a:", attack_two)
 In Brazilian Jiu Jitsu a common attack is a: kimura
Another common attack is a: arm triangle
Adding Numbers
[ ]
 1+1
 2
Adding Phrases
[ ]
 "arm" + " bar"+" 4"+" morestuff " + "lemon"
 
Complex statements
More complex statements can be created that use data structures like the belts variable, which is a list.
[ ]
 belts = ["white", "blue", "purple", "brown", "black"]
for belt in belts:
    if "black" in belt:
        print("The belt I want to be is:", belt)
    else:
        print("This is not the belt I want to end up at:", belt)
 This is not the belt I want to end up at: white
This is not the belt I want to end up at: blue
This is not the belt I want to end up at: purple
This is not the belt I want to end up at: brown
The belt I want to be is: black
Strings and String Formatting

Strings are a sequence of characters and they are often programmatically formatted. Almost all Python programs have strings because they can be used to send messages to users who use the program. When creating strings there are few core concepts to understand:
Strings can be create with the single, double and triple/double quotes
Strings are can be formatted
One complication of strings is they can be encoded in several formats including unicode
Many methods are available to operate on strings. In an editor or IPython shell you can see these methods by tab completion:
basic_string.
          capitalize()   format()       islower()      lower()        rpartition()   title()         
          casefold()     format_map()   isnumeric()    lstrip()       rsplit()       translate()     
          center()       index()        isprintable()  maketrans()    rstrip()       upper()         
          count()        isalnum()      isspace()      partition()    split()        zfill()         
          encode()       isalpha()      istitle()      replace()      splitlines()                  
          endswith()     isdecimal()    isupper()      rfind()        startswith()                  
          expandtabs()   isdigit()      join()         rindex()       strip()                       
          find()         isidentifier() ljust()        rjust()        swapcase()        
[ ]
 my_string = "this is a string I am using this time"
my_string.split()
#my_string.upper()
#my_string.title()
#my_string.count("this")
 ['this', 'is', 'a', 'string', 'I', 'am', 'using', 'this', 'time']
[ ]
 my_string.capitalize()
 
[ ]
 my_string.isnumeric()


 False
[ ]
 print(my_string)
var2 = my_string.swapcase()
print(var2)
print(var2.swapcase())
 this is a string I am using this time
THIS IS A STRING i AM USING THIS TIME
this is a string I am using this time
Basic String
[ ]
 basic_string = "Brazilian Jiu Jitsu"
Splitting String
Turn a string in a list by splitting on spaces, or some other thing
[ ]
 #split on spaces (default)
basic_string.split()
 ['Brazilian', 'Jiu', 'Jitsu']
[ ]
 result = basic_string.split()
len(result)
 3
[ ]
 #split on hyphen
string_with_hyphen = "Brazilian-Jiu-Jitsu"
string_with_hyphen.split("-")
 ['Brazilian', 'Jiu', 'Jitsu']
[ ]
 #split on comma
string_with_hyphen = "Brazilian,Jiu,Jitsu"
string_with_hyphen.split(",")
 ['Brazilian', 'Jiu', 'Jitsu']
All Capital
Turn a string into all Capital Letter
[ ]
 basic_string.capitalize()
 'Brazilian jiu jitsu'
Slicing Strings
Strings can be referenced by length and sliced
[ ]
 #Get the last character
basic_string[-1:]
 
[ ]
 len(basic_string[2:])
 17
[ ]
 #Get length of string
len(basic_string)
 19
[ ]
 basic_string[-18:]
 
Strings Can Be Added Together
[ ]
 basic_string + " is my favorite Martial Art"
 
[ ]
 items = ["-",1,2,3]
for item in items:
  basic_string += str(item)
basic_string
 
[ ]
 "this is a string format: %s" % "wow"
 
F-Strings Can Be Formatted in More Complex Ways
One of the best ways to format a string in modern Python 3 is to use f-strings
[ ]
 f'I love practicing my favorite Martial Art, {basic_string}'
 
[ ]
 fruit = 'apple'
f'I love this {fruit}'
 
Strings Can Use Triple Quotes to Wrap
[ ]
 f"""
This phrase is multiple sentenances long.
There phrase can be formatted like simpler sentances,
for example, I can still talk about my favorite Martial Art {basic_string}
"""
 
Line Breaks Can Be Removed with Replace
The last long line contained line breaks, which are the \n character, and they can be removed by using the replace method
[ ]
 f"""
This phrase is multiple sentenances long.
There phrase can be formatted like simpler sentances,
for example, I can still talk about my favorite Martial Art {basic_string}
""".replace("\n", " ")
 
Numbers and Arithmetic Operations

Python is also a built-in calculator. Without installing any additional libraries it can do many simple and complex arithmetic operations.
Adding and Subtracting Numbers
[ ]
 steps = (1+1)-1
print(f"Two Steps Forward:  One Step Back = {steps}")
 Two Steps Forward:  One Step Back = 1
Multiplication with Decimals
Can use float type to solve decimal problems
[ ]
 body_fat_percentage = 0.10
weight = 200
fat_total = body_fat_percentage * weight
print(f"I weight 200lbs, and {fat_total}lbs of that is fat")
 I weight 200lbs, and 20.0lbs of that is fat
Can also use Decimal Library to set precision and deal with repeating decimal
[ ]
 from decimal import (Decimal, getcontext)

getcontext().prec = 5
Decimal(1)/Decimal(3)


 Decimal('0.33333')
Using Exponents
Using the Python math library it is straightforward to call 2 to the 3rd power
[ ]
 import math
math.pow(2,4)
 16.0
Can also use built in exponent operator to accomplish same thing
[ ]
 2**3
 8
[ ]
 2**4
 16
this is regular multiplication
[ ]
 2*3
 6
Converting Between different numerical types
There are many numerical forms to be aware of in Python. A couple of the most common are:
Integers
Floats
[ ]
 number = 100
num_type = type(number).__name__
print(f"{number} is type [{num_type}]")
 100 is type [int]
[ ]
 number = float(100)
num_type = type(number).__name__
print(f"{number} is type [{num_type}]")
 100.0 is type [float]
[ ]
 num2 = 100.20
type(num2)
 float
[ ]
 class Foo:pass
f = Foo()
[ ]
 type(f)
 __main__.Foo
Numbers can also be rounded
Python Built in round
[ ]
 too_many_decimals = 1.912345897
round(too_many_decimals, 6)
#get more info
#round?
 1.912346
Numpy round
[ ]
 import numpy as np
np.round(too_many_decimals, 6)
 1.912346
Pandas round
[ ]
 import pandas as pd
df = pd.DataFrame([too_many_decimals], columns=["A"], index=["first"])
df.round(2)

 
Simple benchmark of all three (Python, numpy and Pandas round): using %timeit
*Depending on what is getting rounded (i.e. a very large DataFrame, performance may very, so knowing how to benchmark performance is important with round) *
[ ]
 print("built in Python Round")
%timeit round(too_many_decimals, 2)

print("numpy round")
%timeit np.round(too_many_decimals, 2)

print("Pandas DataFrame round")
%timeit df.round(2)
 built in Python Round
The slowest run took 59.70 times longer than the fastest. This could mean that an intermediate result is being cached.
1000000 loops, best of 3: 423 ns per loop
numpy round
The slowest run took 8.10 times longer than the fastest. This could mean that an intermediate result is being cached.
100000 loops, best of 3: 8.2 µs per loop
Pandas DataFrame round
1000 loops, best of 3: 773 µs per loop
Presentation: Lists and Dictionaries

Python has a couple of core Data Structures that are used very frequently
Lists
Dictionaries
Dictionaries and lists are the real workhorses of Python, but there are also other Data Structers like tuples, sets, Counters, etc, that are worth exploring too.
Python Dictionaries

The workhorse of Python datastructures
Creating Python Dictionaries

Creating Python Dictionaries can be done with* brackets {}*
[ ]
 #bad_dictionary = {[2]:"one"}
[ ]
 new_dictionary = {"one":1}
[ ]
 submissions = {"armbar": "upper_body", 
               "arm_triangle": "upper_body", 
               "heel_hook": "lower_body", 
               "knee_bar": "lower_body"}
#type(submissions)
#submissions.items?
submissions
 {'arm_triangle': 'upper_body',
 'armbar': 'upper_body',
 'heel_hook': 'lower_body',
 'knee_bar': 'lower_body'}
[ ]
 new_dict =dict(upper_body="lower_body")
new_dict
 {'upper_body': 'lower_body'}
Using Python Dictionaries

A common dictionary usage pattern is to iterate on a dictionary by using the items method. In the example below the key and the value are printed:
[ ]
 #submissions.items?

[ ]
 for submission, body_part in submissions.items():
    print(f"The {submission} is an attack on the {body_part}")
 The armbar is an attack on the upper_body
The arm_triangle is an attack on the upper_body
The heel_hook is an attack on the lower_body
The knee_bar is an attack on the lower_body
Dictionaries can also be used to filter. In the example below, only the submission attacks on the lower body are displayed:
[ ]
 for _, body_parts in submissions.items():
  print(body_parts)
 upper_body
upper_body
lower_body
lower_body
[ ]
 print(f"These are lower_body submission attacks in Brazilian Jiu Jitsu:")
for submission, body_part in submissions.items():
    if body_part == "lower_body":
        print(submission)
 These are lower_body submission attacks in Brazilian Jiu Jitsu:
heel_hook
knee_bar
Dictionary keys and values can also be selected with built in keys() * and *values() methods
[ ]
 print(f"These are keys: {submissions.keys()}")
print(f"These are values: {submissions.values()}")
 These are keys: dict_keys(['armbar', 'arm_triangle', 'heel_hook', 'knee_bar'])
These are values: dict_values(['upper_body', 'upper_body', 'lower_body', 'lower_body'])
Key lookup is very performant, and one of the most common ways to use a dictionary.
[ ]
 if "armbar" in submissions:
  print("found key")
  
 found key
[ ]
 print("timing key membership")
%timeit if "armbar" in submissions: pass 
 timing key membership
10000000 loops, best of 5: 52.8 ns per loop
Python Lists

Lists are also very commonly used in Python. They allow for sequential collections. Lists can hold dictionaries, just as dictionaries can hold lists.
Creating Lists

One way to create lists is with *[] syntax*
[ ]
 list_of_bjj_positions = ["mount", "full-guard", "half-guard", 
                         "turtle", "side-control", "rear-mount", 
                         "knee-on-belly", "north-south", "open-guard"]
Another method os creating lists is with built in list() method
[ ]
 bjj_dominant_positions = list()
bjj_dominant_positions.append("side-control")
bjj_dominant_positions.append("mount")
bjj_dominant_positions

 ['side-control', 'mount']
Yet another way, very performant way to create lists is to use list comprehension syntax
[ ]
 guards = "full, half, open"
guard_list = [f"{guard}-guard" for guard in guards.split(",")]
guard_list

 ['full-guard', ' half-guard', ' open-guard']
Using Lists

For loops are one of the simplist ways to use a list.
[ ]
 for position in list_of_bjj_positions:
    if "open" in position: #explore on your own "guard"
        print(position)
 open-guard
Lists can also be used to select elements by slicing.
[ ]
 print(f'First position: {list_of_bjj_positions[:1]}')
print(f'Last position: {list_of_bjj_positions[-1:]}')
print(f'First three positions: {list_of_bjj_positions[0:3]}')
 First position: ['mount']
Last position: ['open-guard']
First three positions: ['mount', 'full-guard', 'half-guard']
Lists can also be used to unpack powerful, succinct statements when used with built-in functions like zip.
[ ]
 bjj_position_matrix = [
    ["dominant", "top-mount", "back-mount", "side-control"],
    ["neutral", "open-guard", "full-guard", "standing"],
    ["weak", "turtle", "bottom-back-mount", "bottom-mount"]
]
list(zip(*bjj_position_matrix))
 [('dominant', 'neutral', 'weak'),
 ('top-mount', 'open-guard', 'turtle'),
 ('back-mount', 'full-guard', 'bottom-back-mount'),
 ('side-control', 'standing', 'bottom-mount')]
[ ]
 zip?
Python Sets

Sets are unordered unique collections
Creating Python Sets

Sets can be created by using built-in sets() method
[ ]
 unique_attacks = set(("armbar","armbar", "armbar", "kimura", "kimura", "heel hook"))
print(type(unique_attacks))
unique_attacks
 <class 'set'>
{'armbar', 'heel hook', 'kimura'}
Using Sets

One of the most powerful ways to use sets is to find the differences between to collections
[ ]
 attacks_set_one = set(("armbar", "kimura", "heal-hook"))
attacks_set_two = set(("toe-hold", "knee-bar", "heal-hook"))
unique_set_one_attacks = attacks_set_one - attacks_set_two
print(f"Unique Set One Attacks {unique_set_one_attacks}")

 Unique Set One Attacks {'kimura', 'armbar'}
Exercise: Write a dictionary with a mutable key.

Double-click (or enter) to edit
[ ]
 good = {'one': 'two'}
[ ]
 # A list is mutable
var = ["two"]
badone = {var:"two"}
 
[ ]
 # be careful about mutating objects
class Foo:pass
foo = Foo()

bad_two = {foo: "two"}
[ ]
 # try out why this is weird

def fun():pass
bad_three = {fun:"one"}

Presentation: Functions, Lazy Expressions, Async and Concurrency

Read related material covered in Chapter 1 (Functions Section) of Pragmatic AI
Watch video section 2: Writing and Applying Functions
Writing Functions
Function arguments: positional, keyword
Functional Currying: Passing uncalled functions
Functions that Yield
Decorators: Functions that wrap other functions
Making Classes Behave Like Functions
Applying a Function to a Pandas DataFrame
Writing Lambdas
Writing Functions

Learning to write a function is the most fundamental skill to learn in Python. With a basic mastery of functions, it is possible to have an almost full command of the language.
Simple function
The simplest functions just return a value.
[ ]
 def favorite_martial_art():
    return "bjj"
[ ]
 print(favorite_martial_art())
# This is the same output
my_variable = "bjj"
my_variable
 
[ ]
 def myfunc():pass
[ ]
 res = myfunc()
print(res)
#result = myfunc()
#print(result)
 None
Documenting Functions
It is a very good idea to document functions.
In Jupyter Notebook and IPython docstrings can be viewed by referring to the function with a ?. ie.
In [2]: favorite_martial_art_with_docstring?
Signature: favorite_martial_art_with_docstring()
Docstring: This function returns the name of my favorite martial art
File:      ~/src/functional_intro_to_python/<ipython-input-1-bef983c31735>
Type:      function
[ ]
 def favorite_martial_art_with_docstring():
    """This function returns the name of my favorite martial art
    This is more
    This is even more
    return "string"
    """
    return "bjj"
Docstrings of functions can be printed out by referring to __doc__
[ ]
 #favorite_martial_art_with_docstring.__doc__
favorite_martial_art_with_docstring?

[ ]
 #favorite_martial_art_with_docstring?
Function arguments: positional, keyword

A function is most useful when arguments are passed to the function. New values for times are processed inside the function. This function is also a 'positional' argument, vs a keyword argument. Positional arguments are processed in the order they are created in.
[ ]
 def practice(times):
    print(f"I like to practice {times} times a day")
[ ]
 practice(2)
 I like to practice 2 times a day
[ ]
 practice(3)
 I like to practice 3 times a day
Positional Arguments are processed in order
Note, position is the key to pay attention to.
[ ]
 def practice(times, technique, duration):
    print(f"I like to practice {technique}, {times} times a day, for {duration} minutes")
[ ]
 practice(3, "piano", 45)
 I like to practice piano, 3 times a day, for 45 minutes
[ ]
 #Order is important, now the entire is incorrect and prints out nonsense
practice("piano", 7,60)
 I like to practice 7, piano times a day, for 60 minutes
Keyword Arguments are processed by key, value and can have default values
One handy feature of keyword arguments is that you can set defaults and only change the defaults you want to change.
[ ]
 def practice(times=2, technique="python", duration=60):
    print(f"I like to practice {technique}, {times} times a day, for {duration} minutes")
[ ]
 practice()
 I like to practice python, 2 times a day, for 60 minutes
[ ]
 practice(duration=90, times=4)
 I like to practice python, 4 times a day, for 90 minutes
**args and *kwargs
allow dynamic argument passing to functions Should be used with discretion because it can make code hard to understand
[ ]
 def attack_techniques(**kwargs):
    """This accepts any number of keyword arguments"""
    
    for name, attack in kwargs.items():
        print(f"This is an attack I would like to practice: {attack}")
[ ]
 attack_techniques(arm_attack="kimura", 
                  leg_attack="straight_ankle_lock", 
                  neck_attack="arm_triangle",
                 body_attack="charge")
 This is an attack I would like to practice: kimura
This is an attack I would like to practice: straight_ankle_lock
This is an attack I would like to practice: arm_triangle
This is an attack I would like to practice: charge
[ ]
 #I also can pass as many things as I wants
attack_techniques(arm_attack="kimura", 
                  leg_attack="straight_ankle_lock", 
                  neck_attach="arm_triangle",
                  attack4="rear nake choke", attack5="key lock")
 This is an attack I would like to practice: kimura
This is an attack I would like to practice: straight_ankle_lock
This is an attack I would like to practice: arm_triangle
This is an attack I would like to practice: rear nake choke
This is an attack I would like to practice: key lock
passing dictionary of keywords to function
**kwargs syntax can also be used to pass in arguments all at once
[ ]
 attacks = {"arm_attack":"kimura", 
           "leg_attack":"straight_ankle_lock", 
           "neck_attach":"arm_triangle"}
[ ]
 attack_techniques(**attacks)
 This is an attack I would like to practice: kimura
This is an attack I would like to practice: straight_ankle_lock
This is an attack I would like to practice: arm_triangle
Passing Around Functions
Object-Oriented programming is a very popular way to program, but it isn't the only style available in Python. For concurrency and for Data Science, functional programming fits as a complementary style.
In the example, below a function can be used inside of another function by being passed into the function itself as an argument.
[ ]
 def attack_location(technique):
    """Return the location of an attack"""
    
    attacks = {"kimura": "arm_attack",
           "straight_ankle_lock":"leg_attack", 
           "arm_triangle":"neck_attach"}
    if technique in attacks:
        return attacks[technique]
    return "Unknown"
[ ]
 attack_location("kimura")
 
[ ]
 attack_location("bear hug")
 
[ ]
 def multiple_attacks(attack_location_function):
    """Takes a function that categorizes attacks and returns location"""
    
    new_attacks_list = ["rear_naked_choke", "americana", "kimura"]
    for attack in new_attacks_list:
        attack_location = attack_location_function(attack)
        print(f"The location of attack {attack} is {attack_location}")
[ ]
 multiple_attacks(attack_location)
 The location of attack rear_naked_choke is Unknown
The location of attack americana is Unknown
The location of attack kimura is arm_attack
Closures and Functional Currying

Closures are functions that contain other nested functions with state from outer function.
In Python, a common way to use them is to keep track of the state. In the example below, the outer function, attack_counter keeps track of counts of attacks. The inner fuction attack_filter uses the "nonlocal" keyword in Python3, to modify the variable in the outer function.
This approach is called "functional currying". It allows for a specialized function to be created from general functions. As shown below, this style of function could be the basis of a simple video game or maybe for the statistics crew of a mma match.
[ ]
 #nonlocal cannot modify this variable
#lower_body_counter=5
def attack_counter():
    """Counts number of attacks on part of body"""
    lower_body_counter = 0
    upper_body_counter = 0
    #print(lower_body_counter)
    def attack_filter(attack):
        nonlocal lower_body_counter
        nonlocal upper_body_counter
        attacks = {"kimura": "upper_body",
           "straight_ankle_lock":"lower_body", 
           "arm_triangle":"upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body"}
        if attack in attacks:
            if attacks[attack] == "upper_body":
                upper_body_counter +=1
            if attacks[attack] == "lower_body":
                lower_body_counter +=1
        print(f"Upper Body Attacks {upper_body_counter}, Lower Body Attacks {lower_body_counter}")
    return attack_filter
[ ]
 fight = attack_counter()
[ ]
 type(fight)
 function
[ ]
 fight("kimura")
 Upper Body Attacks 1, Lower Body Attacks 0
[ ]
 fight("knee_bar")
 Upper Body Attacks 1, Lower Body Attacks 1
[ ]
 fight("keylock")
 Upper Body Attacks 2, Lower Body Attacks 1
Partial Functions

Useful to partial assign default values to functions
[ ]
 from functools import partial

def multiple_attacks(attack_one, attack_two):
  """Performs two attacks"""
  
  print(f"First Attack {attack_one}")
  print(f"Second Attack {attack_two}")
  
attack_this = partial(multiple_attacks, "kimura")
type(attack_this)
 functools.partial
By using this partial function, only one argument is needed
[ ]
 attack_this("knee-bar")
 First Attack kimura
Second Attack knee-bar
Alternately, the original function can also be called with a different two attacks
[ ]
 multiple_attacks("Darce Choke", "Bicep Slicer")
 First Attack Darce Choke
Second Attack Bicep Slicer
Lazy Evaluated Functions (Generators)

A very useful style of programming is "lazy evaluation". A generator is an example of that. Generators yield an items at a time.
The example below return an "infinite" random sequence of attacks. The lazy portion comes into play in that while there is an infinite amount of values, they are only returned when the function is called.
[ ]
 def lazy_return_random_attacks():
    """Yield attacks each time"""
    import random
    attacks = {"kimura": "upper_body",
           "straight_ankle_lock":"lower_body", 
           "arm_triangle":"upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body"}
    while True:
        random_attack = random.choices(list(attacks.keys()))
        yield random_attack
[ ]
 attack = lazy_return_random_attacks()
[ ]
 type(attack)
 generator
[ ]
 for _ in range(6):
    print(next(attack))
 ['knee_bar']
['straight_ankle_lock']
['arm_triangle']
['keylock']
['knee_bar']
['knee_bar']
Decorators: Functions that wrap other functions

Randomized Sleep Decorator

Another useful technique in Python is to use the decorator syntax to wrap one function with another function. In the example below, a decorator is written that adds random sleep to each function call. When combined with the previous "infinite" attack generator, it generates random sleeps between each function call.
[ ]
 def randomized_speed_attack_decorator(function):
    """Randomizes the speed of attacks"""
    
    import time
    import random
    
    def wrapper_func(*args, **kwargs):
        sleep_time = random.randint(0,3)
        print(f"Attacking after {sleep_time} seconds")
        time.sleep(sleep_time)
        return function(*args, **kwargs)
    return wrapper_func
[ ]
 @randomized_speed_attack_decorator
def lazy_return_random_attacks():
    """Yield attacks each time"""
    import random
    attacks = {"kimura": "upper_body",
           "straight_ankle_lock":"lower_body", 
           "arm_triangle":"upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body"}
    while True:
        random_attack = random.choices(list(attacks.keys()))
        yield random_attack
[ ]
 for _ in range(5):
    print(next(lazy_return_random_attacks()))
 Attacking after 1 seconds
['keylock']
Attacking after 0 seconds
['knee_bar']
Attacking after 1 seconds
['keylock']
Attacking after 2 seconds
['straight_ankle_lock']
Attacking after 0 seconds
['arm_triangle']
Timing Decorator

Using a decorator to time code is very common
[ ]
 from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"fun: {f.__name__}, args: [{args}, {kw}] took: {te-ts} sec")
        return result
    return wrap
Using decorator to time execution of a function
[ ]
 @timing
def some_attacks(foo):
  print(f"this was passed in: {foo}")
  attack = lazy_return_random_attacks()
  for _ in range(5):
    print(next(attack))
    
some_attacks("bar")
  
 this was passed in: bar
Attacking after 0 seconds
['arm_triangle']
['straight_ankle_lock']
['straight_ankle_lock']
['arm_triangle']
['straight_ankle_lock']
fun: some_attacks, args: [('bar',), {}] took: 0.0008716583251953125 sec
Making Classes Behave Like Functions

Creating callable functions
[ ]
 class AttackFinder:
  """Finds the attack location"""
  
  
  def __init__(self, attack):
    self.attack = attack
  
  def __call__(self):
    attacks = {"kimura": "upper_body",
           "straight_ankle_lock":"lower_body", 
           "arm_triangle":"upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body"}
    if not self.attack in attacks:
      return "unknown location"
    return attacks[self.attack]
    
[ ]
 my_attack = AttackFinder("kimura")
my_attack()
 
Applying Functions to Pandas DataFrames

The final lesson on functions is to take this knowledge and use it on a DataFrame in Pandas. One of the more fundamental concepts in Pandas is use apply on a column vs iterating through all of the values. An example is shown below where all of the numbers are rounded to a whole digit.
[ ]
↳ 12 cells hidden
Writing Lambdas

Generally considered to be unnecessary. A Python lambda is an inline python and it can often lead to confusing code.
[ ]
↳ 9 cells hidden
Exercise: Write a function that returns infinite values

[ ]
 def forever():
    while True:
        yield 1

[ ]
 res = forever()
type(res)
 generator
[ ]
 next(res)
 1
[ ]
 #Finite
def not_forever():
    vars = [1,2,3,5]
    for var in vars:
        yield var

[ ]
 res2 = not_forever()
[ ]
 next(res2)
 
Exercise: Capture the output of a shell command using the ! operator and parse with SList grep

[ ]
 !ls -l
 total 4
drwxr-xr-x 1 root root 4096 Oct  5 16:31 sample_data
[ ]
 directory_listing = !ls -l
type(directory_listing)
 IPython.utils.text.SList
[ ]
 directory_listing.grep("data")
 ['drwxr-xr-x 1 root root 4096 Oct  5 16:31 sample_data']
Automating Text and Filesystem
Presentation: Reading, Writing and Using files: TXT, CSV, and YAML

Writing to a file

*Watch Video Lesson 6.1: Use write file operations*
[ ]
 f = open('workfile.txt', 'w')
f.write("foo20\n")
f.write("foo3\n")
f.write("foo4\n")
f.close()
!cat workfile.txt

#!ls -l
 foo20
foo3
foo4
[ ]
 my_writes = ["foo2\n","foo3\n","foo4\n"]
f = open('workfile2.txt', 'w')
for line in my_writes:
  f.write(line)
f.close()
!cat workfile2.txt
 foo2
foo3
foo4
Writing to a file with 'context'

[ ]
 with open("workfile.txt", "w") as workfile:
    workfile.write("bam")
!cat workfile.txt
 bam
Reading a file in

*Watch Video Lesson 6.2: Use read file operations*
[ ]
 f = open("workfile.txt", "r")
out = f.readlines() #r.read() works as well
# Maybe we want to create a generator pipeline
for line in out:
  print(line)
  #  yield line
f.close()
print(out)
 bam
['bam']
Reading a file with 'context'

[ ]
 with open("workfile.txt", "r") as workfile:
    print(workfile.readlines())
    #print(workfile.read())

 ['bam']
Double-click (or enter) to edit
Serialize a Python Dictionary to Pickle

[ ]
 mydict = {"one":1, "two":2}
[ ]
 import pickle
[ ]
 pickle.dump(mydict, open('mydictionary.pickle', 'wb'))
[ ]
 !ls -l mydictionary.pickle
 -rw-r--r-- 1 root root 32 Aug  9 13:19 mydictionary.pickle
[ ]
 #!cat mydictionary.pickle
[ ]
 res = pickle.load(open('mydictionary.pickle', "rb"))
[ ]
 print(res)
 {'one': 1, 'two': 2}
Serialize a Python Dictionary to JSON

[ ]
 import json
with open('data.json', 'w') as outfile:
    json.dump(res, outfile)
[ ]
 !cat data.json
 {"one": 1, "two": 2}
[ ]
 with open('data.json', 'rb') as outfile:
    res2 = json.load(outfile)
[ ]
 print(res2)
type(res2)
 {'one': 1, 'two': 2}
dict
Save to Yaml

[ ]
 import yaml
[ ]
 with open("data.yaml", "w") as yamlfile:                                               
    yaml.safe_dump(res2, yamlfile, default_flow_style=False)
[ ]
 !cat data.yaml
 one: 1
two: 2
Load Yaml

[ ]
 with open("data.yaml", "rb") as yamlfile:                                               
    res3 = yaml.safe_load(yamlfile) 
[ ]
 print(res3)
type(res3)
 {'one': 1, 'two': 2}
dict
TO DO Protobuff Example

Double-click (or enter) to edit
Exercise: Read and Write a YAML file

[ ]
↳ 9 cells hidden
Presentation: Managing files and directories using os.path and pathlib

[ ]
 # Make some dirs
import pathlib
import os

path = "somedir"
#Depending on the script you are writing maybe you want this False
pathlib.Path(path).mkdir(parents=True, exist_ok=True)
[ ]
 ls -la somedir
 total 8
drwxr-xr-x 2 root root 4096 Aug  9 13:22 ./
drwxr-xr-x 1 root root 4096 Aug  9 13:22 ../
[ ]
 import pathlib
pathvar = pathlib.Path("newdir")
pathvar2 = pathlib.Path("somedir")
Check if path exists?
[ ]
 pathvar.exists()
 False
[ ]
 pathvar2.exists()
 True
[ ]
 pathvar.write_text("foo")
 3
[ ]
 cat newdir
 foo
Exercise: Use pathlib to rename files

Double-click (or enter) to edit
[ ]
 from pathlib import Path
p = Path('foo.txt')
p.open('w').write('bam')

#This file is created
print("Before rename")
!ls -l *.txt

out = Path('bar.txt')
p.rename(out)

#It is renamed
print("After rename")
!ls -l *.txt
!rm bar.txt
 Before rename
-rw-r--r-- 1 root root  3 Aug  9 13:24 foo.txt
-rw-r--r-- 1 root root 15 Aug  9 13:18 workfile2.txt
-rw-r--r-- 1 root root  3 Aug  9 13:19 workfile.txt
After rename
-rw-r--r-- 1 root root  3 Aug  9 13:24 bar.txt
-rw-r--r-- 1 root root 15 Aug  9 13:18 workfile2.txt
-rw-r--r-- 1 root root  3 Aug  9 13:19 workfile.txt
Fnmatch
import fnmatch

files = ["data1.csv", "script.py", "image.png", "data2.csv", "all.py"]


def csv_matches(files):
    """Return matches for csv files"""

    matches = fnmatch.filter(files, "*.csv")
    return matches


# Print matches to pattern
print(f"Found matches: {csv_matches(files)}")
Archive?
from shutil import make_archive
import os

username = "user1"
root_dir = "/tmp"
# archive path
path = f"{root_dir}/{username}"

# create tar and gzipped archive
make_archive(username, "gztar", root_dir)

# create zip archive
make_archive(username, "zip", root_dir)

print(os.listdir("/tmp"))
Presentation: Walking directory trees using os.walk

Example from standard library docs...but lets change.
import os
from os.path import join, getsize
for root, dirs, files in os.walk('somedir'):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
These are the hooks to walk the file system...
[ ]
 import os
from os.path import join, getsize
for root, dirs, files in os.walk('sample_data'):
    print(f"files I found: {files}")
    #full path
    for name in files:
        full_path = join(root, name)
        print(f"full path to files: {full_path}")
 files I found: ['anscombe.json', 'README.md', 'california_housing_train.csv', 'mnist_train_small.csv', 'mnist_test.csv', 'california_housing_test.csv']
full path to files: sample_data/anscombe.json
full path to files: sample_data/README.md
full path to files: sample_data/california_housing_train.csv
full path to files: sample_data/mnist_train_small.csv
full path to files: sample_data/mnist_test.csv
full path to files: sample_data/california_housing_test.csv
Presentation: Getting stat information on files and directories

Double-click (or enter) to edit
[ ]
 import os
location = "sample_data/anscombe.json"
result = os.stat(location)
[ ]
 result.st_gid
 0
[ ]
 result
 os.stat_result(st_mode=33261, st_ino=3670050, st_dev=40, st_nlink=1, st_uid=0, st_gid=0, st_size=1697, st_atime=946713600, st_mtime=946713600, st_ctime=1659706701)
Subprocess.run

↳ 1 cell hidden
Example health check

import subprocess
import os

# setup
file_location = "/tmp/file.txt"
expected_uid = 501
# touch a file
proc = subprocess.Popen(["touch", file_location])

# check user permissions
stat = os.stat(file_location)
Presentation: Finding files: duplicates, globbing, and patterns

subprocess find

import subprocess

print("Enter a path to search for directories: \n")
user_input = input()
print(f"user_input: {user_input}")
with subprocess.Popen(
    ["find", user_input, "-type", "d"], stdout=subprocess.PIPE
) as find:
    result = find.stdout.readlines()
    for line in result:
        print(f"Found Directory: {line}")
[ ]
 !touch foo.csv && touch bar.txt
import glob
glob.glob("*.csv")
 ['foo.csv']
Exercise: Find files using glob

Double-click (or enter) to edit
[ ]
 path = "sample_data"
results = glob.glob(f"{path}/*.csv")

#how many many CSV did you find?
print(len(results))
results
 4
['sample_data/california_housing_train.csv',
 'sample_data/mnist_train_small.csv',
 'sample_data/mnist_test.csv',
 'sample_data/california_housing_test.csv']
[ ]
 path = "sample_data"
results = glob.glob(f"{path}/*.json")

#how many many CSV did you find?
print(len(results))
results
 1
['sample_data/anscombe.json']
Developing with the Command Line
Presentation: Setting up a Python project with VSCode and pip

Double-click (or enter) to edit
Presentation: Using sys.argv

Double-click (or enter) to edit
Exercise: Write a command-line tool with sys.argv

Double-click (or enter) to edit
Presentation: Using click CLI Framework

Write a command-line tool with click

Reference: https://click.palletsprojects.com/en/5.x/quickstart/
[ ]
%%writefile hello-click.pyimport click@click.command()def hello():    click.echo('Hello World!')if __name__ == '__main__':    hello()

 Writing hello-click.py
[ ]
!python hello-click.py

 Hello World!
Presentation: click, subprocess.run, and mixing shell and Python together

Double-click (or enter) to edit
