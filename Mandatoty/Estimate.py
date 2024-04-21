import csv

def estimate_price():
    try:
        data_mileage = []

        with open('data.csv', newline='') as data_file:
            reader = csv.reader(data_file)
            next(reader) 
            for row in reader:
                data_mileage.append(int(row[0]))

        try:
            with open('theta.csv', newline='') as theta_file:
                reader = csv.reader(theta_file)
                first_row = next(reader)
                theta0 = float(first_row[0])
                theta1 = float(first_row[1])
        except:
            theta0 = 0
            theta1 = 0

        mileage = int(input("Enter the mileage: "))

        moyenne_mileage = sum(data_mileage) / len(data_mileage)
        ecart_type_mileage = 0
        for value in data_mileage:
            ecart_type_mileage += (value - moyenne_mileage) ** 2
        ecart_type_mileage = (ecart_type_mileage / len(data_mileage)) ** 0.5
        mileage_normalise = (mileage - moyenne_mileage) / ecart_type_mileage
        print("\nThe estimated price is: ", theta0 + (theta1 * mileage_normalise))

    except:
        print("\nInvalid number")
        estimate_price() 

estimate_price()