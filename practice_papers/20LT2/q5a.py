# Name:
# Email ID:
def add_power(polynomial):
    r_list = []
    count = 0
    for i in range(-1, -len(polynomial) - 1, -1):
        r_list.insert(0, [count, polynomial[i]])
        count += 1
    return r_list


def multiply_2(poly1, poly2):
    highest_power = poly1[0][0] + poly2[0][0]
    poly_dict = {}
    r_list = []
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            multiple = poly1[i][1] * poly2[j][1]
            power2 = poly1[i][0] + poly2[j][0]
            if power2 in poly_dict:
                poly_dict[power2] += multiple
            else:
                poly_dict[power2] = multiple
    for k in range(highest_power, -1, -1):
        r_list.append([k, poly_dict[k]])
    return r_list


def multiply(polynomials):
    converted = []
    final = []
    if len(polynomials) == 1:
        return polynomials[0]
    for polynomial in polynomials:
        if polynomial == [0]:
            return [0]
        converted.append(add_power(polynomial))
    holding = converted[0]
    for l in range(1, len(converted)):
        holding = multiply_2(holding, converted[l])
    for m in range(len(holding)):
        final.append(holding[m][1])
    return final


# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)

    polynomials = [[1, 2, 3], [5, 6, 7]]
    print(f"Test Case {tc_num} : multiply({polynomials})")
    print("Expected : [5, 16, 34, 32, 21]")
    result = multiply(polynomials)
    print(f"Actual   : {result}")
    print()

    print("Expected return type : <class 'list'>")
    print(f"Actual return type   : {type(result)}")

    print()

    print("Expected return type of the first element of the list : <class 'int'>")
    print("Actual return type of the first element of the list   : ", end="")
    if (isinstance(result, list)):
        print(type(result[0]))
    else:
        print("N/A")

    tc_num += 1
    print('-' * 40)

    polynomials = [[1, 2], [3, 4, 5], [6, 7, 8]]
    print(f"Test Case {tc_num} : multiply({polynomials})")
    print('Expected : [18, 81, 172, 231, 174, 80]')
    print(f"Actual   : {multiply(polynomials)}")
    print()

    tc_num += 1
    print('-' * 40)

    polynomials = [[1, 2], [0], [3, 4, 5], [6, 7, 8]]
    print(f"Test Case {tc_num} : multiply({polynomials})")
    print('Expected : [0]')
    print(f"Actual   : {multiply(polynomials)}")
    print()

    tc_num += 1
    print('-' * 40)

    polynomials = [[1, 2, 3], [5, 6, 7], [8, 9, 0]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print('Expected : [40, 173, 416, 562, 456, 189, 0]')
    print(f'Actual   : {multiply(polynomials)}')
    print()

    tc_num += 1
    print('-' * 40)

    polynomials = [[1, 1, -1, 1], [2, 0], [8, 9, 0]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print('Expected : [16, 34, 2, -2, 18, 0, 0]')
    print(f'Actual   : {multiply(polynomials)}')
    print()

    tc_num += 1
    print('-' * 40)

    polynomials = [[1], [0]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print('Expected : [0]')
    print(f'Actual   : {multiply(polynomials)}')
    print()

    tc_num += 1
    print('-' * 40)

    polynomials = [[1, 5, 0, 4]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print(f'multiply({polynomials})')
    print('Expected : [1, 5, 0, 4]')
    print(f'Actual   : {multiply(polynomials)}')
    print()
