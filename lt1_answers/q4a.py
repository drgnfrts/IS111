# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def is_overlapping(rect_1, rect_2):
    # Replace the code below with your implementation.
    occupied_by_rect1 = []
    occupied_by_rect2 = []
    name, x, y, x_len, y_len = rect_1
    for j in range(x_len):
        for k in range(y_len):
            occupied_by_rect1.append((x + j, y + k))
    name, x, y, x_len, y_len = rect_2
    for j in range(x_len):
        for k in range(y_len):
            occupied_by_rect2.append((x + j, y + k))
    for grid_square1 in occupied_by_rect1:
        for grid_square2 in occupied_by_rect2:
            if grid_square1 == grid_square2:
                return True
    return False
