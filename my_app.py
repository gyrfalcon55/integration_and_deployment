import argparse

def train(epochs, model):
    print(f"Training {model} model for {epochs} epochs...")
    
    # dummy logic
    for i in range(1, epochs + 1):
        print(f"Epoch {i}/{epochs} completed")

    print("Training completed successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--epochs", type=int, required=True)
    parser.add_argument("--model", type=str, required=True)

    args = parser.parse_args()

    train(args.epochs, args.model)