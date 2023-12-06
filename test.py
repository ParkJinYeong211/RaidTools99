from chain import Chain
from chaintools import Cleric

cleric_names = ["Spasepope", "Drgn", "Vet", "Katastrophic", "Salvette", "Fizzlesnick", "Teomus"]
new_chain = Chain()

for c in cleric_names:
    new_chain.add_cleric(c)
    print(new_chain)

new_chain.remove_cleric(1)
new_chain.remove_cleric(3)

print(new_chain)

new_chain.remove_chain_gaps()

print(new_chain)