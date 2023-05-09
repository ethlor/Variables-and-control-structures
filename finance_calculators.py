import math

# choose if user wants to invest a amount or a bond. choose what type of invetment, either compound or simple. then display the total amount over a given number of years.

# the \t is a tab and \n means a new line
# the double \t is there because a tab takes 8 spaces, investments takes up more than 8 spaces so if you add \t to it then another 8 spaces allocated for the tab. 
print("investment\t- to calculater the amount of interest you'll earn on your investment \nbond\t\t- to calculate amount youll have to pay on home loan\n")
choice = input("Enter either'investment' or 'bond' from the menu above to proceed: ")
# convert to lower case so its not case sensitive
choice = choice.lower()

# check the type of calcualtion to do
if choice == "investment":
    # enter the paramaters for calculation
    deposit = float(input("Enter deposit amount: "))
    interest_rate = float(input("Enter interest rate"))
    # interest rate is a percentage value/100
    interest_rate = interest_rate/100
    years = int(input("Enter number of years for investment: "))
    # check the type of investment to calculate for
    interest = input("Enter 'simple' or 'compund' for type of interest: ")
    if interest == "simple":
        # A = P(1 + r*t)
        total_amount = deposit * (1 + interest_rate * years)
        print("your total investment amount is R{}".format(round(total_amount,2)))
    else:
        # A = P(1 + r)**t
        total_amount = deposit * math.pow((1+interest_rate),years)
        print("your total investment amount is R{}".format(round(total_amount,2)))

# check the type of calcualtion to do
elif choice == "bond":
    # enter the paramaters for calculation
    house_value = float(input("Enter present value of house: "))
    interest_rate = float(input("Enter interst rate: "))
    # monthly interest rate is (i/100) / 12 
    irate = (interest_rate /100 ) / 12
    months = int(input("Enter amountof months on bond:"))
    # (i*P)/(1-(1+i)**(-n))
    repay_amount = (irate * house_value)/ (1-(1+irate)**(-months))
    print("your monthly repaying amount is R{}".format(round(repay_amount,2)))

# if an invalid entery was inserted taht dont math the above critera it comes here
else:
    print("You have entered an invalid option. Please restart and try again.")
