lines = 6
i = 1
while (i <= lines):
    j = 1
    while j < i:
        print("*", end=" ")
        j += 1
    print()
    i += 1  


    rows = 5  # Number of rows for the pattern

# Outer loop for rows
i = 1
while i <= rows:
    # Inner loop for printing stars in each row
    j = 1
    while j <= i:
        print("*", end=" ")  # Print a star and a space without a newline
        j += 1
    print()  # Move to the next line after printing stars for the current row
    i += 1