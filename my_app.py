import os

os.mkdir('results')
with open("results/output.txt", "w") as f:
    f.write("This is my artifact file")