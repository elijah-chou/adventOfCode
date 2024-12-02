def main():
  file_path = 'day1input.txt'
  list1 = []
  list2 = []
  with open(file_path, mode = 'r') as file:
    for line in file:
      numbers = line.strip().split('   ') # each row's numbers are separated by 3 spaces
      list1.append(int(numbers[0]))
      list2.append(int(numbers[1]))

  print(list1[:3])
  print(list2[:3])

  list1.sort()
  list2.sort()
  total_distance = sum(abs(a - b) for a,b in zip(list1, list2))

  print("Total distance: ", total_distance)
if __name__ == "__main__":
  main()
