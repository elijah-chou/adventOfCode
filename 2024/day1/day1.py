def main():
    # Define the path to the input file
    file_path = 'day1input.txt'

    # Initialize two empty lists
    list1 = []
    list2 = []

    # Open and read the text file
    with open(file_path, mode='r') as file:
        for line in file:
            numbers = line.strip().split('   ')  # Split by 3 spaces
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

    print("List 1:", list1[0:3])
    print("List 2:", list2[0:3])

    # Sort the lists in ascending order
    list1.sort()
    list2.sort()

    # Calculate the sum of the absolute values of the distances
    total_distance = sum(abs(a - b) for a, b in zip(list1, list2))

    # Calculate the similarity score
    similarity_score = 0
    for num in list1:
        similarity_score += num * list2.count(num)

    # Print the total distance, and similarity score to verify the result
    print("Total Distance:", total_distance)
    print("Similarity Score:", similarity_score)

if __name__ == "__main__":
    main()
