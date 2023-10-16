from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca, SENSOR


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def _cerca(self, estat_inicial: Estat):
        self.__oberts = []
        self.__tancats = set()

        self.__oberts.append(estat_inicial)
        actual = None
        while len(self.__oberts) > 0:
            actual = self.__oberts.pop(0)

            if actual in self.__tancats:
                continue

            if not actual.es_segur():
                self.__tancats.add(actual)
                continue

            if actual.es_meta():
                break

            estats_fills = actual.genera_fill()

            for estat_f in estats_fills:
                self.__oberts.append(estat_f)

            self.__tancats.add(actual)
        if actual is None:
            raise ValueError("Error impossible")

        if actual.es_meta():
            self.__accions = actual.accions_previes
            return True

        return False

    def actua(
            self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        estat = Estat(local_barca=percepcio[SENSOR.LLOC], polls_esq=percepcio[SENSOR.QUICA_ESQ],
                      llops_esq=percepcio[SENSOR.LLOP_ESQ])

        if self.__accions is None:
            self._cerca(estat_inicial=estat)

        if len(self.__accions) > 0:
            return AccionsBarca.MOURE, self.__accions.pop()
        else:
            return AccionsBarca.ATURAR
