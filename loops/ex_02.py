picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

# Loop over the above list 
# print " " when encounters a "0"
# print "*" when encounters "1"

for row in picture:
    for col in row:
        if col == 0:
            print(" ", end="")
        elif col == 1:
            print("*", end="")
            
    print("")


            