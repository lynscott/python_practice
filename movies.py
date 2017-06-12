
import csv

with open("movies.csv","w",newline='') as f:
          w=csv.writer(f, delimiter=",")
          w.writerow(["Top Gun",
                      "Risky Business",
                      "Minority Report"])
          w.writerow(["Titanic",
                      "The Revanant",
                      "Inception"])
          w.writerow(["Training Day",
                      "Man on Fire",
                      "Flight"])
