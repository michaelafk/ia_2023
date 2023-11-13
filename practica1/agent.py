"""

ClauPercepcio:
    POSICIO = 0
    OLOR = 1
    PARETS = 2
"""
from ia_2022 import entorn
from practica1 import joc
from practica1.entorn import Accio


class Agent(joc.Agent):
    def __init__(self, nom):
        super(Agent, self).__init__(nom)

    def pinta(self, display):
        pass

    def actua(
            self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        return (Accio.POSAR,[])
class Estat:
    def __init__(self,taulell,mida,pare=None, accions_previes=None):
        self.pare = pare
        if accions_previes is None:
            self.accions_previes = []
        self.taulell = taulell
        self.mida = mida

    def generar_fills(self) -> list:
        Estat_generats = []

        exit = False
        for i in range(self.mida - 1):#la cantidad de hijos es N-1 despues de colocar una ficha
            nou_estat = self
            nou_estat.pare = (self)
            nou_estat.accions_previes.append(self.taulell)
            for x in range[self.mida]:#columna
                for y in range[self.mida]:#fila
                    if nou_estat.taulell[x][y] == 0:
                        nou_estat.taulell[x][y] == 1
                        exit = True
                        break
                if exit:
                    break
            exit = False
            Estat_generats.append(nou_estat)
        return Estat_generats  
            

        
    
    

