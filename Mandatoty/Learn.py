import csv

def estimate_price(theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)

def normalise(data):
    mean = sum(data) / len(data)
    # la somme des carrés des différences par rapport à la moyenne
    sum_squares_diff = 0
    for value in data:
        sum_squares_diff += (value - mean) ** 2

    # écart-type
    standard_deviation = (sum_squares_diff / len(data)) ** 0.5

    # Normalisation 
    normalised_data = []
    for value in data:
        normalised_data.append((value - mean) / standard_deviation)

    return normalised_data


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

    theta0, theta1 = learn(theta0, theta1, learning_rate, data_mileage, data_price)
    with open('theta.csv', 'w', newline='') as theta_file:
        writer = csv.writer(theta_file)
        writer.writerow([theta0, theta1])

main()