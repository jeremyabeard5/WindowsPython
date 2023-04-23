

# define main function
def main():
    # print hello world
    print('Hello World')
    # get input integer from user
    inputNum = input('Enter a number: ')
    inputNum = testNumIntness(inputNum)
    
    
    # test if inputNum is not null, else set to 0
    inputNum = inputNum if inputNum else 0
    # print the input number
    print('You entered: ', inputNum)
    


# function that will add 2 to any number
def add2toNum(num):
    # return the number plus 2
    return num + 2

def sub2fromNum(num):
    # return the number minus 2
    return num - 2


# test if user accidentally entered a string for inputNum
def testNumIntness(num):
    try:
        num = int(num)
        return num
    except ValueError:
        print('You entered a string, please enter an integer')
        return 0


# python file main function
if __name__ == '__main__':
    # call main function
    main()
    
