# Phyllis Torres
# Final Project Task 2
# Due 12/1/2016

# import the datetime module
from datetime import datetime

# get the current date
today = datetime.today()

# define colors and bold text parameters
class color:
    def __init__(self):
        pass
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print color.BOLD + '\n To Bean or Not to Bean...\n\n' + color.END,
print('                              Proprietor: Phyllis Torres\n\n'),
# print the curent day of the week in the following format: day of the week, month, day and year
print ('                           Today is: ' + today.strftime("%A, %b %d, %Y\n\n"))

selection = 0

# define function to handle the selection for a returning guest
def returningcust():
    print '\nYou have selected the Returning Customer Option'
    return

# define function to handle the selection for a new guest
def newcust():
    print '\nYou have selected the New Customer Option'
    return

# define function to handle the selection for a guest
def guestcust():
    print '\nYou have selected the Guest Customer Option\n'
    print 'Welcome to "To Bean or Not to Bean!" where it is our goal to serve you the best beverages from our cauldrons!'
    return

# define function to handle when the selection is not 1, 2, or 3
def wrongnumber():
    print('\nPlease enter the appropriate number for your customer type: 1, 2, or 3. ')
    return

while selection >= 0:
    print color.BOLD + '<<=====================================================>>' + color.END
    print color.BOLD + '<<===                                               ===>>' + color.END
    print color.BOLD + '\n<<===             1. Returning Customer             ===>>' + color.END
    print color.BOLD + '\n<<===             2. New Customer                   ===>>' + color.END
    print color.BOLD + '\n<<===             3. Guest Customer                 ===>>' + color.END
    print color.BOLD + '\n<<===                                               ===>>' + color.END
    print color.BOLD + '<<=====================================================>>' + color.END

    selection = int(raw_input('\n\nPlease make the appropriate customer selection: '))

    try:
        if selection < 1 or selection > 3:
            selection = int(raw_input('Please select your customer type. It must be a number equal to 1, 2, or 3.  '))

        if selection == 1:
            returningcust()
            selection = - 1

        elif selection == 2:
            newcust()
            selection = - 1

        elif selection == 3:
            guestcust()
            selection = - 1

        else:
            wrongnumber()

    except ValueError:
        print ('Enter 1, 2, or 3!')
