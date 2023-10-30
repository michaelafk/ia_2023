from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import SENSOR,AccionsBarca


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
        obert = [estat]
        cami = []
        tancat = set()
        while obert:
            estat_actual = obert.pop()
            if estat_actual.es_meta():
                #cami.append(AccionsBarca.MOURE)
                return cami
            elif estat_actual.legal and estat_actual.es_segur:
                #cami.append(AccionsBarca.MOURE)
                for estat_seguent in estat_actual.genera_fill():
                    if estat_seguent not in tancat:
                        obert.append(estat_seguent)
                tancat.add(estat_actual)
