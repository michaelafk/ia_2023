import sys
sys.path.append('C:/Users/kirky/IA_2023')

from aspirador import agent, joc


def main():
    aspirador = agent.AspiradorTaula()
    hab = joc.Casa([aspirador])
    hab.comencar()


if __name__ == "__main__":
    main()
