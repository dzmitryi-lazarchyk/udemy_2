


while True:
    side = input("Throw the coin and enter head or tail here: ")

    match side:
        case 'tail' | 'head':
            with open('../files/heads_tails', 'r') as file:
                lines = file.readlines()
                lines.append(side + "\n")
                result = lines.count('head\n')/len(lines)*100
                print(f"Heads: {result}")
            with open('../files/heads_tails', 'w') as file:
                print(lines)
                file.writelines(lines)
        case _:
            print("Wrong input!")
