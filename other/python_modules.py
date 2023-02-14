import glob
import csv
import shutil
import webbrowser
#
#  ___________________glob experiment
# myfiles =glob.glob("../files/*.txt")
#
# for filepath in myfiles:
#     with open(filepath, 'r') as file:
#         content = file.read()
#         if not content:
#             print(f"'{filepath}':\n Empty.")
#         else:
#             print(f"'{filepath}':\n{content}")

# ___________________csv experiment

# with open("../files/weather.csv", 'r') as file:
#     data = list(csv.reader(file))

# with open("../files/weather.csv", 'w') as file:
#     csv_writer = csv.writer(file)
#     for row in data:
#         csv_writer.writerow(row)

# city = input("Enter a city:").strip()
#
# for row in data[1:]:
#     if row[0] == city:
#         print(f"{city} : {row[1]}")

# ___________________shutil experiment

shutil.make_archive("../files/output", "zip", "../files")

# ___________________webbrowser experiment

user_term = input("Enter a search term: ")

webbrowser.open("https://www.google.com/search?q="+user_term)
