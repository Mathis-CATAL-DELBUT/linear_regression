import csv
import os
import matplotlib.pyplot as plt
from colorama import init, Fore

def clear_terminal():
    os.system('clear')

def scrap_data():
    data_mileage = []
    data_price = []

    with open('data.csv', newline='') as data_file:
        reader = csv.reader(data_file)
        next(reader) 
        for row in reader:
            data_mileage.append(int(row[0]))
            data_price.append(int(row[1]))
    
    return data_mileage, data_price

def normalise_mileage(data_mileage, mileage):
    average_mileage = sum(data_mileage) / len(data_mileage)
    standard_deviation_mileage = 0
    for value in data_mileage:
        standard_deviation_mileage += (value - average_mileage) ** 2
    standard_deviation_mileage = (standard_deviation_mileage / len(data_mileage)) ** 0.5
    return (mileage - average_mileage) / standard_deviation_mileage


def estimate_price_menu(theta0, theta1, data_mileage):
    try:
        if theta0 == 0 or theta1 == 0:
            print("\n⚠️ The program has not yet learned ⚠️\n")
        mileage = int(input("Enter the mileage: "))
        print("\nThe estimated price is: ", round(estimate_price(theta0, theta1, normalise_mileage(data_mileage, mileage)), 2), " $")

    except:
        print("\nInvalid number 🚫")
        estimate_price_menu(theta0, theta1) 

def estimate_price(theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)

def learn(theta0, theta1, learning_rate, data_mileage, data_price, learning_count):

    learn_again = 1

    data_mileage_normalise = []
    for i in range(len(data_mileage)):
        data_mileage_normalise.append(normalise_mileage(data_mileage, data_mileage[i]))

    while (learn_again < learning_count):
        tmp0 = theta0
        tmp1 = theta1

        sumT0 = 0
        sumT1 = 0
        m = len(data_mileage)

        for i in range(m):
            sumT0 += (estimate_price(tmp0, tmp1, data_mileage_normalise[i]) - data_price[i])
            sumT1 += (estimate_price(tmp0, tmp1, data_mileage_normalise[i]) - data_price[i]) * data_mileage_normalise[i]

        d0 = (1 / m) * sumT0
        d1 = (1 / m) * sumT1

        theta0 = tmp0 - learning_rate * d0
        theta1 = tmp1 - learning_rate * d1
            
        learn_again += 1

    return theta0, theta1

def precision(theta0, theta1, data_mileage, data_price):
    print("\n*****************************************************************************")
    print("*                   Precision of the model:                                 *")
    print("*****************************************************************************\n")
    sum_diff = 0
    for i in range(len(data_mileage)):
        estimate = estimate_price(theta0, theta1, normalise_mileage(data_mileage, data_mileage[i]))
        diff = abs(round(estimate * 100 / data_price[i] - 100, 2))
        sum_diff += diff
        print("Real price: ", data_price[i], " | Estimated price: ", round(estimate, 1), " | Difference: ", diff , " %")
    
    print("\nAverage difference: ", Fore.GREEN, round(sum_diff / len(data_mileage), 2), " %", Fore.RESET)

def print_graph(theta0, theta1, data_mileage, data_price, linear_regression):
    plt.scatter(data_mileage, data_price)

    predictions = []
    for i in range(len(data_mileage)):
        predictions.append(estimate_price(theta0, theta1, normalise_mileage(data_mileage, data_mileage[i])))
    if linear_regression == True:
        plt.plot(data_mileage, predictions, color='red', label='Linear Regression')
    plt.title('Linear Regression : Mileage vs Price')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.show()  


def main():
    theta0 = 0
    theta1 = 0
    learning_rate = 0.001
    learning_count = 10000
    data_mileage, data_price = scrap_data()

    init()

    while True:
        print("\n============= MENU =============\n")
        print("1 : Estimate Price 💲")
        print("2 : Learn 🧠")
        print("3 : Change learning rate 📚")
        print("4 : Change learning count 📊")
        print("5 : Display theta values 🖋️")
        print("6 : Reset theta values 🔄")
        print("7 : Precision 🎯")
        print("8 : Graph without linear regression 📈")
        print("9 : Graph with linear regression 📉")
        print("10 : Exit 🚪\n")
        try:
            nb = int(input("Enter a number: "))
            clear_terminal()
            if nb == 1:
                estimate_price_menu(theta0, theta1, data_mileage)
            elif nb == 2:
                theta0, theta1 = learn(theta0, theta1, learning_rate, data_mileage, data_price, learning_count)
                print("\nTheta values updated successfully ✅")
            elif nb == 3:
                learning_rate = float(input("\nEnter the learning rate: "))
                while (learning_rate <= 0 or learning_rate >= 1):
                    if learning_rate <= 0 or learning_rate >= 1:
                        print("\n⚠️ The learning rate must be between 0 and 1 ⚠️")
                    learning_rate = float(input("\nEnter the learning rate: "))
            elif nb == 4:
                learning_count = int(input("\nEnter the learning count: "))
                while (learning_count <= 0):
                    print("\n⚠️ The learning count must be greater than 0 ⚠️")
                    learning_count = int(input("\nEnter the learning count: "))
            elif nb == 5:
                print("\nTheta0: ", theta0)
                print("Theta1: ", theta1)
            elif nb == 6:
                theta0 = 0
                theta1 = 0
                print("\nTheta values reset ✅")
            elif nb == 7:
                precision(theta0, theta1, data_mileage, data_price)
            elif nb == 8:
                print_graph(theta0, theta1, data_mileage, data_price, False)
            elif nb == 9:
                print_graph(theta0, theta1, data_mileage, data_price, True)
            elif nb == 10:
                break
            else:
                print("\nInvalid number 🚫")
                continue
            input("\nPress Enter to continue...")
            clear_terminal()
        except:
            print("\nInvalid number 🚫")
            continue
    print("\nBye 👋")

main()