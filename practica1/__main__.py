import sys
sys.path.append('C:/Users/kirky/IA_2023')

from practica1 import agent, joc


def main():
    quatre = joc.Taulell([agent.Agent("Miquel")])
    quatre.comencar()


if __name__ == "__main__":
    main()
