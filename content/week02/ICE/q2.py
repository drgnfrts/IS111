# ################################################################################
# The following code is given to you.
def print_a_line():
    """
    This function displays a line of 20 dashes.
    """
    print("--------------------")


def print_a_message(msg, symbol):
    """
    This function displays a given text message enclosed in a pair of the specified symbols.
    For example, if msg is "Welcome" and symbol is "#", then the function displays "# Welcome #".

    Parameters:
      - msg: A string that represents the text message to be displayed.
      - symbol: A single character that is used to enclose the text message.
    """
    print(symbol + " " + msg + " " + symbol)


# ################################################################################
# Write your code below:
print_a_line()
print_a_message("Hello SIS!", "|")
print_a_line()

print_a_line()
print_a_message("Hello Python!", "*")
print_a_message("Hello Functions!", "$")
print_a_line()
