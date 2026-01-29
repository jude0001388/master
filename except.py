sum =0
count=0
try:
    number = int(input('Enter a number: '))
except ValueError:
    print('Enter a number')
    while number != 0:
        sum += number
        count += 1
        number = int(input('Enter a number, "0 exit'))
        avg = sum/count
        print('The average price of {} is {}'.format(number,avg))
except ZeroDivisionError:
    print('You cannot divide by zero')
except ValueError:
    print('Enter a number')
except:
