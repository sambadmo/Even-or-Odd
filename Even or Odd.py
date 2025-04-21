#Even or Odd Checker
#variables
even_list = []
even_count = 0
odd_list =[]
odd_count = 0
total_count = 0
total = 0
#Loop
while True:
    number = input('Enter a number or Stop to quit: ').lower()
    if number == 'stop':
            break
    try:
        number = int(number)
        if number % 2 == 0:
            even_list.append(number)
            print(f'{number} is even!')
            even_count += 1
        elif number % 2 != 0:
            odd_list.append(number)
            print(f'{number} is odd!')
            odd_count += 1
    except ValueError:
        print('Please enter a number.')

total = even_count + odd_count
total_count = sum(even_list + odd_list)
average = total_count / total

print('-' * 40)
#organized conditions
if len(even_list) > 0:
    print('Even numbers you\'ve entered:', even_list)
    print('The total even numbers you entered is:', even_count)
    print(f'The highest even number is {max(even_list)}. While the lowest even number is {min(even_list)}.')
if len(even_list) == 0:
    print('No even numbers were entered.')

print('-' * 40)

if len(odd_list) > 0:
    print('Odd numbers you\'ve entered:', odd_list)
    print('The total odd numbers you entered is:', odd_count)
    print(f'The highest odd number is {max(odd_list)}. While the lowest odd number is {min(odd_list)}.')
if len(odd_list) == 0:
    print('No odd numbers were entered.')

print('-' * 40)

print(f'The average is {average:.0f}.')