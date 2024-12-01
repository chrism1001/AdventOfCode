from collections import defaultdict

def part2():
    left = []
    freq = defaultdict(int)
    
    with open("day1/day1.txt") as file:
        for line in file:
            numbers = line.split()
            left.append(int(numbers[0]))
            freq[int(numbers[1])] += 1
    
    result = 0
    for n in left:
        result += n * freq[n]
        
    print(result)

def part1():
    left, right = [], []
    
    with open("day1/day1.txt") as file:
        for line in file:
            numbers = line.split()
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
            
    left.sort()
    right.sort()
    
    result = 0
    for i in range(len(left)):
        result += abs(left[i] - right[i])
        
    print(result)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
