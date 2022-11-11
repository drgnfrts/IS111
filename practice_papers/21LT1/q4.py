# Name:
# Email ID:

import itertools


def print_puzzle(puzzle):
    print(' |0 1 2 3 4 5 6 7 ')
    print('-' * 17)
    index = 0
    for row in puzzle:
        print(str(index) + '|', end='')
        index = index + 1
        for ch in row:
            print(ch + ' ', end='')
        print()


def solve_puzzle(puzzle, word_positions, key, vocabulary):
    all_sequences = itertools.permutations(key)
    for sequence in all_sequences:
        count = 0
        grid_puzzle = []
        answers = []
        works = True
        for string in puzzle:
            dump_list = []
            dump_list[:0] = string
            grid_puzzle.append(dump_list)
        for y in range(len(grid_puzzle)):
            for x in range(len(grid_puzzle[y])):
                if grid_puzzle[y][x] == "*":
                    grid_puzzle[y][x] = sequence[count]
                    answers.append((y, x, sequence[count]))
                    count += 1
        for i in range(len(word_positions)):
            if word_positions[i][2] == "H":
                column_y, x_index, direction, word_length = word_positions[i]
                holding_list = grid_puzzle[column_y][x_index:
                                                     (word_length + x_index)]
            elif word_positions[i][2] == "V":
                column_y, x_index, direction, word_length = word_positions[i]
                holding_list = []
                for j in range(word_length):
                    holding_list.append(grid_puzzle[column_y + j][x_index])
            test_string = "".join(holding_list)
            if test_string not in vocabulary:
                works = False
                break
        if works:
            return answers
