print('Hello, Welcome to nats bank account')
restart=('Y')
chances = 3
balance = 8000
while chances >= 0:
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (0000):
        print('You entered you pin Correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Press 1 For Your Balance\n')
            print('Press 2 To Make a Withdrawl\n')
            print('Press 3 To Pay in\n')
            print('Press 4 To Return Card\n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('Your Balance is Â£',balance,'\n')
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawa = float(input('How Much Would you like to withdraw? \nÂ£10/Â£20/Â£40/Â£60/Â£80/Â£100 for other enter 1:'))

                if withdrawl in [100, 200, 400, 600, 800, 1000]:
                    balance = balance - withdrawl
                    print ('\nYour Balance is now Â£',balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [100, 200, 400, 600, 800, 1000]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))

            elif option == 3:
                Pay_in = float(input('How Much Would You Like To Pay In? '))
                balance = balance + Pay_in
                print ('\nYour Balance is now Â£',balance)
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for you service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('0000'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break