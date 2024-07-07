import pandas as pd

word = input("Enter a word:\n").upper()
letters = list(word)
new_list = []

data = pd.read_csv("nato.csv")
for letter in letters:
    for index, row in data.iterrows():
        if letter == row["letter"]:
            new_list.append(row["code"])

print(new_list)