def upper():
    upper_line = input('Enter here: ')
    high_letter = ""
    for ch in upper_line:
        if 65 <= ord(ch) <= 90:
            x = ord(ch) - 32
            y = chr(x)
            high_letter = high_letter + y
    return print(high_letter)
def lower():
    lower_line = input('Enter here: ')
    low_letter = ""
    for ch in lower_line:
        if 97 <= ord(ch) <= 122:
            x = ord(ch) - 32
            y = chr(x)
            low_letter = low_letter + y
    print(low_letter)
    return print(low_letter)
def isdigit(validity):
    return
def title():
    return
def split():
    return
def join():
    return
def capitalize():
    capitalize_line = input('Enter here: ')
    letter = ""
    while ch in capitalize_line():
        if 97 <= ord(ch) <= 122:
            x = ord(ch) - 32
            y = chr(x)
            letter = letter + y
            break
        else:
            x = ord(ch) + 0
            y = chr(x)
            letter = letter + y
            continue
    print(letter)
def replace():
    return
while True:
    choose = input('Hi, this my new homework!\n Choose what operation do you want to use.\n '
          '1.Upper.\n2.Lower\n3.Isdigit\n4.Title\n5.Split\n6.Join\n7.Capitalize\n8.Replace')
    if choose == '1':
        print('Operation upper is selected')
        upper()
    elif choose == '2':
        print('Operation lower is selected')
        lower()
    elif choose == '3':
        print('Operation isdigit is selected')
        isdigit()
    elif choose == '4':
        print('Operation title is selected')
        title()
    elif choose == '5':
        print('Operation split is selected')
        split()
    elif choose == '6':
        print('Operation join is selected')
        join()
    elif choose == '7':
        print('Operation capitalize is selected')
        capitalize()
    elif choose == '8':
        print('Operation replace is selected')
        replace()
    else:
        misstake = input('Sorry, but i have 8 operation, maybe you want repeat.\n y. yes\n n. no')
        if mistake == 'y':
            continue
        elif misstake == 'n':
            break
        else:
            print('ERROR')
            break