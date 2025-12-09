def read_input(path="input.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def solve(data):
    sum_invalid_ids = 0
    split = data[0].split(",")
    for element in split:
        values = element.split("-")
        for x in range(int(values[0]), int(values[1])+1):
            string_x = str(x)
            length = len(string_x) # number of digits
            for i in range(0, length // 2):
                num_reps = len(string_x) // (i+1)
                if(string_x == string_x[:i+1]*num_reps):
                    sum_invalid_ids += x
                    break
    return sum_invalid_ids
        

if __name__ == "__main__":
    inp = read_input()
    print(solve(inp))
