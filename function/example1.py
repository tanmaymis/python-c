#creation

def si_calc():
    p =float(input("enter the principle :"))
    r =float(input("enter the rate of interest :"))
    t =float(input("enter the time :"))
    si = p*(r*t)/100
    print(f'Simple interest is{si}')

#def is define function
def ci_calc():
    p =float(input("enter the principle :"))
    r =float(input("enter the rate of interest :"))
    t =float(input("enter the time :"))
    ci = p*(1+r/100)**t
    print(f'compound interest is{ci}')
#calling function
#si_calc()
#ci_calc()