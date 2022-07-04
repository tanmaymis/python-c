def simple_interest(p : int ,r:int ,t:int):
    return (p*r*t)/100

def compound_interest(p : int ,r:int ,t:int):
    return p*(1+r/100)**t

if __name__ ==  "__main__":
    p=1000
    r=5
    t=3
    si =simple_interest(p,r,t)
    ci =compound_interest(p,r,t)
    print(f'simple interest is {si}')
    print(f'compond interest is {ci}')

    p =float(input("enter the principle :"))
    r =float(input("enter the rate of interest :"))
    t =float(input("enter the time :"))
    si =simple_interest(p,r,t)
    ci =compound_interest(p,r,t)
    print(f'simple interest is {si}')
    print(f'compond interest is {ci}')