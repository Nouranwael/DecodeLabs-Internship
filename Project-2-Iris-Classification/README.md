# 🤖 Project 2: Data Classification Using AI
**DecodeLabs — Week 2 Internship Project**

---

## 📌 Overview

This project implements a complete **Supervised Learning pipeline** for data classification using the **K-Nearest Neighbors (KNN)** algorithm on the classic **Iris Benchmark Dataset**. It covers the full journey from raw data to intelligent decision-making, following the IPO (Input → Process → Output) framework.

---

## 🎯 Goal

Build a basic classification model that can identify the species of an Iris flower based on its physical measurements, and evaluate the model using proper metrics beyond simple accuracy.

---

## 📁 Project Structure

```
project-2/
│
├── iris_classification.py   # Main script (full pipeline)
├── iris_results.png         # Output charts (Elbow, Confusion Matrix, Scatter)
└── README.md                # This file
```

---

## 🗂️ Dataset: The Iris Benchmark

| Property   | Value                              |
|------------|------------------------------------|
| Samples    | 150 (Balanced — 50 per class)      |
| Classes    | 3 (Setosa, Versicolor, Virginica)  |
| Features   | 4 (Sepal Length, Sepal Width, Petal Length, Petal Width) |
| Source     | `sklearn.datasets.load_iris()`     |

---

## ⚙️ Pipeline (IPO Framework)

```
INPUT                  PROCESS                  OUTPUT
─────────────────      ──────────────────────   ──────────────────
Iris Dataset      →    Train-Test Split (80/20)  →  Confusion Matrix
Feature Scaling        KNN Algorithm             →  F1 Score
StandardScaler         Elbow Method (Best K)         Classification Report
```

---

## 🧠 Algorithm: K-Nearest Neighbors (KNN)

KNN is based on the **Proximity Principle** — similar data points exist in close proximity in feature space. For a new data point, the algorithm:

1. Calculates the distance to all training points
2. Selects the **K nearest neighbors**
3. Assigns the class by **majority vote**

```python
model = KNeighborsClassifier(n_neighbors=optimal_k)  # INSTANTIATE
model.fit(X_train, y_train)                           # FIT
predictions = model.predict(X_test)                  # PREDICT
```

> ⚠️ **K=1** → Overfitting (Noise) | **K=100** → Underfitting (Generic)  
> ✅ Use the **Elbow Method** to find the optimal K with the lowest error rate.

---

## 🔧 Installation

Make sure you have **Python 3.8+** installed, then run:

```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```

---

## 🚀 How to Run

```bash
python iris_classification.py
```

The script will:
- Print a step-by-step log in the terminal
- Display and save `iris_results.png` with 3 charts

---

## 📊 Results

| Metric      | Value   |
|-------------|---------|
| Accuracy    | 100.00% |
| F1 Score    | 1.0000  |
| Optimal K   | 1       |

### Classification Report

```
              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         9
   virginica       1.00      1.00      1.00        11
    accuracy                           1.00        30
```

---

## 📈 Output Charts

| Chart | Description |
|-------|-------------|
| **Elbow Curve** | Error rate vs K value — used to select optimal K |
| **Confusion Matrix** | TP / FP / FN / TN breakdown per class |
| **Feature Scatter** | Petal Length vs Petal Width showing class separation |

---

## 🛠️ Key Concepts Covered

- **Supervised Learning** vs Heuristic (rule-based) approaches
- **Feature Scaling** with `StandardScaler` (Mean=0, Variance=1)
- **Train-Test Split** with shuffle to remove order bias
- **The Accuracy Mirage** — why F1 Score matters for imbalanced data
- **Precision vs Recall trade-off** and the F1 harmonic mean
- **Confusion Matrix** — TP, FP (Type I), FN (Type II), TN

---

## 📦 Dependencies

| Library       | Purpose                        |
|---------------|--------------------------------|
| `scikit-learn`| ML algorithms & metrics        |
| `pandas`      | Data loading & exploration     |
| `numpy`       | Numerical operations           |
| `matplotlib`  | Plotting charts                |
| `seaborn`     | Confusion matrix heatmap       |

---

## 🔭 What's Next

After mastering tabular classification with KNN, the next step is:

> **Deep Learning & CNNs** — From Tabular Data → Computer Vision

---
