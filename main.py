from src.preprocessing import (
    load_data,
    inspect_data,
    split_features_target,
    build_preprocessor,
    encode_target,
    split_data
)

from src.train_model import train_linear_regression, predict
from src.evaluate import evaluate_model


def main():

    # 1 Load dataset
    df = load_data()

    # 2 Inspect dataset
    inspect_data(df)

    # 3 Split X and y
    X, y = split_features_target(df)

    # 4 Encode target if needed
    y = encode_target(y)

    # 5 Train-test split
    X_train, X_test, y_train, y_test = split_data(X, y)

    # 6 Build preprocessing pipeline
    preprocessor = build_preprocessor()

    # 7 Fit preprocessing
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    # 8 Train model
    model = train_linear_regression(X_train_processed, y_train)

    # 9 Predictions
    y_pred = predict(model, X_test_processed)

    # 10 Evaluate
    evaluate_model(y_test, y_pred)


if __name__ == "__main__":
    main()