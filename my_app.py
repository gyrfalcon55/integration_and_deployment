import os

# create folder
os.makedirs("models", exist_ok=True)

# create dummy files
with open("models/model.pkl", "w") as f:
    f.write("dummy model data")

with open("models/metrics.json", "w") as f:
    f.write('{"accuracy": 0.95}')

print("Models and metrics generated!")