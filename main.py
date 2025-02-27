import Qac
from Qac import categorical_choices, binary_choices

isDone = False
user_input_message = "input your choice here: "

while not isDone:
    print("\n", Qac.questions[0]) # choice
    print(categorical_choices)
    x = input(user_input_message)

    if int(x) > 3:
        print(Qac.questions[1]) # coe-cod
        print(binary_choices)
        x = input(user_input_message)
        if x.lower() == 'y':
            print(Qac.consider[2]) # pacucoa
            print(binary_choices)
            x = input(user_input_message)
            if int(x) > 3:
                print(Qac.consider[1])
                isDone = True
            else:
                print(Qac.consider[3])
                isDone = True
        else:
            print(Qac.consider[1])
            isDone = True
    elif int(x) == 3: # root neutral
        print(Qac.consider[2])
        isDone = True
    else:
        print(Qac.questions[3]) # consider
        print(categorical_choices)
        x = input(user_input_message)

        if int(x) > 3:
            print(Qac.questions[5]) # mother occ
            print(binary_choices)
            x = input(user_input_message)

            if x.lower() == 'y':
                print(Qac.consider[1])
                isDone = True
            else:
                print(Qac.consider[2])
                isDone = True
        else:
            print(Qac.questions[4]) # engineering
            print(binary_choices)
            x = input(user_input_message)
            if x.lower() == 'y':
                print(Qac.consider[4])
                isDone = True
            else:
                print(Qac.questions[6]) # father occ
                print(binary_choices)
                x = input(user_input_message)
                if x.lower() == 'y':
                    print(Qac.consider[1])
                    isDone = True
                else:
                    print(Qac.consider[5])
                    isDone = True