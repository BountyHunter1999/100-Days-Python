row1 = ["-","-", "-" ]
row2 = ["-","-", "-" ]
row3 = ["-","-", "-" ]

rows = [row1, row2, row3]

def show_map(rows):
    for row in rows:
        print(row)

show_map(rows)

treasure_location = input("enter the location of the treasure:")
row = int(treasure_location[0]) -1
col = int(treasure_location[1]) -1 

rows[row][col] = "X"

show_map(rows)
