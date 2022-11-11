puzzle = ['BRE* BED',
          '     * I',
          '  BIRD R',
          '  I I  *',
          'R *IDE  ',
          'I D     ',
          '*RIDE   ',
          '  E     ']

vocabulary = ["BRED", "BED", "BID", "DIRE", "BIRD",
              "BIRDIE", "RIB", "BRIDE", "RIDE", "RID"]

key = "BDEIR"

word_positions = [(0, 0, 'H', 4), (0, 5, 'H', 3),
                  (2, 2, 'H', 4), (4, 2, 'H', 4),
                  (6, 0, 'H', 5), (0, 5, 'V', 3),
                  (0, 7, 'V', 4), (2, 2, 'V', 6),
                  (2, 4, 'V', 3), (4, 0, 'V', 3)]

# permutations_of_keys = ()
# all_sequences = itertools.permutations(keys):
# for sequence in all_sequences:
#     permutations_of_keys += sequence

test_sequence = ("D", "I", "E", "R", "B")

count = 0
grid_puzzle = []
for string in puzzle:
    dump_list = []
    dump_list[:0] = string
    grid_puzzle.append(dump_list)
for y in range(len(grid_puzzle)):
    for x in range(len(grid_puzzle[y])):
        if grid_puzzle[y][x] == "*":
            grid_puzzle[y][x] = test_sequence[count]
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
