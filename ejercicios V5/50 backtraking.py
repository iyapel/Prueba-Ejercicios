print("El quilombo de las 8 reinas")

from typing import List
import random


class EightQueensPuzzle:
    def __init__(self, chessboard=8):
        self.chessboard = chessboard
        self.solucion = []

    def individuo_aleatorio(self) -> List:
        tablero = []
        for i in range(self.chessboard):
            tablero.append([0] * self.chessboard)
            tablero[i][random.randint(0, self.chessboard - 1)] = 1
        return tablero

    def mutar_fila(self, tablero: List, pos: int = 1) -> List:

        mutacion = [0] * self.chessboard
        mutacion[random.randint(0, self.chessboard - 1)] = 1

        tablero[pos] = mutacion
        return tablero

    def mutar_posiciones(self, tablero: List) -> List:
        pos1 = random.randint(0, self.chessboard - 1)
        pos2 = random.randint(0, self.chessboard - 1)

        mut = tablero[pos1]
        tablero[pos1] = tablero[pos2]
        tablero[pos2] = mut
        return tablero

    def mutacion_aleatoria(self, tablero: List) -> List:

        mutacion = [0] * self.chessboard
        mutacion[random.randint(0, self.chessboard - 1)] = 1

        tablero[random.randint(0, self.chessboard - 1)] = mutacion
        return tablero

    def combinar(self, individuo1: List, individuo2: List, cruce: int = 3) -> List:
        individuo_combinado = []
        for i in range(0, cruce):
            individuo_combinado.append(individuo1[i])

        for j in range(cruce, self.chessboard):
            individuo_combinado.append(individuo2[j])

        return individuo_combinado

    def get_solucion(self):
        return self.solucion

    def solucionar(self):
        tab1 = self.individuo_aleatorio()
        tab2 = self.individuo_aleatorio()
        error1, error2, error3, error4 = 1, 1, 1, 1
        while error1 > 0 and error2 > 0 and error3 > 0 and error4 > 0:
            error1 = self.es_solucion(tab1)
            error2 = self.es_solucion(tab2)
            if error1 != 0 and error2 != 0:
                tab5 = self.combinar(tab1, tab2)
                tab6 = self.combinar(tab2, tab1)

                tab3 = self.mutacion_aleatoria(tab5)
                tab4 = self.mutacion_aleatoria(tab6)

                error3 = self.es_solucion(tab3)
                error4 = self.es_solucion(tab4)

                tab1 = tab1 if error1 <= error2 else tab2
                tab2 = tab3 if error3 <= error4 else tab4

    def es_solucion(self, tablero: List):
        diagonal = []
        contra_diagonal = []
        columna = []
        err = 0

        for row in range(self.chessboard):
            for column in range(self.chessboard):
                if int(tablero[row][column]) == int(1):
                    if int(row - column) in diagonal:
                        err += 1
                    elif int(row + column) in contra_diagonal:
                        err += 1
                    elif int(column) in columna:
                        err += 1
                    else:
                        diagonal.append(row - column)
                        contra_diagonal.append(row + column)
                        columna.append(column)

        if err == 0:
            self.solucion = tablero

        return err


problema = EightQueensPuzzle(chessboard=8)

problema.solucionar()
print(problema.get_solucion())
