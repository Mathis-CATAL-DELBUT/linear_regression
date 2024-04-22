import csv

def normalise_mileage(data_mileage, mileage):
    average_mileage = sum(data_mileage) / len(data_mileage)
    standard_deviation_mileage = 0
    for value in data_mileage:
        standard_deviation_mileage += (value - average_mileage) ** 2
    standard_deviation_mileage = (standard_deviation_mileage / len(data_mileage)) ** 0.5
    return (mileage - average_mileage) / standard_deviation_mileage

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

        print("\nThe estimated price is: ", theta0 + (theta1 * normalise_mileage(data_mileage, mileage)), " $")

    except:
        print("\nInvalid number")
        estimate_price() 

estimate_price()