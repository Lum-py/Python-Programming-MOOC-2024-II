# Write your solution here
def row_sums(my_matrix: list):  
    for row in my_matrix:
        result = 0
        for item in row:
            result += item
        row.append(result)



if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)