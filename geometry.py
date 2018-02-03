def calc_trapeze_square(base1, base2, height):
    return (base1 + base2) * height * 0.5

def calc_truncated_trapeze_height(base1, base2, height, truncated_height):
    return 0.5 * truncated_height * (2 * base1 + truncated_height * (base2 - base1)/height)

def calc_square(initial_data, distance):
    trapeze_data = [(height, initial_data[i+1][0], length) for i, (height, length) in enumerate(initial_data) if i+1 < len(initial_data)]
    # print(trapeze_data)

    square = 0
    remaining_distance = distance
    for base1, base2, height in trapeze_data:
        if remaining_distance - height < 0:
            square += calc_truncated_trapeze_height(base1, base2, height, remaining_distance)
            break
        else:
            square += calc_trapeze_square(base1, base2, height)
            remaining_distance -= height

    return square