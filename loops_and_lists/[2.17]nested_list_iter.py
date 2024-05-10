# Exercise 2.17

# Defining a nested list with elements grouped into sublists.
q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

# Iterating over each sublist in the nested list.
for sublist in q:
    # Iterating over each element in the current sublist by index.
    for j in range(len(sublist)):
        # Printing the element followed by a space instead of a newline.
        print(sublist[j], end=' ')
    # Printing a newline after each sublist to separate them visually.
    print()

