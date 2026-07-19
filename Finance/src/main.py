import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, confusion_matrix, classification_report
)

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

pd.set_option("display.max_columns", None)



df = pd.read_csv("credit_data.csv")

# Drop stray index column if present (common in this dataset)
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

print(df.shape)
df.head()




df.info()





df.describe().T



missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100

missing_df = pd.DataFrame({
    "Missing Count": missing,
    "Missing %": missing_pct
}).sort_values("Missing %", ascending=False)

missing_df[missing_df["Missing Count"] > 0]




plt.figure(figsize=(10, 5))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap (Before Cleaning)")
plt.show()



print(df["SeriousDlqin2yrs"].value_counts())
print(df["SeriousDlqin2yrs"].value_counts(normalize=True) * 100)

plt.figure(figsize=(6, 4))
sns.countplot(x="SeriousDlqin2yrs", data=df, palette="Set2")
plt.title("Target Class Distribution: SeriousDlqin2yrs")
plt.xlabel("Delinquent (1) vs Not (0)")
plt.show()




print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Shape after dropping duplicates:", df.shape)



fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.boxplot(y=df["age"], ax=axes[0, 0])
axes[0, 0].set_title("Age Distribution")

sns.boxplot(y=df["DebtRatio"], ax=axes[0, 1])
axes[0, 1].set_title("DebtRatio Distribution")

sns.boxplot(y=df["MonthlyIncome"], ax=axes[1, 0])
axes[1, 0].set_title("MonthlyIncome Distribution")

sns.boxplot(y=df["NumberOfTimes90DaysLate"], ax=axes[1, 1])
axes[1, 1].set_title("NumberOfTimes90DaysLate Distribution")

plt.tight_layout()
plt.show()





# Age of 0 or negative is invalid in this dataset
print("Invalid ages:", (df["age"] <= 0).sum())
df = df[df["age"] > 0]

# Values like 96/98 in the "past due" columns are known data errors in this dataset
late_cols = ["NumberOfTime30-59DaysPastDueNotWorse",
             "NumberOfTime60-89DaysPastDueNotWorse",
             "NumberOfTimes90DaysLate"]

for col in late_cols:
    print(col, "unique high values:", sorted(df[col].unique())[-5:])





# Cap/replace known error codes (96, 98) with the column median
for col in late_cols:
    df.loc[df[col] >= 90, col] = df[col].median()




df["MonthlyIncome"] = df["MonthlyIncome"].fillna(df["MonthlyIncome"].median())
df["NumberOfDependents"] = df["NumberOfDependents"].fillna(df["NumberOfDependents"].mode()[0])

# Confirm no missing values remain
df.isnull().sum()




plt.figure(figsize=(10, 5))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap (After Cleaning)")
plt.show()




def cap_outliers(series, factor=1.5):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR
    return series.clip(lower=lower, upper=upper)

df["DebtRatio"] = cap_outliers(df["DebtRatio"])
df["MonthlyIncome"] = cap_outliers(df["MonthlyIncome"])




# Total past-due incidents combined
df["TotalPastDue"] = (
    df["NumberOfTime30-59DaysPastDueNotWorse"] +
    df["NumberOfTime60-89DaysPastDueNotWorse"] +
    df["NumberOfTimes90DaysLate"]
)

# Income per dependent (avoid divide by zero)
df["IncomePerDependent"] = df["MonthlyIncome"] / (df["NumberOfDependents"] + 1)

# Age bracket / life stage
df["AgeGroup"] = pd.cut(
    df["age"],
    bins=[0, 25, 35, 45, 55, 65, 100],
    labels=["<25", "25-34", "35-44", "45-54", "55-64", "65+"]
)

# Debt burden flag
df["HighDebtRatio"] = (df["DebtRatio"] > df["DebtRatio"].median()).astype(int)

df.head()




df = pd.get_dummies(df, columns=["AgeGroup"], drop_first=True)
df.head()




plt.figure(figsize=(12, 8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=False, cmap="coolwarm", center=0)
plt.title("Feature Correlation Heatmap")
plt.show()
# Correlation with target specifically
corr["SeriousDlqin2yrs"].sort_values(ascending=False)


fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.histplot(df["age"], bins=30, kde=True, ax=axes[0])
axes[0].set_title("Age Distribution")

sns.histplot(df["MonthlyIncome"], bins=30, kde=True, ax=axes[1])
axes[1].set_title("Monthly Income Distribution (After Capping)")

plt.tight_layout()
plt.show()
fig = px.box(
    df, x="SeriousDlqin2yrs", y="DebtRatio",
    title="DebtRatio by Delinquency Status",
    labels={"SeriousDlqin2yrs": "Delinquent"}
)
fig.show()


X = df.drop(columns=["SeriousDlqin2yrs"])
y = df["SeriousDlqin2yrs"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(X_train.shape, X_test.shape)



scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)



log_reg = LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42)
log_reg.fit(X_train_scaled, y_train)

y_pred_lr = log_reg.predict(X_test_scaled)
y_proba_lr = log_reg.predict_proba(X_test_scaled)[:, 1]

print("Logistic Regression Results")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print("Precision:", precision_score(y_test, y_pred_lr))
print("Recall:", recall_score(y_test, y_pred_lr))
print("F1:", f1_score(y_test, y_pred_lr))
print("ROC-AUC:", roc_auc_score(y_test, y_proba_lr))



rf = RandomForestClassifier(
    n_estimators=200, max_depth=8, class_weight="balanced", random_state=42
)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)
y_proba_rf = rf.predict_proba(X_test)[:, 1]

print("Random Forest Results")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Precision:", precision_score(y_test, y_pred_rf))
print("Recall:", recall_score(y_test, y_pred_rf))
print("F1:", f1_score(y_test, y_pred_rf))
print("ROC-AUC:", roc_auc_score(y_test, y_proba_rf))



fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.heatmap(confusion_matrix(y_test, y_pred_lr), annot=True, fmt="d", cmap="Blues", ax=axes[0])
axes[0].set_title("Logistic Regression - Confusion Matrix")
axes[0].set_xlabel("Predicted")
axes[0].set_ylabel("Actual")

sns.heatmap(confusion_matrix(y_test, y_pred_rf), annot=True, fmt="d", cmap="Greens", ax=axes[1])
axes[1].set_title("Random Forest - Confusion Matrix")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")

plt.tight_layout()
plt.show()


fpr_lr, tpr_lr, _ = roc_curve(y_test, y_proba_lr)
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_proba_rf)

plt.figure(figsize=(8, 6))
plt.plot(fpr_lr, tpr_lr, label=f"Logistic Regression (AUC = {roc_auc_score(y_test, y_proba_lr):.3f})")
plt.plot(fpr_rf, tpr_rf, label=f"Random Forest (AUC = {roc_auc_score(y_test, y_proba_rf):.3f})")
plt.plot([0, 1], [0, 1], "k--", label="Random Guess")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend()
plt.show()



cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

lr_cv_scores = cross_val_score(log_reg, X_train_scaled, y_train, cv=cv, scoring="roc_auc")
rf_cv_scores = cross_val_score(rf, X_train, y_train, cv=cv, scoring="roc_auc")

print("Logistic Regression CV ROC-AUC scores:", lr_cv_scores)
print("Mean:", lr_cv_scores.mean(), "Std:", lr_cv_scores.std())

print("\nRandom Forest CV ROC-AUC scores:", rf_cv_scores)
print("Mean:", rf_cv_scores.mean(), "Std:", rf_cv_scores.std())



importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=importances.values[:10], y=importances.index[:10])
plt.title("Top 10 Feature Importances (Random Forest)")
plt.xlabel("Importance")
plt.show()



print("Logistic Regression:\n", classification_report(y_test, y_pred_lr))
print("Random Forest:\n", classification_report(y_test, y_pred_rf))
