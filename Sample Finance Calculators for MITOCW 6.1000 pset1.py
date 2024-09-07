#Months required for a down payment
salary=float(input("Enter your yearly salary: "))
monthly_salary=float(salary/12)
housing_portion_salary=float(input("Enter the portion of your yearly salary meant for saving for the house in decimal form: "))
housing_cost=float(input("Enter how much the house costs: "))
portion_down=float(input("Enter the minimum down payment in decimal form: "))
amount_saved=0
invest_return=0.05
months=0
down_payment=float(housing_cost*portion_down)

while (down_payment>amount_saved):
    amount_saved=monthly_salary*housing_portion_salary+amount_saved*(1+(invest_return/12))
    months=months+1
print("Number of months:",months)

#Months required for a down payment with a raise
salary=float(input("Enter your yearly salary: "))
monthly_salary=float(salary/12)
sixmonth_raise=float(input("Enter your six month raise rate as a decimal: "))
housing_portion_salary=float(input("Enter the portion of your yearly salary meant for saving for the house in decimal form: "))
housing_cost=float(input("Enter how much the house costs: "))
portion_down=float(input("Enter the minimum down payment in decimal form: "))
amount_saved=0
invest_return=0.05
months=0
down_payment=float(housing_cost*portion_down)

while (down_payment>amount_saved):
    amount_saved=monthly_salary*housing_portion_salary+amount_saved*(1+(invest_return/12))
    months=months+1
    if months%6==0:
        monthly_salary*=1+sixmonth_raise

print("Number of months:",months)

#Compounding interest rate necessary for a down payment with an initial investment within n months
home_cost=800000
down_percentage=.25
down_payment=(home_cost*down_percentage)
print(down_payment)
months=float(input("How many months will you invest for: "))
initial=float(input("What is your initial investment: "))
low=0
high=1
r=(high+low)/2
steps=0
while abs(down_payment-initial*(1+(r/12))**months)>100:
    if (initial>=down_payment): #initial investment is more than required
        r=0
        break
    elif ((initial*(1+(1/12))**months)<down_payment): #initial investment will not earn enough interest within the selected term
        r=None
        break
    if (initial*(1+(r/12))**months>down_payment): #bisection search to find minimum necessary
        high=r
    else:
        low=r
    r=(high+low)/2
    steps+=1
print("Minimum necessary return on investment through term (percentage): ", r*100)
print("Steps of bisection search:",steps)