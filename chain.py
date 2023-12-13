from chaintools import Cleric
from maptools import gen_chain_map, gen_RT_map

class Chain:
    
    def __init__(self) -> None:
        self._chain = list()
        self._chain_map = gen_chain_map()
        self._RT_map = gen_RT_map()

    def __str__(self) -> str:
        if len(self._chain):
            return " // ".join(str(c) for c in self._chain)+"\n"
        return "Empty Chain\n\n"

    def _set_positions(self) -> None:
        for i, cleric in enumerate(self._chain):
            if cleric:
                cleric.set_position(self._chain_map[str(i)])
        

    def add_cleric(self, new_cleric) -> None:
        if(isinstance(new_cleric, str)):
            self._chain.append(Cleric(new_cleric))
        self._set_positions()

    def remove_cleric(self, position_to_remove) -> None: 
        self._chain[int(self._chain_map.get(position_to_remove))] = None

    def remove_chain_gaps(self) -> None:
        self._chain = [cleric for cleric in self._chain if cleric]
        self._set_positions()

    def add_cleric_to_position(self, name: str, position: str) -> None:
        index = int(self._chain_map.get(position))
        new_cleric = Cleric(name)
        if self._chain[index]:
            self.add_cleric(self._chain[index].my_name()) #old cleric added to end
            self._chain[index] = new_cleric # new cleric is added to position
        else:
            self._chain[index] = new_cleric

        self._set_positions()

    def swap_clerics(self, posA, posB) -> None:
        posA, posB = int(self._chain_map.get(posA)), int(self._chain_map.get(posB))
        if self._chain[posA] and self._chain[posB]:
            self._chain[posA], self._chain[posB] = self._chain[posB], self._chain[posA]
        self._set_positions()