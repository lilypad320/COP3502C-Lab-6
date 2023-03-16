# Elizabeth Rush
run = True
while run:
    print('Menu\n-------------\n1.Encode\n2.Decode\n3.Quit')
    user_input = int(input())
    if user_input == 1:
        print('Please enter your password to encode:', end=' ')
        password_string = input()
        encoded_list = [int(i) for i in str(password_string)]
        new_list = []
        for num in encoded_list:
            new_list.append(num + 3)
        encoded_string = [str(i) for i in new_list]
        encoded_list = ''.join(encoded_string)
        print('Your password has been encoded and stored!')
    elif user_input == 2:
        pass
    elif user_input == 3:
        run = False
        break
