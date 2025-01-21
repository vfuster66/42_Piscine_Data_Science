import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def calculate_confusion_matrix(predictions, truths):
    """
    Calcule la matrice de confusion entre les prédictions et les vérités
    terrain.
    """
    classes = list(set(truths))  # Classes uniques (par exemple Jedi et Sith)
    matrix = np.zeros((len(classes), len(classes)), dtype=int)

    class_to_index = {cls: i for i, cls in enumerate(classes)}
    for pred, truth in zip(predictions, truths):
        matrix[class_to_index[truth]][class_to_index[pred]] += 1

    return matrix, class_to_index


def calculate_metrics(confusion_matrix, class_to_index):
    """
    Calcule précision, rappel, score F1 et exactitude globale
    à partir de la matrice de confusion.
    """
    metrics = {}
    total_samples = np.sum(confusion_matrix)
    correct_predictions = np.trace(confusion_matrix)  # Diagonale

    accuracy = correct_predictions / total_samples

    for class_name, idx in class_to_index.items():
        tp = confusion_matrix[idx][idx]
        fn = np.sum(confusion_matrix[idx]) - tp
        fp = np.sum(confusion_matrix[:, idx]) - tp
        tn = total_samples - tp - fn - fp

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1_score = (2 * precision * recall) / (precision + recall) \
            if (precision + recall) > 0 else 0

        metrics[class_name] = {
            "Precision": precision,
            "Recall": recall,
            "F1-Score": f1_score,
            "Total": tp + fn
        }

    return metrics, accuracy


def display_confusion_matrix(confusion_matrix, class_to_index):
    """
    Affiche la matrice de confusion sous forme de heatmap.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="viridis",
                xticklabels=class_to_index.keys(),
                yticklabels=class_to_index.keys())
    plt.xlabel("Prédictions")
    plt.ylabel("Vérités terrain")
    plt.title("Matrice de Confusion")
    plt.show()


# Charger les fichiers
with open("predictions.txt", "r") as f:
    predictions = [line.strip() for line in f]

with open("truth.txt", "r") as f:
    truths = [line.strip() for line in f]

# Calcul de la matrice de confusion
confusion_matrix, class_to_index = calculate_confusion_matrix(
    predictions, truths)

# Calcul des métriques
metrics, accuracy = calculate_metrics(confusion_matrix, class_to_index)

# Affichage des résultats
print("Matrice de confusion :")
print(confusion_matrix)

print("\nMétriques :")
for class_name, values in metrics.items():
    print(f"{class_name}: Précision={values['Precision']:.2f}, "
          f"Rappel={values['Recall']:.2f}, "
          f"F1-Score={values['F1-Score']:.2f}, "
          f"Total={values['Total']}")

print(f"\nExactitude globale : {accuracy:.2f}")

# Affichage graphique
display_confusion_matrix(confusion_matrix, class_to_index)
