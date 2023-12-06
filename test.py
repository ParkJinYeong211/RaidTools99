from chain import Chain
from chaintools import Cleric

clericA, clericB, clericC = Cleric("Spasepope"), Cleric("Drgn"), Cleric("Vet")
new_chain = Chain()

print(f"Clerics are: {clericA}; {clericB}, {clericC}")

print(new_chain)

new_chain.add_cleric(clericA)

print(new_chain)

new_chain.add_cleric(clericB)

print(new_chain)

new_chain.add_cleric(clericC)

print(new_chain)
