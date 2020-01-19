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
run_while_loops = True

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
    
# this is what happens if no modules are set to true
else:
    print("Please select a module to work on")
