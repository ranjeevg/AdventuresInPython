# import statements import libraries, just like in Java

# import math - this imports the entire math module
from math import *  # this imports the functions to the scope

# assigning a variable
a = "Hello"
# apparently you don't need to use a declarative word here
# ah, well, let's forge on
b = "Hi"
c = "macha, whyy you ignoring da"
d = "ok tata bye bye"
new_line = "\n"

# setting booleans to control which parts of the program run

run_string = False
run_math = False
run_user_input = False
run_lists = False
run_tuples = False
run_dictionaries = False
run_while_loops = False
run_for_loops = False
run_functions = False
run_2D_arrays = False
run_try_except = False
run_io = False
run_classes = True

# using if, elif and else statements to control the flow of the program

if run_string:
    # printing the strings that we stored to the variables

    print(a)
    print(b)
    print(c)
    print(d)

    # playing around with string methods

    print(new_line + a.upper() + new_line + b.upper() + new_line + c.upper() + new_line + d.upper() + new_line)
    total_string = new_line + a.upper() + new_line + b.upper() + new_line + c.upper() + new_line + d.upper() + new_line
    print(total_string + "PO DA PATTI MYRE" + new_line)  # because why not

# this branch of the program deals with the math library
elif run_math:
    a = 10
    b = 15
    c = pi
    d = radians(180)

    print("the hypotenuse of a right triangle with legs of " + str(a) + " and " + str(b) + " is " + str(hypot(a, b)))
    print(new_line)
    if c == d:
        print("Pi radians is isomorphic to 180 degrees")
    else:
        print("Experiment fail")

# this section plays around with user input
elif run_user_input:
    # this was alarmingly easy
    user_input = input("Enter anything here: ")
    print(new_line + "This is what you entered: " + user_input)

# this section deals with lists and stuff
elif run_lists:
    initial_list = [a, b, c, d]
    print(initial_list[3])
    print(new_line)

    # apparently you can mix and match data types
    mixed_list = [a, b, c, run_lists, pi, cos(pi)]
    # a foreach loop
    for x in mixed_list:
        print(x)
        print(new_line)
    # creating a new list, we're going to concatenate lists, and other fun stuff
    norwegian_black_metal_keywords = ["Fantoft", "Helvete", "Grischnakh", "tremolo", "neo-paganism"]
    # 'extend' adds on to lists, even concatenating a new list on to it
    mixed_list.extend(norwegian_black_metal_keywords)
    # a foreach loop to demonstrate the modified list
    print(new_line + "############### Modified List ###############   " + new_line + new_line)
    for x in mixed_list:
        print(x)
        print(new_line)
    # append pushes a single entry to the end of the list
    mixed_list.append(666)
    # a foreach loop to demonstrate the modified list
    print(new_line + "############### New Modified List ###############   " + new_line + new_line)
    for x in mixed_list:
        print(x)
        print(new_line)
    # insert pushes an item into a specified index, bumping all following indices by 1
    mixed_list.insert(1, "RIP SLAYER \\m/")
    # a foreach loop to demonstrate the modified list
    print(new_line + "############### New Modified List ###############   " + new_line + new_line)
    for x in mixed_list:
        print(x)
        print(new_line)
    # remove removes the entry matching the specified value
    mixed_list.remove("RIP SLAYER \\m/")
    # a foreach loop to demonstrate the modified list
    print(new_line + "############### New Modified List ###############   " + new_line + new_line)
    for x in mixed_list:
        print(x)
        print(new_line)
    # pop removes the last entry, or can remove an entry at a specified index
    mixed_list.pop()
    # a foreach loop to demonstrate the modified list
    print(new_line + "############### New Modified List ###############   " + new_line + new_line)
    for x in mixed_list:
        print(x)
        print(new_line)
    mixed_list.pop(1)
    # a foreach loop to demonstrate the modified list
    print(new_line + "############### New Modified List ###############   " + new_line + new_line)
    for x in mixed_list:
        print(x)
        print(new_line)
    # you can also find the index of a certain entry
    print("########################################################################################")
    print(mixed_list.index("neo-paganism"))
    print("########################################################################################")
    print(new_line)
    # count displays how many times an entry appears in a list
    print("########################################################################################")
    print(mixed_list.count("neo-paganism"))
    print("########################################################################################")
    print(new_line)
    # clear resets the list to empty
    mixed_list.clear()
    # a foreach loop to demonstrate the modified list
    print(new_line + "############### New Modified List ###############   " + new_line + new_line)
    for x in mixed_list:
        print(x)
        print(new_line)

# this module explores tuples
# note - tuples are immutable, i.e. you can't change their values once assigned
elif run_tuples:
    x = input("please enter the x-coordinate of your point: ")
    y = input("please enter the y-coordinate of your point: ")
    coordinates = (x, y)  # apparently, we use parentheses instead of square brackets for tuples
    print(new_line)
    for z in coordinates:
        print(z)

# this module explores dictionaries
# apparently we use curly brackets for dictionaries in Python.
# recap: parentheses for tuples, square brackets for lists
# note - key-value pairing here; the key is the first entry, which matches to the value next to it
# furthermore, the keys need to be unique, in order to prevent potential mishaps with a key
#     having different values. I'm quite sure Python throws an exception anyway.
elif run_dictionaries:
    sample_dictionary = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"
    }
    # this is one method to access elements in a dictionary - reference the key directly
    print(sample_dictionary["Jan"])
    # we could also use the get method, as such:
    print(sample_dictionary.get("Oct"))
    # keep in mind that you reference the key, not the value
    # the get method is also overloaded so that you can specify a message if the key doesn't match
    #   with any values in the dictionary
    print(sample_dictionary.get("SATAN", "Entry not found"))
    # here, there's no entry with a key of "SATAN", so it returns "Entry not found"

# this is fairly straightforward - while loops
elif run_while_loops:
    i = 1
    while i < 10:
        print(i)
        i += 1
    print("Our loop's done, thanks :)")

# so there are some things that I didn't know about for loops
elif run_for_loops:
    # this is a way to use the foreach syntax to cover a predetermined range of numbers
    for index in range(10):
        # the range method returns a list of all whole numbers below the number inserted.
        # as such, range(10) returns a list of the numbers 0 through 9.
        print(index)
    print("For loop done, guys")
    print(new_line)

    # another application of the range method is to specify a starting number
    # for example, range(2, 10) returns the numbers 2 through 9
    for index in range(1,10):
        print(index)
    print("Modified-range for loop done, guys")

# so I missed a section about functions, working on that here
elif run_functions:
    # 'def function_name(arguments):
    def first_python_function():
        print("Hello Python Function Space!" + new_line)
        for index2 in range(1, 16):
            print(str(index2) + new_line)
        return("Bahut bahut dhanyavaad")

    # ok, so we've defined a function. Calling it is fairly easy:
    print(first_python_function())

# this section explores 2D arrays in Python
elif run_2D_arrays:
    # let's use a this 2D array to define a 3x3 invertible matrix
    two_dim_array = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 1]
    ]
    # python, unlike Xamarin, thankfully, indexes rows first and then columns
    # also, nested loops
    # this prints out the matrix that we printed before, in Octave format
    for j in range(3):
        row = "["
        for k in range(3):
            row += str(two_dim_array[j][k])
            if k < 2:
                row += ", "
            elif k == 2:
                row += "]"
                if j != 2:
                    row += ","
                print(row)

# try / except statements - essentially try/catch by another name
elif run_try_except:
    try:
        print(int(input("Enter a number here: ")))
    except:
        print("Invalid input")
    # this inevitably happens at the end, after either the try or except conditions have been met
    finally:
        print("This is the final step")

    # a try-except statement with specified conditions to check for
    #   here, we have a type-conversion error in the try statement that we allow to run, but it catches a
    #   divide-by-zero
    try:
        value = int(10 / (0.001 - 0.001))
        print(value)
        print(int(input("Enter another value here: ")))
    except ZeroDivisionError as err:
        print(err)

# playing around with I/O
elif run_io:
    try:
        # open opens the file. the second argument specifies the file open type
        file_contents = open("helloWorld.txt", "r+")
        # "r" stands for 'read', "w" stands for 'write', "a" stands for 'append',
        #    "r+" stands for 'read and write'

        # now, we want to check if the file is readable - the .readable method returns a bool accordingly
        print("File readable? : " + str(file_contents.readable()))

        # reaading the lines and adding them to a list
        line_list = file_contents.readlines()
        print(line_list)

        # reading a single line, moving the cursor to the next line
        print(file_contents.readline())

        # now, we want to actually read the file
        print(file_contents.read())

        # writing to the file
        file_contents.write("Ave Lucifer\n")

        # of course, we want to close the file when we're done
        file_contents.close()
        print("File read successfully")

        # creating a new file programmatically - do not use r+, as it tries to read the file before
        #    it's been created
        html_example = open("example.html", "w")
        html_example.write("<p>This is an HTML file</p>")
        html_example.close()

    # in the case that the file doesn't exist
    except FileNotFoundError as err:
        print(err)

# this section deals with classes
elif run_classes:
    # note: classes are best defined in their own separate files and then imported, but, for the sake of this
    #   exercise, I'm going to define a class in this file
    # we would import them as such: from <filename> import <class>
    class TestClass:
        # this next function is a constructor, called __init__. 2 underscores, mind you.
        # also, you need to specify the self argument here.
        def __init__(self, name, favorite_food):
            self.name = name
            self.favorite_food = favorite_food

    # creating an object of the TestClass class
    Object = TestClass("Ranjeev Grewal", "Mutton biryani")
    print(Object.name + ", " + Object.favorite_food)

    # you declare that a class inherits from another in the following syntax:
    # class ChildClass(ParentClass): # etc.
    class FirstInheritedClass(TestClass):
        def this_is_a_method(self):
            try:
                return self.name
            except Exception as err2:
                print(err2)

    # instantiating a FirstInheritedClass object
    first_inherited_object = FirstInheritedClass("Ranjeev", "Biryani")
    print(first_inherited_object.this_is_a_method())

# this is what happens if no booleans that control the program flow are set to true
else:
    print("Please select a section of the code to work on by changing the appropriate booleans, starting at line "
          + "17 of the program.")
