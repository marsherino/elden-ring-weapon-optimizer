import csv
### define a function that opens up the two csv files, one function for each dictionary, and they parse stuff
### goal: get data in the same format that it's in in the weapon_optimizer file lns. 608-656
### rename the csv files to something normal - this saves a lot of effort

def get_weapon_damage():
  output = {}
  with open('file_name.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
      # Get info from row