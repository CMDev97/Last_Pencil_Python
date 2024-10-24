import random

msg_many_pencils = "How many pencils would you like to use:"
msg_name = "Who will be the first (John, Jack):"

msg_no_number_pencils = "The number of pencils should be numeric"
msg_number_not_positive = "The number of pencils should be positive"
msg_invalid_name = "Choose between 'John' and 'Jack'"
msg_possible_values = "Possible values: '1', '2' or '3'"
msg_overflow_pencils = "Too many pencils were taken"


def input_start_pencils():
    print(msg_many_pencils)
    while True:
        try:
            counter = int(input())
            if counter > 0:
                return counter
            raise IndexError()
        except ValueError:
            print(msg_no_number_pencils)
        except IndexError:
            print(msg_number_not_positive)


def input_start_user():
    print(msg_name)
    while True:
        command_user = input().lower()
        if command_user == "john" or command_user == "jack":
            return command_user
        else:
            print(msg_invalid_name)


def input_number_pencils(max_pencils):
    while True:
        try:
            number_pencils = int(input())
            if 0 < number_pencils < 4:
                if number_pencils > max_pencils:
                    raise OverflowError()
                return number_pencils

            raise IndexError()
        except (ValueError, IndexError):
            print(msg_possible_values)
        except OverflowError:
            print(msg_overflow_pencils)


def bot_decision(pencil_enables):
    if (pencil_enables % 4) == 0:
        return 3
    if (pencil_enables % 2) == 1:
        return 2 if pencil_enables > 2 else 1
    if (pencil_enables % 2) == 0:
        return 1

    return random.choice([1, 2, 3])


users = ["john", "jack"]

count_pencil = input_start_pencils()
name = input_start_user()
stage = users.index(name)
bot_user = 1
while count_pencil > 0:
    pencils = ["|" for i in range(count_pencil)]
    print(''.join(pencils))
    print(f"{users[stage]}'s turn:")
    if stage == bot_user:
        remove_pencil = bot_decision(count_pencil)
        print(remove_pencil)
    else:
        remove_pencil = input_number_pencils(count_pencil)
    count_pencil -= remove_pencil
    stage = stage + (1 if stage == 0 else -1)
    if count_pencil == 0:
        print(f"{users[stage]} won!")





