from chain import Chain
from maptools import gen_chain_map, gen_RT_map
import os

main_chain, RT_chain = Chain("Main Chain", gen_chain_map()), Chain("RT Chain", gen_RT_map)

def write_options() -> None:
    os.system('cls')
    print(main_chain)
    print(RT_chain)
    print("1. Add Cleric (to end)")
    print("2. Add Cleric to specific position")
    print("3. Remove Cleric")
    print("4. Swap Cleric")
    print("5. Remove Gaps in Chain")
    print("6. Copy chain to buffer")
    print("0. Quit\n")

while True:
    write_options()

    selection = input("Make Selection: ")
    match selection:
        case "0": break
        case "1":
            cleric = input("Cleric name: ")
            main_chain.add_cleric(cleric)
        case "2":
            cleric = input("Cleric name: ")
            position = input("Position: ")
            main_chain.add_cleric_to_position(cleric, position)
        case "3":
            position = input("Cleric position to remove: ")
            main_chain.remove_cleric(position)
        case "4":
            clericA, clericB = input("Cleric A to swap with B: "), input("Cleric B to swap with A: ")
            main_chain.swap_clerics(clericA, clericB)
        case "5":
            main_chain.remove_chain_gaps()
        case "6":
            print("not yet implemented")
            pass
                


print("bye!")

