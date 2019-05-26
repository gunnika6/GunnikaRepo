csvcut -c 15,17 flightdelays.csv | csvgrep -c 2 -m "SFO"  | head -n 4 > first3sfo.csv
csvlook first3sfo.csv
cut -d',' -f18 flightdelays.csv | sort | uniq -c | sort -n -r | head -n 3 | csvlook -H
