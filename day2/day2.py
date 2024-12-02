def part1():
    result = 0
    
    with open("day2/day2.txt") as file:
        for line in file:
            line = line.split()
            
            safe = True
            direction = 0
            for i in range(1, len(line)):
                diff = int(line[i-1]) - int(line[i])
                
                if i == 1 and diff < 0:
                    direction = -1
                elif i == 1 and diff > 0:
                    direction = 1
                
                if abs(diff) < 1 or abs(diff) > 3:
                    safe = False
                    break
                
                if i > 1 and (direction == -1 and diff > 0) or (direction == 1 and diff < 0):
                    safe = False
                    break
    
            result += 1 if safe == True else 0
            
    print(result)

def main():
    part1()
        
if __name__ == "__main__":
    main()