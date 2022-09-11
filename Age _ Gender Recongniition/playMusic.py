from winsound import PlaySound


fun playMusic(age, gender):
    if ageFound == "(20-25)" and gender == "Male":
    file = open('hipHop', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)
        break


if ageFound == "(20-25)" and gender == "Female":
    file = open('dance', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)

if ageFound == "(26-30)" and gender == "Male":
    file = open('jazz', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)
        break


if ageFound == "(26-30)" and gender == "Female":
    file = open('acoustic', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)