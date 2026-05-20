# ============================================================
#   DecodeLabs | Industrial Training Kit | Batch 2026
#   Project 2: Data Classification Using AI
#   Algorithm : K-Nearest Neighbors (KNN)
#   Dataset   : Iris Benchmark (150 samples, 3 classes, 4 features)
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score,
    accuracy_score,
)

# ── 1. LOAD & UNDERSTAND THE DATASET ────────────────────────
print("=" * 60)
print("  STEP 1 — RAW MATERIAL: THE IRIS BENCHMARK")
print("=" * 60)

iris = load_iris()
X = iris.data          # Features: sepal_length, sepal_width, petal_length, petal_width
y = iris.target        # Labels : 0=Setosa, 1=Versicolor, 2=Virginica

df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in y]

print(f"\nSamples   : {X.shape[0]}  (Balanced)")
print(f"Classes   : {len(iris.target_names)}  → {list(iris.target_names)}")
print(f"Dimensions: {X.shape[1]}  features")
print("\nFirst 5 rows:")
print(df.head())
print("\nClass distribution:")
print(df["species"].value_counts())

# ── 2. FEATURE SCALING (THE GATEKEEPER RULE) ────────────────
print("\n" + "=" * 60)
print("  STEP 2 — THE GATEKEEPER RULE: SCALING")
print("=" * 60)

# Split FIRST, then scale (to avoid data leakage)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)

scaler = StandardScaler()                    # Mean=0, Variance=1
X_train = scaler.fit_transform(X_train)      # Fit on train only
X_test  = scaler.transform(X_test)           # Apply same scale to test

print(f"\nTraining set : {X_train.shape[0]} samples  (80%)")
print(f"Test set     : {X_test.shape[0]}  samples  (20%)")
print("StandardScaler applied → Mean ≈ 0, Variance ≈ 1")

# ── 3. FIND THE OPTIMAL K (THE ELBOW METHOD) ────────────────
print("\n" + "=" * 60)
print("  STEP 3 — TUNING THE ENGINE: CHOOSING K")
print("=" * 60)

error_rates = []
k_range = range(1, 31)

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    error_rates.append(1 - accuracy_score(y_test, preds))

optimal_k = k_range[error_rates.index(min(error_rates))]
print(f"\nOptimal K (lowest error rate) → K = {optimal_k}")

# ── 4. TRAIN THE KNN MODEL ───────────────────────────────────
print("\n" + "=" * 60)
print("  STEP 4 — THE WORKFLOW: SCIKIT-LEARN")
print("=" * 60)

model = KNeighborsClassifier(n_neighbors=optimal_k)   # INSTANTIATE
model.fit(X_train, y_train)                            # FIT
predictions = model.predict(X_test)                   # PREDICT

print(f"\nmodel = KNeighborsClassifier(n_neighbors={optimal_k})")
print("model.fit(X_train, y_train)        → ✅ Model trained")
print("predictions = model.predict(X_test)→ ✅ Predictions made")

# ── 5. OUTPUT VALIDATION ─────────────────────────────────────
print("\n" + "=" * 60)
print("  STEP 5 — OUTPUT VALIDATION")
print("=" * 60)

accuracy = accuracy_score(y_test, predictions)
f1       = f1_score(y_test, predictions, average="weighted")

print(f"\nAccuracy : {accuracy * 100:.2f}%")
print(f"F1 Score : {f1:.4f}  (Weighted — Precision/Recall balance)")
print("\nDetailed Classification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))

# ── 6. VISUALIZATIONS ────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("DecodeLabs | Project 2: KNN Classification on Iris Dataset",
             fontsize=14, fontweight="bold", color="#1a3a5c")

# — Plot A: Error Rate vs K (Elbow Curve) —
axes[0].plot(k_range, error_rates, color="#1a3a5c", linewidth=2, marker="o", markersize=5)
axes[0].axvline(x=optimal_k, color="#e8500a", linestyle="--", linewidth=2,
                label=f"Optimal K={optimal_k}")
axes[0].set_title("Tuning the Engine: Choosing K", fontweight="bold")
axes[0].set_xlabel("K Value")
axes[0].set_ylabel("Error Rate")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# — Plot B: Confusion Matrix —
cm = confusion_matrix(y_test, predictions)
sns.heatmap(
    cm, annot=True, fmt="d", ax=axes[1],
    xticklabels=iris.target_names,
    yticklabels=iris.target_names,
    cmap="Blues", linewidths=0.5,
    annot_kws={"size": 13, "weight": "bold"},
)
axes[1].set_title("Diagnostic Tool: Confusion Matrix", fontweight="bold")
axes[1].set_xlabel("Predicted Label")
axes[1].set_ylabel("True Label")

# — Plot C: Feature Importance (Petal Length vs Petal Width) —
colors = ["#1a3a5c", "#e8500a", "#2ca02c"]
for cls_idx, cls_name in enumerate(iris.target_names):
    mask = y == cls_idx
    axes[2].scatter(
        X[mask, 2], X[mask, 3],
        label=cls_name, color=colors[cls_idx],
        alpha=0.7, edgecolors="white", linewidths=0.5, s=60,
    )
axes[2].set_title("Data Structure: Petal Features", fontweight="bold")
axes[2].set_xlabel("Petal Length (cm)")
axes[2].set_ylabel("Petal Width (cm)")
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("iris_results.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n" + "=" * 60)
print("  PROJECT 2 COMPLETE ✅")
print("=" * 60)
print(f"\n  Optimal K     : {optimal_k}")
print(f"  Accuracy      : {accuracy * 100:.2f}%")
print(f"  F1 Score      : {f1:.4f}")
print("\n  Chart saved   → iris_results.png")
print("  Pipeline      : Iris → StandardScaler → KNN → F1 + ConfusionMatrix")
print("=" * 60)
