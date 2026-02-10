import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# ----------------------------
# Load dataset
# ----------------------------
df = pd.read_csv('../data/raw/heart.csv')

# ----------------------------
# Dataset inspection
# ----------------------------
print("=== Dataset Info ===")
print(df.info())
print("\n=== Dataset Shape ===")
print(df.shape)

# Check missing values
print("\n=== Missing Values Per Column ===")
print(df.isnull().sum())

# Check duplicate rows
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# Print number of unique values per column
print("\n=== Unique Values Per Column ===")
for col in df.columns:
    print(f"{col}: {df[col].nunique()}")

# ----------------------------
# Separate features (X) and target (y)
# Keep X as a DataFrame so ColumnTransformer can use column names
# ----------------------------
X = df.iloc[:, :-1]  # all columns except target
y = df.iloc[:, -1]   # target column

# ----------------------------
# Define feature types
# ----------------------------
binary_features = ['sex', 'fbs', 'exang']                 # Two-state features (0/1)
categorical_ordinal_features = ['slope', 'ca']           # Ordered categories, distance not meaningful
categorical_nominal_features = ["cp", "restecg", "thal"] # Unordered categories
continuous_features = ["age", "trestbps", "chol", "thalach", "oldpeak"] # Measurements with meaningful numeric differences

# ----------------------------
# Pipelines per feature type
# ----------------------------

# 1️⃣ Continuous pipeline
# Strategy: median imputation (robust to outliers) + scaling
continuous_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),  # Replace missing with median
    ('scaler', StandardScaler())                     # Standardize to zero mean & unit variance
])

# 2️⃣ Binary pipeline
# Strategy: most frequent imputation (fill missing with 0 or 1)
binary_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent'))  # Preserve majority class
])

# 3️⃣ Ordinal categorical pipeline
# Strategy: most frequent imputation only (keep ordering intact)
ordinal_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent'))  # Fill missing with most common level
])

# 4️⃣ Nominal categorical pipeline
# Strategy: most frequent imputation + one-hot encoding
categorical_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Fill missing with most common category
    ('onehot', OneHotEncoder(handle_unknown='ignore'))     # Convert categories to binary columns
])

# ----------------------------
# Combine pipelines using ColumnTransformer
# ----------------------------
preprocessor = ColumnTransformer(transformers=[
    ('continuous', continuous_pipeline, continuous_features),
    ('binary', binary_pipeline, binary_features),
    ('ordinal', ordinal_pipeline, categorical_ordinal_features),
    ('nominal', categorical_pipeline, categorical_nominal_features)
])

# ----------------------------
# Encode target variable (if it's non-numeric)
# ----------------------------
if y.dtype == object:
    le = LabelEncoder()
    y = le.fit_transform(y)

# ----------------------------
# Split dataset
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# ----------------------------
# Fit and transform preprocessing pipeline
# ----------------------------
X_train_preprocessed = preprocessor.fit_transform(X_train)
X_test_preprocessed = preprocessor.transform(X_test)

print("\nPreprocessed training set shape:", X_train_preprocessed.shape)
print("Preprocessed test set shape:", X_test_preprocessed.shape)
