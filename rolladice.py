import random

# Function to display the dice face based on the rolled number
def display_dice(number):
    dice_faces = {
        1: [
            "[-----]",
            "[     ]",
            "[  0  ]",
            "[     ]",
            "[-----]"
        ],
        2: [
            "[-----]",
            "[0    ]",
            "[     ]",
            "[    0]",
            "[-----]"
        ],
        3: [
            "[-----]",
            "[0    ]",
            "[  0  ]",
            "[    0]",
            "[-----]"
        ],
        4: [
            "[-----]",
            "[0   0]",
            "[     ]",
            "[0   0]",
            "[-----]"
        ],
        5: [
            "[-----]",
            "[0   0]",
            "[  0  ]",
            "[0   0]",
            "[-----]"
        ],
        6: [
            "[-----]",
            "[0   0]",
            "[0   0]",
            "[0   0]",
            "[-----]"
        ]
    }
    
    # Print the corresponding face of the dice
    for line in dice_faces[number]:
        print(line)

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        # Roll the dice
        number = roll_dice()
        
        # Display the result
        print(f"You rolled a {number}:")
        display_dice(number)
        
        # Ask if the user wants to roll again
        roll_again = input("Press 'y' to roll again and 'n' to exit: ")
        if roll_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
