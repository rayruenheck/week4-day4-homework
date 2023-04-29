#Write a function that prints the numbers from 1 to n. But for multiples of 3, print ‘Fizz’ instead of the number, and for multiples of 5, print ‘Buzz’. For numbers that are multiples of both 3 and 5, print ‘FizzBuzz’
# Sample output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11


def rangelist(n):

    for i in range(1, n+1):
        
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')

        elif i % 5 == 0:
            print('fizz')
        elif i % 3 == 0:
            print('buzz')
        
        else: print(i)
    


rangelist(30)


