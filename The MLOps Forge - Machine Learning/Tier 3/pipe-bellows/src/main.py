from pipeline import get_data, split_data, train_model, evaluate_and_save_artifacts

def main():
    """
    Main function to run the entire ML pipeline.
    """
    print("--- Starting ML Pipeline ---")

    # Step 1: Get Data
    X_data, y_data = get_data()

    # Step 2: Split Data
    X_train, X_test, y_train, y_test = split_data(X_data, y_data)

    # Step 3: Train Model
    model = train_model(X_train, y_train)

    # Step 4: Evaluate and Save Artifacts
    evaluate_and_save_artifacts(model, X_test, y_test)

    print("--- ML Pipeline Finished Successfully ---")

if __name__ == '__main__':
    main()