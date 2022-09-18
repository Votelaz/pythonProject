import string

valid2 = string.ascii_letters + string.digits + '@' + '.' + '_'


def ver(x):
    if set(x) <= set(valid1):

        if x.count("@") == 1 or x.count(".") == 1:
            print("ДА")
        else:
            print("НЕТ")
    else:
        print("НЕТ")


x = input()
ver(x)