def same_author(file_name):
    author = ""
    same = True
    with open(file_name, "r") as new_file:
        for line in new_file:
            columns = line.split("\t")
            if author == "":
                author = columns[1]
            elif author == columns[1]:
                continue
            else:
                same = False
                break
    return same


# Test cases used to test your function
print('\nTestcase 1')
print('-' * 10)
print("Expected: False")
filename = 'books-1.txt'
result = same_author(filename)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print("Expected: True")
filename = 'books-2.txt'
result = same_author(filename)
print('Actual:   ' + str(result))

print('\nTestcase 3')
print('-' * 10)
print("Expected: False")
filename = 'books-3.txt'
result = same_author(filename)
print('Actual:   ' + str(result))
