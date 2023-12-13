from chaintools import Cleric
from maptools import gen_chain_map, gen_RT_map

class Chain:
    
    def __init__(self, name:str, map: dict) -> None:
        self._name = name
        self._chain = list()
        self._map = map

    def __str__(self) -> str:
        if len(self._chain):
            return self._name+" :: "+" // ".join(str(c) for c in self._chain)+"\n"
        return f"{self._name} :: Empty Chain\n"

    def _set_positions(self) -> None:
        for i, cleric in enumerate(self._chain):
            if cleric:
                cleric.set_position(self._map[str(i)])
        

    def add_cleric(self, new_cleric) -> None:
        if(isinstance(new_cleric, str)):
            self._chain.append(Cleric(new_cleric))
        self._set_positions()

    def remove_cleric(self, position_to_remove) -> None: 
        try:
            self._chain[int(self._map.get(position_to_remove))] = None
        except IndexError:
            pass

    def remove_chain_gaps(self) -> None:
        self._chain = [cleric for cleric in self._chain if cleric]
        self._set_positions()

    def add_cleric_to_position(self, name: str, position: str) -> None:
        index = int(self._map.get(position))
        new_cleric = Cleric(name)
        try:
            if self._chain[index]:
                self.add_cleric(self._chain[index].my_name()) #old cleric added to end
                self._chain[index] = new_cleric # new cleric is added to position
            else:
                self._chain[index] = new_cleric

        except IndexError:
            pass

        self._set_positions()

    def swap_clerics(self, posA, posB) -> None:
        posA, posB = int(self._map.get(posA)), int(self._map.get(posB))
        if self._chain[posA] and self._chain[posB]:
            self._chain[posA], self._chain[posB] = self._chain[posB], self._chain[posA]
        self._set_positions()