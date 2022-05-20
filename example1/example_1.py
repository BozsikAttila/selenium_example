#Count back from 100 to 1 and print:
# - Agile if number is divisible by 5
# - Software if number is divisible by 3
# - Testing if number is divisible by both
# - Otherwise print the number

def example_1():
    for i in range(100, 0, -1):
        out = i
        if (i % 3 == 0) and (i % 5 == 0): out = "Testing"
        elif (i % 3 == 0): out = "Software"
        elif (i % 5 == 0): out = "Agile"
        print(out)

if __name__ == '__main__':
    example_1()
