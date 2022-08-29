# Simple arithmetic formatter to which you pass arithmetic operations
# arithmetic operations are displayed in console vertically, as in primary school

# Example
# args_list = ['2.3 + 3', '9 - 1', '6 + 2', '2 - 2', '4 % 3', '7 / 4', '5 * 3']

print('Type some basic arithmetic problems to solve (e.g. 2 + 4, 5 * 3, 120 / 5, 8 % 2 ...).')
print('Operations must be typed one by one.')
print('Type "end", "quit" or "q" to terminate the program.')
args_list = []

while True:
    # TODO add some input validation
    
    args = input('List of problems to solve: ')
    args_list.append(args)
    print(args_list)
    if args == 'end' or args == 'quit' or args == 'q':
        print('Program was ended by user')
        break

def arithmetic_arranger(problems):
    for problem in problems:
        problem = problem.split()

        if '+' in problem:
            add = float(problem[0]) + float(problem[2])
            print('   ', problem[0])
            print('+  ', problem[2])
            print('-----\n   ', add, '\n')
        elif '-' in problem:
            subtract = float(problem[0]) - float(problem[2])
            print('   ', problem[0])
            print('-  ', problem[2])
            print('-----\n   ', subtract, '\n')
        elif '*' in problem:
            multiply = float(problem[0]) * float(problem[2])
            print('   ', problem[0])
            print('*  ', problem[2])
            print('-----\n   ', multiply, '\n')
        elif '/' in problem:
            divide = float(problem[0]) / float(problem[2])
            print('   ', problem[0])
            print('/  ', problem[2])
            print('-----\n   ', divide, '\n')
        elif '%' in problem:
            modulo = float(problem[0]) % float(problem[2])
            print('   ', problem[0])
            print('%  ', problem[2])
            print('-----\n   ', modulo, '\n')

arithmetic_arranger(args_list)