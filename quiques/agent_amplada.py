from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca, SENSOR


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def actua(
            self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        x = Estat(2,3,3)
        oberts = []
        tancats = []
        oberts.append(x)
        while oberts:
            estat_actual = oberts.pop(0)
            if estat_actual.es_meta:
                return AccionsBarca.MOURE()
            else:
                fills = estat_actual.genera_fill()
                tancats.append(estat_actual)
                oberts.append(fills)
        return AccionsBarca.ATURAR

