import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers=[]
    total=0
    value=0
    while value<5:
        randomnum = random.randint(0,100)
        numbers.append(randomnum)
        total += randomnum 
        value += 1    
    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
