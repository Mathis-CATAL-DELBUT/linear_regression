import csv

def estimate_price(theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)

def normalise_mileage(data_mileage, mileage):
    average_mileage = sum(data_mileage) / len(data_mileage)
    standard_deviation_mileage = 0
    for value in data_mileage:
        standard_deviation_mileage += (value - average_mileage) ** 2
    standard_deviation_mileage = (standard_deviation_mileage / len(data_mileage)) ** 0.5
    return (mileage - average_mileage) / standard_deviation_mileage


def learn(theta0, theta1, learning_rate, data_mileage, data_price):

    learn_again = 1

    data_mileage_normalise = []
    for i in range(len(data_mileage)):
        data_mileage_normalise.append(normalise_mileage(data_mileage, data_mileage[i]))

    while (learn_again < 10000):

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

    theta0, theta1 = learn(theta0, theta1, learning_rate, data_mileage, data_price)
    with open('theta.csv', 'w', newline='') as theta_file:
        writer = csv.writer(theta_file)
        writer.writerow([theta0, theta1])

main()