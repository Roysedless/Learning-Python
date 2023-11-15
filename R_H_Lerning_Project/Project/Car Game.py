# Building a Car Game
# ^^ Making a Car Game using all we learn so far

# my solution
# print('(: Typ an help to see info (:')
# while True:
#     command = input('> ')
#     if command.upper() == 'HELP':
#         print("""
#         START - to start the car.
#         STOP - to stop the car.
#         QUIT - to exit
#         """)
#     elif command.upper() == 'START':
#         print('The car is driven (:, ready to go.')
#     elif command.upper() == 'STOP':
#         print('The car is brake, time to rest a bit.')
#     elif command.upper() == 'QUIT':
#         print('Bye hope to see you soon.')
#         break
#     else:
#         print('''
#         Sorry, your typ must be included in the available options );
#         please try again >>
#         ''')

# Mosh solution + add my solution of the challenge
# ^ making stop and start only in time.
# print('(: Typ an help to see info (:')
# command = ''
# count = 1
# while True:
#     command = input('> ').upper()
#     if command == 'HELP':
#         print("""
# START - to start the car.
# STOP - to stop the car.
# QUIT - to exit
#         """)
#     elif command == 'START' and count == 1:
#         print('The car is start (:, ready to go.')
#         count += 1
#     elif command == 'START' and count == 2:
#         print('you already started')
#         count -= 1
#     elif command == 'STOP' and count == 1:
#         print('The car is stop, time to rest a bit.')
#         count += 1
#     elif command == 'STOP' and count == 2:
#         print('you already stopped')
#         count -= 1
#     elif command == 'QUIT':
#         print('Bye hope to see you soon.')
#         break
#     else:
#         print('''
# Sorry, your typ must be include in the available options );
# please try again >>
#         ''')

# mosh challenge solution
print('(: Typ an help to see info (:')
command = ''
started = False
while True:
    command = input('> ').upper()
    if command == 'HELP':
        print("""
START - to start the car.
STOP - to stop the car.
QUIT - to exit
        """)
    elif command == 'START':
        if started:
            print('You already started')
        else:
            started = True
            print('The car is start (:, ready to go.')
    elif command == 'STOP':
        if not started:
            print('You already stopped')
        else:
            started = False
            print('The car is stop, time to rest a bit.')
    elif command == 'QUIT':
        print('Bye hope to see you soon.')
        break
    else:
        print('''
Sorry, your typ must be include in the available options );
please try again >>
        ''')