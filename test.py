import numpy as np

def entrainer_regression_lineaire(X, y, taux_apprentissage=0.01, epochs=1000):
    """
    Entraîne un modèle de régression linéaire.

    Arguments :
        X : numpy.array
            Les caractéristiques (features) d'entraînement.
        y : numpy.array
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
    m = len(X)  # Nombre d'exemples dans l'ensemble de données
    theta0 = 0  # Initialisation de theta0
    theta1 = 0  # Initialisation de theta1

    # Entraînement du modèle
    for _ in range(epochs):
        predictions = theta0 + theta1 * X  # Calcul des prédictions
        erreur = predictions - y  # Calcul de l'erreur
        gradient_theta0 = (1 / m) * np.sum(erreur)  # Calcul du gradient pour theta0
        gradient_theta1 = (1 / m) * np.sum(erreur * X)  # Calcul du gradient pour theta1
        theta0 -= taux_apprentissage * gradient_theta0  # Mise à jour de theta0
        theta1 -= taux_apprentissage * gradient_theta1  # Mise à jour de theta1

    return theta0, theta1

def normaliser(X):
    """
    Normalise les caractéristiques en soustrayant la moyenne et en divisant par l'écart-type.

    Arguments :
        X : numpy.array
            Les caractéristiques à normaliser.

    Returns :
        X_normalise : numpy.array
            Les caractéristiques normalisées.
    """
    return (X - np.mean(X)) / np.std(X)

def main():
    # Chargement des données
    data = np.loadtxt("data.csv", delimiter=",", skiprows=1)

    # Séparation des caractéristiques (kilométrage) et des étiquettes (prix)
    X = data[:, 0]
    y = data[:, 1]

    # Normalisation des caractéristiques
    X_normalise = normaliser(X)

    # Entraînement du modèle de régression linéaire
    theta0, theta1 = entrainer_regression_lineaire(X_normalise, y)

    # Affichage des paramètres appris
    print("theta0:", theta0)
    print("theta1:", theta1)

    # Sauvegarde des paramètres dans un fichier pour une utilisation future
    np.savetxt("parameters.txt", [theta0, theta1])

    # Utilisation du modèle entraîné pour prédire le prix pour un kilométrage donné
    while True:
        try:
            kilométrage = float(input("Entrez le kilométrage: "))
            break
        except ValueError:
            print("Veuillez entrer une valeur numérique valide.")

    # Normalisation du kilométrage avant la prédiction
    kilométrage_normalisé = (kilométrage - np.mean(X)) / np.std(X)
    prix_estimé = theta0 + theta1 * kilométrage_normalisé
    print("Prix estimé:", prix_estimé)

if __name__ == "__main__":
    main()
