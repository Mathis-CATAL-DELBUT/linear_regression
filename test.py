def entrainer_regression_lineaire(KM, y, taux_apprentissage=0.01, epochs=1000):
    """
    Entraîne un modèle de régression linéaire.

    Arguments :
        KM : list
            Les caractéristiques (features) d'entraînement.
        y : list
            Les étiquettes (labels) cibles.
        taux_apprentissage : float, optionnel
            Le taux d'apprentissage pour la descente de gradient.
        epochs : int, optionnel
            Le nombre d'itérations d'entraînement.

    Returns :
        theta0 : float
            Le paramètre theta0 (bias) appris.
        theta1 : float
            Le paramètre theta1 (pente) appris.
    """
    m = len(KM)  # Nombre d'exemples dans l'ensemble de données
    theta0 = 0  # Initialisation de theta0
    theta1 = 0  # Initialisation de theta1

    # Entraînement du modèle
    for _ in range(epochs):
        predictions = [theta0 + theta1 * x for x in KM]  # Calcul des prédictions
        erreur = [pred - label for pred, label in zip(predictions, y)]  # Calcul de l'erreur
        gradient_theta0 = (1 / m) * sum(erreur)  # Calcul du gradient pour theta0
        gradient_theta1 = (1 / m) * sum([err * x for err, x in zip(erreur, KM)])  # Calcul du gradient pour theta1
        theta0 -= taux_apprentissage * gradient_theta0  # Mise à jour de theta0
        theta1 -= taux_apprentissage * gradient_theta1  # Mise à jour de theta1

    return theta0, theta1

def normaliser(X):
    """
    Normalise les caractéristiques en soustrayant la moyenne et en divisant par l'écart-type.

    Arguments :
        X : list
            Les caractéristiques à normaliser.

    Returns :
        X_normalise : list
            Les caractéristiques normalisées.
    """
    moyenne_X = sum(X) / len(X)
    ecart_type_X = (sum([(x - moyenne_X) ** 2 for x in X]) / len(X)) ** 0.5
    return [(x - moyenne_X) / ecart_type_X for x in X]

def main():
    # Chargement des données
    with open("data.csv", "r") as file:
        lines = file.readlines()
        data = [list(map(float, line.strip().split(','))) for line in lines[1:]]

    # Séparation des caractéristiques (kilométrage) et des étiquettes (prix)
    X = [row[0] for row in data]
    y = [row[1] for row in data]

    # Normalisation des caractéristiques
    X_normalise = normaliser(X)

    # Entraînement du modèle de régression linéaire
    theta0, theta1 = entrainer_regression_lineaire(X_normalise, y)

    # Affichage des paramètres appris
    print("theta0:", theta0)
    print("theta1:", theta1)

    # Sauvegarde des paramètres dans un fichier pour une utilisation future
    with open("parameters.txt", "w") as file:
        file.write(f"{theta0}\n{theta1}")

    # Utilisation du modèle entraîné pour prédire le prix pour un kilométrage donné
    while True:
        try:
            kilométrage = float(input("Entrez le kilométrage: "))
            break
        except ValueError:
            print("Veuillez entrer une valeur numérique valide.")

    # Normalisation du kilométrage avant la prédiction
    moyenne_X = sum(X) / len(X)
    ecart_type_X = (sum([(x - moyenne_X) ** 2 for x in X]) / len(X)) ** 0.5
    kilométrage_normalisé = (kilométrage - moyenne_X) / ecart_type_X
    prix_estimé = theta0 + theta1 * kilométrage_normalisé
    print("Prix estimé:", prix_estimé)

if __name__ == "__main__":
    main()
