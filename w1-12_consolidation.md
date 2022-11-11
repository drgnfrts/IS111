# IS111 Consolidation (Week 1 to 12)

- [IS111 Consolidation (Week 1 to 12)](#is111-consolidation-week-1-to-12)
  - [Variables](#variables)
  - [Operators](#operators)
    - [Precedence Table](#precedence-table)
    - [Logic Table & De Morgan's Law](#logic-table--de-morgans-law)
    - [Truthy & Falsy Values](#truthy--falsy-values)
  - [Functions](#functions)
  - [Conditionals](#conditionals)
  - [Tuples](#tuples)
  - [Strings](#strings)
  - [For Loops](#for-loops)
  - [Lists](#lists)
  - [While Loops](#while-loops)
  - [File Handling](#file-handling)
  - [Dictionaries](#dictionaries)
  - [Other Useful Functions](#other-useful-functions)
- [Algorithms](#algorithms)
  - [W1: Currency Seperation / Time Division [*]](#w1-currency-seperation--time-division-)
  - [W2: Pattern Printing [*]](#w2-pattern-printing-)
  - [W2: Tax Question, No Conditionals [**]](#w2-tax-question-no-conditionals-)
  - [W3: De Morgan's Law & Evaluating T/F Statements [*]](#w3-de-morgans-law--evaluating-tf-statements-)
  - [W3: Taxi Fare Flagdown [**]](#w3-taxi-fare-flagdown-)
  - [W4: Pyramid Question [*]](#w4-pyramid-question-)
  - [W4: Check for Minimums / Data Plan Question [**]](#w4-check-for-minimums--data-plan-question-)
  - [W4: Check For Characters / Password Strength [***]](#w4-check-for-characters--password-strength-)
  - [W4: Print Fibonacci without Recursion [***]](#w4-print-fibonacci-without-recursion-)
  - [W5: Tax Question, with Conditonals [*]](#w5-tax-question-with-conditonals-)
  - [W5: Checking For Primes [**]](#w5-checking-for-primes-)
  - [W5: Finding Non Common Elements [**]](#w5-finding-non-common-elements-)
  - [21LT1: List Index Swapping 1 / Teammate Swap [***]](#21lt1-list-index-swapping-1--teammate-swap-)
  - [21LT1: Permutation Handling 1 / Puzzle Solving [***]](#21lt1-permutation-handling-1--puzzle-solving-)
  - [20LT1: Getting Minimums with Conditionals [**]](#20lt1-getting-minimums-with-conditionals-)
    - [Getting Maximums with Conditionals [**]](#getting-maximums-with-conditionals-)
    - [Getting Middle Number with Conditionals [**]](#getting-middle-number-with-conditionals-)
  - [20LT1: Checking Equations [***]](#20lt1-checking-equations-)
  - [20LT1: Implicit While Loop / Contact Tracing [***]](#20lt1-implicit-while-loop--contact-tracing-)
  - [19LT1: Check Seating Arrangement [***]](#19lt1-check-seating-arrangement-)
    - [Permutation Handling 2 [***]](#permutation-handling-2-)
  - [19LT1: List Index Swapping 2 / String Transformation [***]](#19lt1-list-index-swapping-2--string-transformation-)
  - [W7: Pangram [**]](#w7-pangram-)
  - [W7: Diamond Printing [***]](#w7-diamond-printing-)
  - [W7: Sublist Flattening [***]](#w7-sublist-flattening-)
  - [W9: Get Strings with Digits w Min Overall Digit Count [***]](#w9-get-strings-with-digits-w-min-overall-digit-count-)
  - [W9: Merge Lists by Number, Ascending Order [***]](#w9-merge-lists-by-number-ascending-order-)
  - [W9: Group Numbers With Minimum Total [***]](#w9-group-numbers-with-minimum-total-)
  - [W9: Check if Strings have Same Characters [**]](#w9-check-if-strings-have-same-characters-)
  - [W9: Line Up Question [***]](#w9-line-up-question-)
  - [W10: Sort by Subject and Find Classmates [***]](#w10-sort-by-subject-and-find-classmates-)
  - [W10: Matrix Transpose [**]](#w10-matrix-transpose-)
  - [W10: Docstring Finding [***]](#w10-docstring-finding-)
  - [W10: Scramble Words Keep Punctuation/First/Last Letter [****]](#w10-scramble-words-keep-punctuationfirstlast-letter-)
  - [W11: Degrees of Separation [***]](#w11-degrees-of-separation-)
  - [W11: Nested Dictionaries [**]](#w11-nested-dictionaries-)
  - [W12: Due Date Scheduling [***]](#w12-due-date-scheduling-)
  - [MLT2: Separate Numbers & Calculate Averages [***]](#mlt2-separate-numbers--calculate-averages-)

## Variables

- Variables are names that refer to a value
- Variables cannot start with digits
- Variable types can be reassigned since Python is dynamically typed
- For lists, as seen below,

        var_a = [1, 2, 3]
        var_b = var_a
        # there will still only be one list in memory

## Operators

### Precedence Table

| Precedence | Operators            | Notes                                                                |
| ---------- | -------------------- | -------------------------------------------------------------------- |
| 1          | \*\*                 | Exponents are read from RHS. 2 ** 3 ** 2 is $2^{3^2}$, not $(2^3)^2$ |
| 2          | \*                   | Strings, Tuples and Lists can use this operator. See code block      |
| =          | \\                   | Will always return a float                                           |
| =          | \\\                  | Floor Division will give the quotient. Integers not affected         |
| =          | %                    | Modulo will give the remainder. Integers not affected                |
| 3          | +                    | Strings, Tuples and Lists can use this operator                      |
| =          | -                    |                                                                      |
| 4          | ==, !=, <, <=, >=, > | Relational Operators                                                 |
| 5          | not                  |                                                                      |
| 6          | and                  |                                                                      |
| 7          | or                   |                                                                      |

        "12" * 2 returns "1212"
        [1, 2] * 2 returns [1, 2, 1, 2]
        (1, 2) * 2 returns (1, 2, 1, 2)

### Logic Table & De Morgan's Law

| A     | B     | A and B | A or B |
| ----- | ----- | ------- | ------ |
| False | False | False   | False  |
| False | True  | False   | True   |
| True  | False | False   | True   |
| True  | True  | True    | True   |

De Morgan's Law states that:

- not (A and B) = (not A or not B)
- not (A or B) = (not A and not B)

### Truthy & Falsy Values

Falsy values return False and Truthy values return True upon being conditionally evaluated. Falsy Values include:

- Empty lists, tuples, strings, ranges
- Zero of any numeric type
- None
- False

Note: int(True) = 1 and int(False) = 0

## Functions

- Check question to see if Print or Return is the better one to use. Else, default to Return
- Once parameters are inputted with keyword arguments, cannot use positional arguments

        def powerpuff(sugar, everything_nice = 3, spice): -> this will not work
            pass -> pass does nothing btw

## Conditionals

- Operator Precedence, Truth Table and De Morgan's Law meeds to be memorised
- When to use if/else vs only if:

  - Code block below will print "b" then "c" if conditional is true, else only "c" is printed

        if a == 0:
            print("b")
        print("c")

  - Code block below will only print either "b" or "c"

        if a == 0:
            print("b")
        else:
            print("c")

## Tuples

- Immutable sequence of values, called with tuple_a[index]
- Values from tuples can be "taken out" as such, useful for iterations

        tuple_a = ("IS111", ("Dragonboat", "Smart City Society"))
        current_mod, cca_tuple = tuple_a

- Certain ways to generate tuples:

        tuple_b = "abcd"  -> ("abcd")
        tuple_c = tuple("abcd") OR tuple("abcd",) -> ("a", "b", "c", "d")
        tuple_d = tuple("ab, cd") -> ("a", "b", " ", ",", "c", "d")
        not_tuple = ("abcd") -> returns string "abcd"

- Two tuples can be concat-ed together. Convert a singular string/int to a tuple with , then you can concat the "new tuple" to the main one

## Strings

- String indexes begin from 0 on the LHS, and -1 on RHS
- Take note of the following string slicing sequence [start index : end_index (exclusive) : step]

        str = [1, 2, 3, 4, 5, 6]
        print(str[:2]) -> returns [1, 2], the last index printed i = 1 is 2
        print(str[-1::-1]) -> returns [6, 5, 4, 3, 2, 1]
        print(str[1::2]) -> returns [2, 4, 6] at indexes 1, 3, 5

        .upper() -> returns all uppercase
        .lower() -> returns all lowercase
        .find(substr) -> finds the lowest index in string where substring is found
        .rfind(substr) -> searches from right, but returns the positive index
        .split(sep) -> splits into list by sep, default sep is " "
        "sep".join(list) -> joins list into a string with sep between them
        .replace(original, replacement) -> replaces all characters in string matching original with replacement
        .strip(ch) -> strips away instances of ch at the front and end of string
        a_list[:0] = a_string -> turns string into list

- Any iteration through a string will return individual characters

## For Loops

- range() takes in a number only and uses , as seperator, NOT :

        for i in range(start, end(exclusive, step)):
                -> this iterates from start to end - 1

        for answer in list_of_answers:
                -> iterates through list_of_answers, including any modifications to the list halfway thru the iteration

- 2 major functions that greatly impact the loop:

        break -> breaks out of the nearest/innermost for loop
        continue -> skips the current iteration and move on to the next iteration in the for loop

## Lists

- slice operator uses : and can only be used for lists

        n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(n_list[0:9:3]) -> returns [1, 4, 7]

- Note the way list are stored and memory

        var_a = [1, 2, 3]
        var_b = var_a
        # there will still only be one list in memory

- Global lists can be accessed and modified locally in functions even without a return statement.

        a_list = [4, 5, 6]
        def do_something(my_list):
                my_list[0] = 5
                my_list[1] = 6
                my_list[2] = 7
        print(a_list) -> returns [5, 6, 7]

- If you completely reassign a list in the function, the first list will stay in memory and not be modified, and a second list will be created.

        a_list = [5, 6, 7]
        def do_something_2(my_list):
                my_list = [7, 8, 9]

        do_something_2(a_list)
        print(a_list) -> still is [5, 6, 7]

- Operators inside the append function will execute first before append is executed

        def do_trick(a_list):
            a_list.append(a_list[1:3] + [a_list[3]])

        my_list = ['a', 'b', 'c', 'd']
        do_trick(my_list)
        print(my_list) -> result is [a, b, c, d, [b, c, d]] -> + operation is completed before appending, thus appending a pre-existing list [b, c, d] to my_list (modify global list)

- Never use "list" as a variable. Otherwise the list() method will break
- Note the following list modification functions. Do not assign them to variables as their return value is None.

        list1.append() -> appends to back
        list1.remove() -> removes first instance of item
        list1.pop() -> removes item at that index
        list1.insert() -> inserts item at that index
        list1.count() -> counts number of elements

- Note the list() method will make every element in the string an element in the list. It may be preferable to use .split()

## While Loops

- Two major types of While Loops used for IS111: While True and While Conditional
  - While True loops more useful when starting question is the exact same as the repeated questions, but requires explicit breaking
  - While Conditionals will auto-break if the Conditional has been met at the end of the loop
- May be more intuitive to identify what conditional will break the loop, and put While Not Conditional

        while (num < 2 or num > 100 or num % 2 != 0 ): -> may be less intuitive than:
        while (not (num >= 2 and num <= 100 and num % 2 == 0 )):

- Make extensive use of breaks and continues
- While Loops are generally more useful than For Loops if you want to keep jumping around a list rather than iterating through them. You will probably need an index variable to keep track of how many times you've run through the list/loop.

## File Handling

- Ensure you are in the correct directory when running the program. Otherwise your links will break.
  - Use cd filename to go into a folder and cd ../ to move up one folder (Windows OS)
- The primary command for file handling is:

        with open(filename, "#") as newfile:

  - with # being replaced with:
    - r for read
    - w for write
    - a for append

- To write to a file after it has been opened, use:

        newfile.write(whatever content)

- Minimise the number of times the file is opened. Never put the open function into a while loop
- txt files will usually have "\n" at the end of each line. You will need to use .strip("\n") to remove it
- Questions relating to file handling often require you to split by "\t" or other seperators
- Can open input file and output file at the same time, separated by comma
- After iterating through the file, the cursor will be at the bottom of the file and you will need to re-open and re-iterate through the file

## Dictionaries

- Call or assign the value of a dictionary key:value pair with dict[my_key]
- if x in dict will only work if x is a key
- Dictionaries can be modified from within the function, similar to lists
- Any immutable value can be a key, including tuples
- Hash function lookup used by dictionaries enables lookup time to be constant
- Useful calls:

        dict.items() -> calls all items
        dict.keys() -> calls all keys
        dict.values() -> calls all values
        sort = sorted(new_dict.items(), key=lambda x: x[1], reverse=True) -> to sort a dictionary by numerical keys

- A list of tuples can be converted to a dictionary with dict()

## Other Useful Functions

        input() -> returns a string
        print(i, end=' ') -> prints i and ends with a space instead of new line
        round(element, demical_places)
        random.randint(a, b) -> gives an integer exclusive of b [a, b)
        random.randrange(a, b) -> gives an integer inclusive of b [a, b]
        max(iterables), min(iterables) -> returns the max or min of iterables
        float("inf") and -float("inf") as proxies for infinity and negative infinity
        set(list1).union(set(list2)) -> outputs the union of two sets, returns a set
        set(list1).intersection(set(list2)) -> outputs the intersection between two sets, returns a set

        string.ascii_lowercase , string.ascii_uppercase and string.digits (all without paranthesis) -> gives you a string of all lowercase, uppercase letters and digits respectively

# Algorithms

## W1: Currency Seperation / Time Division [*]

1.  Floor divide largest demonination
2.  For subsequent denominations, modulo the previous denomination's "positions", and floor divide the denomination only at the end
3.  See ICE1 Q6, Lab 1 Q6

        time_in_seconds = int(input("Enter time in seconds:"))
        hours = time_in_seconds // 3600
        minutes = time_in_seconds % 3600 // 60
        seconds = time_in_seconds % 60

        # minutes may overrun if you use time_in_seconds // 60 % 60. get the hours out of the way first, then floor divide (quotient) by 60

## W2: Pattern Printing [*]

1.  Identify pattern - keyword and seperator
2.  Run Lab 2 Q3 to see output

        def print_pattern(my_str, delimiter_str, n):
            print(my_str, end='')
            for i in range(n-1):
                print(delimiter_str, end='')
                print(my_str, end='')
            print()

## W2: Tax Question, No Conditionals [**]

1.  For each tax bracket, check if income manages to "reach" the bracket by taking the max(income - bracket_amount, 0)
2.  Apply the increase in percentage of tax liable for (income - bracket_amount)
3.  See ICE2 Q8 for more details

        def calculate_all_tax_brackets(income):
            rate_20k = max(income - 20000, 0) * 0.02
            additional_rate_30k = max(income - 30000, 0) * 0.015
            additional_rate_40k = max(income - 40000, 0) * 0.035
            additional_rate_80k = max(income - 80000, 0) * 0.045
            tax = rate_20k + additional_rate_30k + additional_rate_40k + additional_rate_80k
            return tax

## W3: De Morgan's Law & Evaluating T/F Statements [*]

1.  Slowly evaluate the statement, don't rush through it!

                not ( not ( a and not b ) or ( b or not a ) )
                = not(not(( a and not b ))) and not(b or not a)
                = a and not b and not b and a
                = a and not b

## W3: Taxi Fare Flagdown [**]

| Charge Type            | value |
| ---------------------- | ----- |
| First 1km              | a     |
| Next 400m, up to 9.8km | b     |
| Next 350m beyond 9.8km | c     |
| Peak Surcharge         | 25%   |
| Midnight Surcharge     | 50%   |
| Location Surcharge     | d     |

Base Fare = a + (no. of intervals) \* b + (no. of intervals) \* c  
Surcharge = e.g. Base Fare \* 1.25 + d OR Base Fare \* 1.5

1. See Lab 3 Taxi Fare / Q6 for full details
2. Split into two functions, Base Fare & Surcharge Calculations, to reduce number of input parameters
3. Use Floor Divide to handle the number of 400m intervals. Bear in mind there are two cases for the interval distance fare calculation, which need to use Modulo to check
   1. Modulo == 0: e.g. at 1400m, 1800m. In this case floor divide will return 1, 2 when in reality the charge will count 1400m and 1800m as the start of the 2nd and 3rd intervals. Need to +1.
   2. Modulo != 0, use floor divide value to multiply
   3. Take note of the differing charges and interval distances before and after 9.8km
4. Dump Base Fare into Surcharge Calculation function

## W4: Pyramid Question [*]

1.  Objective is to create a pyramid with letters, as follows - e.g. word is Hey

        H
        He
        Hey
        He
        H

2.  First part is a standard for loop, then second part is reverse step

        input_string = input("Enter a message :")
        printed_value = ""
        for ch in input_string:
            printed_value += ch
            print(printed_value)
        for i in range(len(input_string) -1, -1, -1):
            print(input_string)
            input_string = input_string[:i]

## W4: Check for Minimums / Data Plan Question [**]

1.  See Lab 4 Q3 for full details
2.  The question gives you a set of tuples, and a minimum requirement, and asks you to check which set of tuples fulfills the minimum requirement
3.  Clear out the conditions that will definitely not be processed (e.g if they ask for 11GB of data but largest plan only offeres 10GB)
4.  See psuedocode

        plans = (phone0, sms0, data0), etc....
        for i in range(len(plans))
                if phone mins < plans[i][0]:
                        num = i -> this is the minimum that the next 2 need to check
                        break. any num below this, don't bother
                        break
        for j in range(num, len(plans))
                -> continue checking
        ...
        return plan num OR plan num + 1 (remember index starts from 0 while the list given to you might not be)

## W4: Check For Characters / Password Strength [***]

1. The question asks you to check if a string has certain characters, special characters, is/is not upper/lower case, has digit, etc.
2. Clear out the minimum string lengths / empty string scenarios first
3. Using a SINGLE for loop, iterate through the different conditions
4. Be careful with using breaks. Don't break out of the loop without checking through all subcharacters if the initial checks are ok (just because the first character passes doesn't mean all will pass)
5. See ICE4 Q7 for full details

## W4: Print Fibonacci without Recursion [***]

1.  See Lab 4 Q8 for Details

            for i in range(n):
                if i == 0:
                    return_string = "1"
                elif i == 1:
                    return_string = "1 1"
                    f_tuple = (1, 1)
                else:
                    current_value = f_tuple[i - 1] + f_tuple[i - 2]
                    f_tuple += current_value, -> the "," matters!!
                    return_string += str(f" {current_value}")

            print(return_string)

## W5: Tax Question, with Conditonals [*]

1. See Lab 5 Q5
2. Create a list of tuples containing bracket minimum, amount to be paid before that minimum, and the tax percentage
3. Clear out amounts below 20k and above 320k
4. Iterate thru the list of tuples. If the amount is less than the minimum, use the values from the previous set of tuples for calculation

## W5: Checking For Primes [**]

1.  From Lab 5 Q2d
2.  In checking of prime numbers, only need to check up to sqrt of number.
3.  Rounded up the sqrt and +1 to ensure that it checks properly especially for small numbers like 2, 3, 4 where a small difference in iterable range can cause the algorithm to not check certain numbers (e.g. sqrt 4 is 2, we need 2 to be included in checks, hence +1)

        def check_if_prime(number):
            sqrt_rounded = math.ceil(math.sqrt(number)) + 1
            for i in range(sqrt_rounded):
                if i == 0 or i == 1:
                    continue
                elif number % i == 0 and i != number:
                    return False
            return True

        def get_prime_numbers(num_list, sep):
            primes_list = []
            for num in num_list:
                if check_if_prime(num):
                    primes_list.append(str(num))
            return sep.join(primes_list)

## W5: Finding Non Common Elements [**]

1.  From Lab 5 Q6c
2.  2 list of strings are given to you. If the question allows you to modify either string, iterate through str2 and check if element is in str1.
3.  If element not in str1, append element to str1
4.  Return str1

        def get_non_common_strings(str_list1, str_list2):
            return_list = str_list1
            for item in str_list2:
                if item not in return_list:
                    return_list.append(item)
                else:
                    return_list.remove(item)
            return return_list

## 21LT1: List Index Swapping 1 / Teammate Swap [***]

1. 2021LT1 Q3b
2. Objective is to swap team members and check whether the new teams meet the diversity quota
3. Want to keep both lists team1, team2 intact so that proper iteration can occur
4. Create seperate team_a, team_b (total 4 lists in memory) that are copies of team1, team2 by iterating thru team1 and team2 and appending their elements. team_a and team_b will be used to swap around
5. At the respective indexes to be swapped, create a holding variable for the names. Then pop the indexes and do the swap with insert()
6. Proceed to check. If ok return team_a and team_b
7. Else "reset" team_a and team_b and re-iterate with the next indexes

## 21LT1: Permutation Handling 1 / Puzzle Solving [***]

1. 2021LTQ4
2. Brute force sovle the puzzle.
3. Iterate through the possible keys
4. Put the puzzle into a grid (i.e split the string into a list)
5. Replace \* with keys
6. Merge back the words
7. Check the vocab if the words make sense. If any word is wrong, trash the whole set and iterate with the next set of keys

## 20LT1: Getting Minimums with Conditionals [**]

        min_nos = []
        num1, num2, num3 = num_tuple
        if num1 <= num2:
            if num1 <= num3:
                min_nos.append(num1)
            else:
                min_nos.append(num3)
        elif num2 <= num3:
            if num2 <= num1:
                min_nos.append(num2)
            else:
                min_nos.append(num1)
        elif num3 <= num1:
            if num3 <= num2:
                min_nos.append(num3)
            else:
                min_nos.append(num2)

### Getting Maximums with Conditionals [**]

        min_nos = []
        num1, num2, num3 = (3, 1, 2)
        if num1 >= num2:
            if num1 >= num3:
                min_nos.append(num1)
            else:
                min_nos.append(num3)
        elif num2 >= num3:
            if num2 >= num1:
                min_nos.append(num2)
            else:
                min_nos.append(num1)
        elif num3 >= num1:
            if num3 >= num2:
                min_nos.append(num3)
            else:
                min_nos.append(num2)

### Getting Middle Number with Conditionals [**]

        def get_middle(a, b, c):
            if a < b:
                if b < c:
                    return b
                else:
                # b > c
                    if a < c:
                    # b < a < c
                        return c
                    else:
                    # a > c
                    # b > a > c
                        return a
            else:
            # a > b
                if b > c:
                # a > b > c
                    return b
                else:
                # c > b
                    if a > c:
                    # a > c > b
                        return c
                    else:
                    # c > a
                    # c > a > b
                        return a

## 20LT1: Checking Equations [***]

1. 20LT1 Q3
2. Start by clearing out empty strings or lists
3. Initialise RHS as an empty int()
4. Split string at "=" and dump new_list[1]/RHS into RHS variable, remembering to convert to int
5. Split new_list[0]/LHS by the operator, dumping the results into int1 and int2, again converting both to int
6. Compare the result of LHS with RHS

## 20LT1: Implicit While Loop / Contact Tracing [***]

1.  20LT1 Q4_better gives the most optimal code (19 lines)
2.  Relies heavily on the idea that the loop below will continue to run without limit so long answers has things left to iterate thru

        for answer in answers:
                answers.append(something)

3.  Set up a list of infected and list of persons checked thru
4.  For the list of infected, iterate through the interaction history. Ensure that the person has not been checked before. Append to the list of infected any contacts and their details.
5.  Once iteration is complete, put the person in checked
6.  Iterate through the list of infected until the last item has been checked
7.  Remove the original patient's name from checked
8.  Return list(set(checked)) to remove duplicates

## 19LT1: Check Seating Arrangement [***]

1. 19LT1 Q4a
2. 3 scenarios - check at Index 0, Final Index, and all other indexes in between
3. The testing is the same for all scenarios, but the indexes must be changed.
   1. i = 0: check 1 and last i
   2. last i = check 0 and last i - 1
   3. other: check i - 1 and i + 1
4. Iterate through the must list. If the L or R is correct, pass. Else, return False
5. Iterate through the cannot list. If the L or R is on the list, return False. Else, Pass
6. At the end, return True since the test cases passed

### Permutation Handling 2 [***]

1.  19LT Q4b
2.  Create the permutations list for males and females seperately.
3.  For each permutation of male and female seating, alternate slot them into the list
4.  Check!

        def get_seating_arrangement(female_list, male_list, must_list, cannot_list):
            male_permutations = list(itertools.permutations(male_list))
            female_permutations = list(itertools.permutations(female_list))
            for m_perm in male_permutations:
                for f_perm in female_permutations:
                    proposed_seating = []
                    for i in range(len(m_perm)):
                        proposed_seating.append(m_perm[i])
                        proposed_seating.append(f_perm[i])
                    if q4a.check_seating_arrangement(proposed_seating, must_list, cannot_list):
                        return proposed_seating
            return None

## 19LT1: List Index Swapping 2 / String Transformation [***]

1.  19LT1 Q5
2.  str1 is the start state, str2 is the end state. We want to modify str1.
3.  Create a list to store the series of transformations. Put str1 into that list.
4.  Convert both str1 and str2 into lists, list1 and list2
5.  For each index in list2, check where the respective character in list1 is. Since we are iterating from index 0, the respective character in list1 will be in an index greater or equal to list2 (i.e. character in list1 will always be in the same position or to the right)
6.  In str1, identify the number of swaps needed (usually is index of list1 - desired index in list2). For that number of times, swap with the character to the left.
7.  Append each swap to the list of transformations

        def transform(str1, str2):
            answers = [str1]
            list1 = list(str1)
            list2 = list(str2)
            for i in range(len(list2)):
                if list2[i] == list1[i]:
                    continue
                org_pos = list1.index(list2[i])
                difference = org_pos - i
                for j in range(difference):
                    swap_left = list1[org_pos - j]
                    swap_right = list1[org_pos - j - 1]
                    list1[org_pos - j] = swap_right
                    list1[org_pos - j - 1] = swap_left
                    answers.append("".join(list1))
            return answers

## W7: Pangram [**]

1.  ICE7 Q4 - A pangram is a sentence with all the words of the alphabet in it
2.  Instead of checking the characters and keeping track of which character has been used, just run through the list of alphabets and see which one is not inside

        for char in string.ascii_lowercase:
            if char not in sentence.lower():
                return False
            return True

## W7: Diamond Printing [***]

1. e1ICE& Q2, as an extension of ICE Q3
2. The diamond has sides of length n (i.e. n number of str per side). Start by finding the horizontal width and vertical length of the diamond, s. s = 2n -1
3. Each line has 3 (end whitespace + str + end whitespace) or 5 components (end whitespace + str + middle whitespace + str + end whitespace). 3 component lines are the top and bottom of the diamond.
4. Iterate through and print each line. Two seperate cases for top/bottom and middle lines.
5. The end whitespace length can be defined as abs(n - 1 - i). Hence the middle whitespace length if any is s - 2\*abs(n - 1 - i) - 2.

For the printing of diamond using a text string, we need to define s and n in terms of the string's length

1. s = int(len(text) / 4 + len(text) / 4 + 1)
2. Let len(text) / 4 be x. Since s = 2x + 1 = 2n - 1, n = x + 1, n = int(len(text) / 4 + 1)
3. Same principles as above, but replace the str with list[i]

## W7: Sublist Flattening [***]

1. e2ICE7 Q3
2. Convert the list into a string, then replace all instances of whitespace, [ and ] with empty strings. Split by , and return this new list.

## W9: Get Strings with Digits w Min Overall Digit Count [***]

1.  ICE9 Q5
2.  Objective is to iterate through the list, and add strings with digits in them until we hit a minimum number of digits for all the strings
3.  Create a function to count the number of digits in a string
4.  Create a while toop with the conditionals: while overall count is less than t and the list has not been fully iterated through yet
5.  See code snippet below:

        def get_strings_with_digits(str_list, t):
            r_list = []
            count = 0
            n = 0
            while count <= t and n < len(str_list):
                if count_digits(str_list[n]) != 0:
                    r_list.append(str_list[n])
                count += count_digits(str_list[n])
                n += 1
            return r_list

## W9: Merge Lists by Number, Ascending Order [***]

1.  eICE9 Q3
2.  Initialise two indexes to track where you are in list1 and list2, i and j.
3.  While Conditional is: while i < len(list1) and j < len(list2) - will break out if one lists ends earlier than the other
4.  Compares numbers at index i and j, and += to the index for the lower number, lower number appending to return list
5.  After breakout from while loop, append the remaining numbers with the conditional if len(list#) > index

        def merge_by_age(list1, list2):
            merged = []
            i = 0
            j = 0
            while i < len(list1) and j < len(list2):
                if list1[i][1] < list2[j][1]:
                    merged.append(list1[i])
                    i += 1
                else:
                    merged.append(list2[j])
                    j += 1
            if len(list1) > i:
                merged += list1[i:len(list1)]
            elif len(list2) > j:
                merged += list2[j:len(list2)]
            return merged

## W9: Group Numbers With Minimum Total [***]

1.  eICE Q4
2.  Two while loops:
    1. First to continue looping through while the whole list is being iterated through
    2. The while loop inside that is to handle each sub-list of numbers that total to a minimum number, threshold.
3.  The inner while loop will continually append numbers to a holding list until the threshold is exceeded. Once broken out of, function appends the holding list to the main list.

        def group_numbers(list_of_ints, threshold):
            groupings = []
            index = 0
            while index < len(list_of_ints):
                total = 0
                subgroup = []
                while total <= threshold and index < len(list_of_ints):
                    total += list_of_ints[index]
                    if total <= threshold:
                        subgroup.append(list_of_ints[index])
                        index += 1
                groupings.append(subgroup)
            return groupings

## W9: Check if Strings have Same Characters [**]

1. Lab 6 Q5. This section deals only with the third criteria of the question, all characters in first string must appear in second question
2. Use list(set(list)) to remove duplicates and then iterate through the characters in the cleaned first list and check against the cleaned second list

## W9: Line Up Question [***]

1.  Lab 6 Q7
2.  Question gives you a list of tuples and asks to sort them, with the zeroth person in the tuple always standing in front of the first person in the tuple
3.  Number of tuples will always equal number of people. Hence use a while conditional:

        while len(lined_up) != len(list_of_tuples)

4.  Work from the back forwards. Identify the final tuple (whose first item (0, 1) will be "") and append the final person
5.  Insert the remaining people at position zero. Continually iterate through the list to find the person in front, ensuring that the tuple has not been used before.

        def line_up(list_of_tuples):
            lined_up = []
            while len(lined_up) != len(list_of_tuples):
                for each_tuple in list_of_tuples:
                    if "" in each_tuple and each_tuple[0] not in lined_up:
                        lined_up.append(each_tuple[0])
                    elif len(lined_up) != 0 and each_tuple[1] == lined_up[0] and each_tuple[0] not in lined_up:
                        lined_up.insert(0, each_tuple[0])
            return lined_up

## W10: Sort by Subject and Find Classmates [***]

1. eICE10 1b. File handling + While Loops.
2. Open the file and append its contents to a holding list
3. If the subject has been added, skip over it
4. Else, add the list of names related to that subject as a sub-list to the main name list
5. For each sub-list of classmates, compare one with another to create pairings that can be checked through.
   1. If there is a duplicate, skip to the next pairing.
   2. If it is a unique pair, append the pairing as a tuple

## W10: Matrix Transpose [**]

1.  Lab 7 Q5b

        def get_matrix_transpose(file):
            transposed = []
            index = 0
            original = get_matrix(file)
            while index < len(original):
                new_row = []
                for row in original:
                    new_row.append(row[index])
                transposed.append(new_row)
                index += 1
            return transposed

## W10: Docstring Finding [***]

1.  Lab 7 Q6
2.  The script is a python file, and need to find docstrings that are attached to each function
3.  Dump the whole code into a string, and split the string by "def" because we know each function will only have 1 set of docstring
4.  pop the zeroth index which will be ""
5.  For each portion of code, find the start and end indexes of the docstring with find() and rfind()
6.  Add blank spaces as necessary

        def extract_functions(python_filename, output_filename):
            lines = ""
            with open(python_filename, "r") as python_file, open(output_filename, "w") as output_file:
                for line in python_file:
                    lines += line
                functions = lines.split("def")
                functions.pop(0)
                for i in range(len(functions)):
                    name, contents = functions[i].split(":", 1)
                    ds_start = contents.find('"""')
                    ds_end = contents.rfind('"""')
                    docstring = contents[ds_start + 3:ds_end].strip().strip("\n")
                    if docstring[0:4] != "    ":
                        docstring = "    " + docstring
                    name = f"{i + 1}.{name}"
                    output_file.write(f"{name}\n{docstring}\n\n")

## W10: Scramble Words Keep Punctuation/First/Last Letter [****]

1.  Lab 7 Q7

        def scramble_word(word):
            # there is no need to scramble words that are 3 characters or less in length, return them directly
            if len(word) <= 3:
                return word
            # initialise list of exceptions, and prepare an empty list to store tuples of (index, exception)
            punctuation = ",'!.:"
            punctuation_index = []
            letters = []
            # if punctuation is at the back of the word, we don't want it inside. store it to put back later
            if word[-1] in punctuation:
                back_punctuation = word[-1]
                clean_word = word[:-1]
            else:
                back_punctuation = ""
                clean_word = word
            # dump the non-punctuation middle characters into the list "letters"
            # for punctutation, send (index, punctutation) to the list "punctuation_index"
            for i in range(1, len(clean_word) - 1):
                if word[i] in punctuation:
                    punctuation_index.append((i, clean_word[i]))
                else:
                    letters.append(clean_word[i])
            # shuffle the middle characters
            random.shuffle(letters)
            # using the stored list of (index, punctuation), reinsert the punctuation
            for punctuation_tuple in punctuation_index:
                letters.insert(punctuation_tuple[0], punctuation_tuple[1])
            # generate the number of unique letters in the middle for the recursion check later
            unique_letters_inside = len(list(set(letters)))
            # insert the front and back letters and join back the word
            letters.insert(0, clean_word[0])
            letters.insert(len(clean_word) - 1, clean_word[len(clean_word) - 1])
            new_word = "".join(letters)
            # re-generate a shuffled word if the new word is same as the original
            # however, do not regenerate if unique letters inside = 1 (e.g. "need") because it will cause the function to run forever
            if unique_letters_inside != 1:
                while new_word == clean_word:
                    # uncomment the line below to see if we need to re-shuffle
                    print(
                        f"RECURSION ACTIVATED for {new_word}: duplicates {clean_word}")
                    new_word = scramble_word(clean_word)
            # add back the back punctuation, if any
            returned_word = new_word + back_punctuation
            return returned_word

## W11: Degrees of Separation [***]

1.  eICE Q2
2.  Similar to the contact tracing question, we will need a while loop of sorts. The While Conditional is while index < degrees of separation
3.  Text file contents are dumped into key:value pairs based on the sequential order of the words given
4.  Create a new dictionary, the key being the DOS and the value being the people in that DOS
5.  Check through the keys and values associated with that person and add it to the dictionary of DOS and people if unique
6.  Repeat the same process with the people for each DOS value

        friends = {}
        with open("friends.txt", "r") as input_file:
            for line in input_file:
                stripped = line.strip("\n").split("\t")
                if stripped[0] not in friends:
                    friends[stripped[0]] = [stripped[1]]
                else:
                    friends[stripped[0]].append(stripped[1])

        original = input("Name: ")
        check = [original]
        dos = int(input("Degrees of separation, n: "))
        index = 1
        final_list = []
        friend_link = {}
        while index <= dos:
            holding = []
            for name in check:
                if name in friends:
                    holding += friends[name]
                for each_item in friends.items():
                    each_key, each_val = each_item
                    if name in each_val:
                        holding.append(each_key)
            holding = list(set(holding))
            unique = []
            for i in range(len(holding)):
                if holding[i] not in final_list and holding[i] != original:
                    unique.append(holding[i])
            check = unique
            final_list += unique
            friend_link[index] = unique
            index += 1

## W11: Nested Dictionaries [**]

Honestly there's not much to say about this other than make use of it! It's a good way to organise information without the use of pandas dataframes.

As a visual:

        mydict =
        {
            Name1: {
                School: SOE,
                GPA: 3.7
            }
            Name 2: {
                School: SCIS
                GPA: 3.05
            }
        }

Name 1's GPA can be accessed and modified with

        mydict[Name1][GPA]

When creating "mini databases" in exam settings, try to make use of the above visualisation for as to how you want to sort your data

Applicable to Lab 8 Q3 and 6.

## W12: Due Date Scheduling [***]

1. eICE12 Q1
2. The part about entering new key-value pairs as proxies for due dates and task at hand is fairly standard. What is more complex is how to sort it by date
3. No need to sort the dictionary. Instead, generate a list of numbers (1-31)/(1-12) to be put into a for loop. Iterate through all the days in the year and check if the date exists as a key in the dictionary. If it does, print out the tasks due

## MLT2: Separate Numbers & Calculate Averages [***]

1. MLT2 Q3
2. Fairly standard question, open the text file and clean, and split the lines by the separator
3. Split the strings again by whitespace, calculate averages (remember to convert type)
4. Set negative infinity as the lowest average and use max function to compare the averages
5. Remember to write the result properly to the output file
