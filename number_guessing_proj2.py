import random
rand_number = random.randint(1,100)

playing = True

while playing:
    try:
        choice = int(input("Guess the number between 1 and 100\n"))
        if 1 <= choice <= 100:
            if choice > rand_number:
                print("too high")

            elif choice < rand_number:
                print("too low")

            else:
                print("Congratulations! you have guessed the number")
                break
        
        else:
            print("Please enter a valid number")
    except ValueError:
        print("Please enter a valid number")