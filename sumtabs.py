def sum_integers_from_file(filename):
    total_sum = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split each line into words and check if they're integers
                for word in line.split():
                    if word.isdigit():
                        total_sum += int(word)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    return total_sum

# Example usage
filename = 'localize.txt'  # Replace with your file path
result = sum_integers_from_file(filename)
print(f"The sum of integers in the file is: {result}")