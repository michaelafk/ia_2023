from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import SENSOR


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def actua(
            self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        estat = Estat(local_barca=percepcio[SENSOR.LLOC], polls_esq=percepcio[SENSOR.QUICA_ESQ],
                      llops_esq=percepcio[SENSOR.LLOP_ESQ])

        pass
