from chaintools import Cleric


class Chain:
    
    def __init__(self) -> None:
        self._chain = list()

    def __str__(self) -> str:
        if len(self._chain):
            return "; ".join(str(c) for c in self._chain)
        return "Empty Chain"

    def _set_positions(self) -> None:
        for i, cleric in enumerate(self._chain):
            if cleric:
                cleric.set_position(self._position_map(i))
        

    def add_cleric(self, new_cleric) -> None:
        
        if(isinstance(new_cleric, str)):
            self._chain.append(Cleric(new_cleric))
        self._set_positions()

    def remove_cleric(self, position_to_remove) -> None: 
        self._chain[position_to_remove] = None

    def remove_chain_gaps(self) -> None:
        
        self._chain = [cleric for cleric in self._chain if cleric]
        self._set_positions()
        

    def _position_map(self, index) -> str:
        if index < 9:
            return str(index+1)*3
        elif index == 9:
            return "000"
        elif index == 18:
            return "iii"
        else:
            return chr(index+55)*3