from example1 import ci_calc, si_calc

choice =input("what you want to calculate ? (ci/si)")
if choice == 'si':
    si_calc()
elif choice == 'ci':
    ci_calc()
else:
    print("invalid choice")