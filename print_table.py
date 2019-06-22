def print_table(table_data):
    # passing a list of lists of strings, then print well-organized table
    # with each column right-justified.
    col_widths = []
    for i in range(len(table_data)):
        col_widths.append(len(max(table_data[i], key=len)))

    for row in range(len(table_data[0])):
        row_str = ''
        for col in range(len(table_data)):
            row_str += table_data[col][row].rjust(col_widths[col] + 1)
        print(row_str)


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']
             ]

print_table(tableData)
