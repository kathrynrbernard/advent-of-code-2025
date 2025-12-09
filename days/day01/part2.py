import math

def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def solve(data):
    cur_pos = 50
    zero_count = 0
    for element in data:
        prev_pos = cur_pos
        direction = element[0] # first digit - L or R
        magnitude = int(element[1:]) # remaining digits

        num_rotations = math.floor(magnitude / 100)

        magnitude = magnitude % 100

        if direction == "L":
            cur_pos = cur_pos - magnitude
            if cur_pos < 0:
                cur_pos = 100 - abs(cur_pos)
                if cur_pos != 0 and prev_pos != 0:
                    zero_count += 1
            
        elif direction == "R":
            cur_pos = cur_pos + magnitude
            if cur_pos > 99:
                cur_pos = cur_pos - 100
                if cur_pos != 0 and prev_pos != 0:
                    zero_count += 1

        if cur_pos == 0:
            zero_count += 1
        zero_count += num_rotations
        
    return zero_count
        

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
