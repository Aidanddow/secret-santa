import sys
import random

# Secret Santa
# Takes a list of names, shuffles it and outputs who each person is to buy for

# Output who buys for who by mapping each element in the list to the next
def output_names(name_list):

    # Iterate from -1 so that the last person in the list buys for the first
    for i in range(-1, len(name_list) - 1):
        # Output: "Name1 buys for Name2"
        print(f"{name_list[i].capitalize()} buys for {name_list[i+1].capitalize()}")


def main():

    # Number of names provided
    count = len(sys.argv) - 1

    # If no names were provided
    if count == 0:
        print("Please enter some names!")
        return

    # Secret santa cannot be done with less than three people
    if count <= 3:
        print("Unfortunately, Secret Santa won't work for this amount of people!")
        return

    # sys.argv will look like ["secret_santa.py", "name1", "name2", ...]
    # We extract only the names
    names = [sys.argv[i+1] for i in range(count)]

    # Shuffle the names
    random.shuffle(names)

    # Display output
    output_names(names)



if __name__ == "__main__":
    main()