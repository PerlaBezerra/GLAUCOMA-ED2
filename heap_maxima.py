class HeapMaxima:

    def __init__(self):

        self.heap = []
        self.comparacoes = 0


    # =========================
    # INSERÇÃO
    # =========================
    def inserir(self, paciente):

        self.heap.append(paciente)
        self._subir(len(self.heap) - 1)


    # =========================
    # SUBIR (HEAPIFY UP)
    # =========================
    def _subir(self, indice):

        while indice > 0:

            pai = (indice - 1) // 2

            self.comparacoes += 1

            # Heap Máxima: maior score fica em cima
            if self.heap[indice].score > self.heap[pai].score:

                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai

            else:
                break


    # =========================
    # REMOÇÃO (caso precise no futuro)
    # =========================
    def remover_max(self):

        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._descer(0)

        return raiz


    # =========================
    # DESCER (HEAPIFY DOWN)
    # =========================
    def _descer(self, indice):

        n = len(self.heap)

        while True:

            maior = indice
            esquerda = 2 * indice + 1
            direita = 2 * indice + 2

            if esquerda < n:

                self.comparacoes += 1

                if self.heap[esquerda].score > self.heap[maior].score:
                    maior = esquerda

            if direita < n:

                self.comparacoes += 1

                if self.heap[direita].score > self.heap[maior].score:
                    maior = direita

            if maior != indice:

                self.heap[indice], self.heap[maior] = self.heap[maior], self.heap[indice]
                indice = maior

            else:
                break


    # =========================
    # ALTURA (opcional para relatório)
    # =========================
    def altura(self):

        import math

        if len(self.heap) == 0:
            return 0

        return math.floor(math.log2(len(self.heap))) + 1