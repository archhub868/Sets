# Function to get user input for a set of integers
def get_integer_set():
  user_input = input("Enter a list of integers (or 'x' to quit): ")
  while user_input.lower() != 'x':
    try:
      # Convert input string to a set of integers (handling duplicates)
      integer_set = set(map(int, user_input.split(",")))
      return integer_set
    except ValueError:
      print("Invalid input. Please enter a valid list of integers.")
    user_input = input("Try again (or 'x' to quit): ")
  return None  # Return None if user enters 'x' at the beginning

# Get sets from user input
set1 = get_integer_set()
if set1 is None:
  exit()  # Exit program if user quits for set1

set2 = get_integer_set()
if set2 is None:
  exit()  # Exit program if user quits for set2

# Find common elements using intersection
common_elements = set1.intersection(set2)

# Print the common elements
if common_elements:
  print("Great work ninja there exists common elements in both sets:", common_elements)
else:
  print("There are no common elements between the sets! Try Again Next time Pal.")
