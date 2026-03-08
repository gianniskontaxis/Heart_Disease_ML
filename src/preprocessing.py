import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from pathlib import Path


def load_data():

    
    project_root = Path(__file__).resolve().parents[1]

    data_path = project_root / "data" / "raw" / "heart.csv"

    df = pd.read_csv(data_path)

    return df


def inspect_data(df):

    print("=== Dataset Info ===")
    print(df.info())

    print("\n=== Dataset Shape ===")
    print(df.shape)

    print("\n=== Missing Values Per Column ===")
    print(df.isnull().sum())

    duplicates = df.duplicated().sum()
    print(f"\nNumber of duplicate rows: {duplicates}")

    print("\n=== Unique Values Per Column ===")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()}")


def split_features_target(df):

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    return X, y


def build_preprocessor():

    binary_features = ['sex', 'fbs', 'exang']
    categorical_ordinal_features = ['slope', 'ca']
    categorical_nominal_features = ["cp", "restecg", "thal"]
    continuous_features = ["age", "trestbps", "chol", "thalach", "oldpeak"]

    continuous_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    binary_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent'))
    ])

    ordinal_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent'))
    ])

    categorical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ('continuous', continuous_pipeline, continuous_features),
        ('binary', binary_pipeline, binary_features),
        ('ordinal', ordinal_pipeline, categorical_ordinal_features),
        ('nominal', categorical_pipeline, categorical_nominal_features)
    ])

    return preprocessor


def encode_target(y):

    if y.dtype == object:
        le = LabelEncoder()
        y = le.fit_transform(y)

    return y


def split_data(X, y):

    return train_test_split(
        X, y, test_size=0.2, random_state=1
    )