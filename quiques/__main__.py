import sys
sys.path.append('C:/Users/kirky/IA_2023')
from quiques import agent_amplada, agent_profunditat, joc


def main():
    barca = agent_amplada.BarcaAmplada()
    illes = joc.Illes([barca])
    illes.comencar()


if __name__ == "__main__":
    main()
