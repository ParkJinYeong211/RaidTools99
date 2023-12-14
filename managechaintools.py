import os
from chain import Chain

def display_chains(*chains) -> None:
    os.system('cls')
    for chain in chains:
        print(chain)
    print("(M)ain chain, (R)T Chain, or (Q)uit?: ")

def display_chain_options() -> None:
    print("1. Add Cleric (to end)")
    print("2. Add Cleric to specific position")
    print("3. Remove Cleric")
    print("4. Swap Cleric")
    print("5. Remove Gaps in Chain")
    print("6. Copy chain to buffer")

def manage_chain_selection(chain: Chain) -> None:
    display_chain_options()
    
    selection = input("Make a selection (any other key to cancels to main menu): ")

    match selection:
        case "1":
            cleric = input("Cleric name: ")
            chain.add_cleric(cleric)
        case "2":
            cleric = input("Cleric name: ")
            position = input("Position: ")
            chain.add_cleric_to_position(cleric, position)
        case "3":
            position = input("Cleric position to remove: ")
            chain.remove_cleric(position)
        case "4":
            clericA, clericB = input("Cleric A to swap with B: "), input("Cleric B to swap with A: ")
            chain.swap_clerics(clericA, clericB)
        case "5":
            chain.remove_chain_gaps()
        case "6":
            print("not yet implemented")
            pass
                