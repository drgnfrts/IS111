# no use of lists, dictionaries and conditionals

one = "A partridge in a pear tree"
two = "Two turtle doves, and"
three = "Three French hens"
four = "Four colly birds"
five = "Five gold rings"
six = "Six geese a-laying"
seven = "Seven swans a-swimming"
eight = "Eight maids a-milking"
nine = "Nine ladies dancing"
ten = "Ten lords a-leaping"
eleven = "Eleven pipers piping"
twelve = "Twelve drummers drumming"


def day(num):
    print(f"On the {num} day of Christmas my true love gave to me")


def first_day():
    print(one)


def second_day():
    print(two)
    first_day()


def third_day():
    print(three)
    second_day()


day("first")
first_day()
day("second")
second_day()
