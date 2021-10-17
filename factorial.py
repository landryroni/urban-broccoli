# find the factorial of ouput 
import sys


def factorial(x):
    if x == 0:
        return 1
    else :
        return x * factorial(x-1)

if __name__ == "__main__":
    nums = sys.argv[1:]
    # print(nums)
    print('Computing the factorial of',nums)
    for num in nums:
        num =int(num)
        result = factorial(num)
        print('The factorial of {} is {}'.format(num,result))