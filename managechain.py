from chain import Chain
import os

my_chain = Chain()

def write_options() -> None:
    os.system('cls')
    print(my_chain)
    print("1. Add Cleric (to end)")
    print("2. Add Cleric to specific position")
    print("3. Remove Cleric")
    print("4. Swap Cleric")
    print("5. Remove Gaps in Chain")
    print("6. Copy chain to buffer")
    print("0. Quit")

while True:
    write_options()

    selection = input("Make Selection: ")
    print("\n")
    match selection:
        case "0": break
        case "1":
            cleric = input("Cleric name: ")
            my_chain.add_cleric(cleric)
        case "2":
            cleric = input("Cleric name: ")
            position = input("Position: ")
            my_chain.add_cleric_to_position(cleric, position)
        case "3":
            position = input("Cleric position to remove: ")
            my_chain.remove_cleric(position)
        case "4":
            clericA, clericB = input("Cleric A to swap with B: "), input("Cleric B to swap with A: ")
            my_chain.swap_clerics(clericA, clericB)
        case "5":
            my_chain.remove_chain_gaps()
        case "6":
            print("not yet implemented")
            pass
                


print("bye!")

