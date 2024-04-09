
def estimate_price(theta0, theta1):
    mileage = int(input("Enter the mileage: "))
    print("The estimated price is: ", theta0 + theta1 * mileage) 

def main():
    theta0 = 0
    theta1 = 0
    while True:
        print("\n============= MENU =============\n")
        print("1 : Estimate Price")
        print("2 : Learn")
        print("3 : Exit")
        nb = int(input("Enter a number: "))
        if nb == 1:
            estimate_price(theta0, theta1)
        elif nb == 2:
            print("Learn")
        elif nb == 3:
            print("Exit")
            break
        else:
            print("Invalid number")
            continue
    print("End of the program")

main()