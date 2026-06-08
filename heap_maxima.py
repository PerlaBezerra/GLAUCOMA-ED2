#HEAP_MAXIMA
import math

class HeapMaxima:

    def __init__(self):
        self.heap = []
        self.comparacoes = 0

    def inserir(self, paciente):
        self.heap.append(paciente)
        self._subir(len(self.heap) - 1)

    def _subir(self, i):

        while i > 0:
            pai = (i - 1) // 2

            self.comparacoes += 1  # comparação pai vs filho

            if self.heap[i].score > self.heap[pai].score:
                self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
                i = pai
            else:
                break

    def _descer(self, i):

        n = len(self.heap)

        while True:

            maior = i
            e = 2 * i + 1
            d = 2 * i + 2

            if e < n:
                self.comparacoes += 1
                if self.heap[e].score > self.heap[maior].score:
                    maior = e

            if d < n:
                self.comparacoes += 1
                if self.heap[d].score > self.heap[maior].score:
                    maior = d

            if maior == i:
                break

            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            i = maior

    def remover_maior(self):
        if not self.heap:
            return None

        maior = self.heap[0]
        ultimo = self.heap.pop()

        if self.heap:
            self.heap[0] = ultimo
            self._descer(0)

        return maior

    def listar_ordenado(self):
        return sorted(self.heap, key=lambda x: x.score, reverse=True)

    def vazia(self):
        return len(self.heap) == 0

    def altura(self):
        if not self.heap:
            return 0
        return math.floor(math.log2(len(self.heap))) + 1