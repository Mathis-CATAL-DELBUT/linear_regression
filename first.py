import csv
import numpy as np ####################### !!!!!!!!!!!!!!!! A ENLEVER !!!!!!!!!!!!!!!! #######################

def estimate_price_menu(theta0, theta1, data_mileage_2):
    try:
        data_mileage = []
        data_price = []

        with open('data.csv', newline='') as data_file:
            reader = csv.reader(data_file)
            next(reader) 
            for row in reader:
                data_mileage.append(int(row[0]))
                data_price.append(int(row[1]))

        mileage = int(input("Enter the mileage: "))

        moyenne_mileage = sum(data_mileage) / len(data_mileage)
        ecart_type_mileage = (sum([(x - moyenne_mileage) ** 2 for x in data_mileage]) / len(data_mileage)) ** 0.5
        kilométrage_normalisé = (mileage - moyenne_mileage) / ecart_type_mileage
        
        print("\nThe estimated price is: ", estimate_price(theta0, theta1, kilométrage_normalisé))
    except:
        print("\nInvalid number")
        estimate_price_menu(theta0, theta1) 

def estimate_price(theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)

def normalise(data):
    mean = sum(data) / len(data)
    dif_edge = []
    for value in data:
        dif_edge.append((value - mean) ** 2)
    mean_dif_edge = sum(dif_edge) / len(dif_edge)
    ecart_type = np.sqrt(mean_dif_edge)

    for i in range(len(data)):
        data[i] = (data[i] - mean) / ecart_type
    
    return data

def learn(theta0, theta1, learning_rate, data_mileage, data_price):

    tmp0 = theta0
    tmp1 = theta1
    learn_again = 1

    data_mileage_normalise = normalise(data_mileage)

    while (learn_again < 10000):

        sumT0 = 0
        sumT1 = 0
        m = len(data_mileage)

        for i in range(m):
            sumT0 += (estimate_price(tmp0, tmp1, data_mileage_normalise[i]) - data_price[i])
            sumT1 += (estimate_price(tmp0, tmp1, data_mileage_normalise[i]) - data_price[i]) * data_mileage_normalise[i]

        d0 = (1 / m) * sumT0
        d1 = (1 / m) * sumT1

        tmp0 = tmp0 - learning_rate * d0
        tmp1 = tmp1 - learning_rate * d1
            
        learn_again += 1

    return tmp0, tmp1


def main():
    theta0 = 0
    theta1 = 0
    learning_rate = 0.001
    data_mileage = []
    data_price = []

    with open('data.csv', newline='') as data_file:
        reader = csv.reader(data_file)
        next(reader) 
        for row in reader:
            data_mileage.append(int(row[0]))
            data_price.append(int(row[1]))

    while True:
        print("\n============= MENU =============\n")
        print("1 : Estimate Price")
        print("2 : Learn")
        print("3 : Change learning rate")
        print("4 : Display theta values")
        print("5 : Reset theta values")
        print("6 : Exit\n")
        try:
            nb = int(input("Enter a number: "))
            if nb == 1:
                estimate_price_menu(theta0, theta1, data_mileage)
            elif nb == 2:
                theta0, theta1 = learn(theta0, theta1, learning_rate, data_mileage, data_price)
                print("\nTheta values updated")
                print("Theta0: ", theta0)
                print("Theta1: ", theta1)
            elif nb == 3:
                learning_rate = float(input("\nEnter the learning rate: "))
            elif nb == 4:
                print("\nTheta0: ", theta0)
                print("Theta1: ", theta1)
            elif nb == 5:
                theta0 = 0
                theta1 = 0
                print("\nTheta values reset")
            elif nb == 6:
                print("Exit")
                break
            else:
                print("\nInvalid number")
                continue
        except:
            print("\nInvalid number")
            continue
    print("\nEnd of the program")

main()