from collections import defaultdict

def main():
    left, right = [], []
    freq = defaultdict(int)
    
    with open("day1/day1.txt") as file:
        for line in file:
            numbers = line.split()
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
            freq[int(numbers[1])] += 1
            
    # left.sort()
    # right.sort()
    
    result = 0
    # for i in range(len(left)):
    #     result += abs(left[i] - right[i])
        
    for n in left:
        result += n * freq[n]
        
    print(result)

if __name__ == "__main__":
    main()
