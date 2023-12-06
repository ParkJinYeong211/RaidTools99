from chain import Chain
from chaintools import Cleric

cleric_names = ["Spasepope", "Drgn", "Vet", "Katastrophic", "Salvette", "Fizzlesnick", "Teomus", "Exeter", "Ossington", "Darulah", "Absolve"]
new_chain = Chain()

for c in cleric_names:
    new_chain.add_cleric(c)

print("Create a chain")
print(new_chain)

new_chain.remove_cleric(1)
new_chain.remove_cleric(3)

print("Remove 222, 444")
print(new_chain)

new_chain.add_cleric_to_position("Drgn", 1)

print("Add Drgn to 222")
print(new_chain)

new_chain.add_cleric_to_position("Katastrophic", 1)

print("Add Kata to 222 (Drgn should go to the end)")
print(new_chain)

new_chain.add_cleric("Chapman")

print("Add Chapman")
print(new_chain)

new_chain.remove_chain_gaps()

print("Tidy up chain")
print(new_chain)

new_chain.swap_clerics(1, 5)

print("Swap 222, 555")
print(new_chain)