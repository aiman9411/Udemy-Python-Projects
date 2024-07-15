import pandas as pd

# Load the CSV file and create a dictionary
data = pd.read_csv("nato.csv")
nato_dict = dict(zip(data['letter'], data['code']))

# Get user input
while True:
    word = input("Enter a word:\n").upper()
    new_list = []
    try:
        for letter in word:
            new_list.append(nato_dict[letter])
        break
    except KeyError:
        print("Please input letters only")
print(new_list)
