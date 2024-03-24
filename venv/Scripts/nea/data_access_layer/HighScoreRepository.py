import csv
import os.path

def read_highscore_from_file(filename):
    high_scores = dict()
    if os.path.exists(filename):
        with open(filename, 'r') as csv_file:
            spreadsheet = csv.DictReader(csv_file)
            for row in spreadsheet:
                # convert the score column to an integer
                player_name = row['player_name']
                score = int(row['score'])
                high_scores[player_name] = score
                print(player_name + " " + str(score))
    return high_scores

def write_highscore_to_file(file_name, player_name, score):
    if not os.path.exists(file_name):
        print("File does not exist: " + file_name)
        with open(file_name, 'w') as csvfile:
            fieldnames = ['player_name', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'player_name': player_name, 'score': score})
    else:
        print("File exists: " + file_name)
        with open(file_name, 'a') as csvfile:
            fieldnames = ['player_name', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'player_name': player_name, 'score': score})
