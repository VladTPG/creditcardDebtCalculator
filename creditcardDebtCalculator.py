#Calculator for the smallest monthly fee to fully pay the credit card debt in 12 months

annualInterestRate = 0
balance = 0
def getInput(data,message,errorMessage):
    validInput = True
    while(validInput):
        try:
            data = float(input(message))
            validInput = False
        except:
            print(errorMessage)  
    return data

annualInterestRate = getInput(annualInterestRate,"Please insert the annual interest rate as shown here (0.2, 0.3, etc) : ", "Please enter the value like in the example") 

monthinterest = annualInterestRate/12

balance = getInput(balance, "Please enter the debt amount: ", "Invalid Value")

copy_balance = balance

low = balance / 12

high = (balance*(1+monthinterest)**12)/12
guess = (low + high) / 2

while True:
    guess = (low + high) / 2
    for n in range(12):
        unpaid_bal = balance - guess
        balance = unpaid_bal + unpaid_bal*monthinterest
    if balance > 0.1:
        low = guess
    if balance < -0.01:
        high = guess
    if balance > -0.01 and balance < 0.1:
        break   
    balance = copy_balance
print(round(guess,2))