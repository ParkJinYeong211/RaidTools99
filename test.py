from chain import Chain
from maptools import gen_RT_map, gen_chain_map
from chaintools import Cleric

cleric_names = ["Spasepope", "Drgn", "Vet", "Katastrophic", "Salvette", "Fizzlesnick", "Teomus", "Exeter", "Ossington", "Darulah", "Absolve"]
new_chain = Chain("Test Chain", gen_chain_map())

for c in cleric_names:
    new_chain.add_cleric(c)

print("Create a chain")
print(new_chain)

new_chain.remove_cleric("222")
new_chain.remove_cleric("444")

print("Remove 222, 444")
print(new_chain)

new_chain.add_cleric_to_position("Drgn", "222")

print("Add Drgn to 222")
print(new_chain)

new_chain.add_cleric_to_position("Katastrophic", "222")

print("Add Kata to 222 (Drgn should go to the end)")
print(new_chain)

new_chain.add_cleric("Chapman")

print("Add Chapman")
print(new_chain)

new_chain.remove_chain_gaps()

print("Tidy up chain")
print(new_chain)

new_chain.swap_clerics("222", "555")

print("Swap 222, 555")
print(new_chain)

new_chain.add_cleric_to_position("Rodolfo", "XXX")
print("Trying to add a cleric to a position out of range:")
print(new_chain)

new_chain.remove_cleric("YYY")
print("Trying to remove cleric from position that doesn't exist:")
print (new_chain)