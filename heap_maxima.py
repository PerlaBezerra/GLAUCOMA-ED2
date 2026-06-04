class HeapMaxima:

    def __init__(self):

        self.heap = []
<<<<<<< HEAD
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
=======

        self.comparacoes = 0


    def inserir(self, paciente):

        self.heap.append(paciente)

        self.subir(len(self.heap) - 1)


    def subir(self, indice):

        pai = (indice - 1) // 2

        while indice > 0 and self.heap[indice].score > self.heap[pai].score:

            self.comparacoes += 1

            self.heap[indice], self.heap[pai] = (

                self.heap[pai],
                self.heap[indice]
            )

            indice = pai

            pai = (indice - 1) // 2


    def remover_maior(self):

        if len(self.heap) == 0:

            return None

        maior = self.heap[0]

        ultimo = self.heap.pop()

        if self.heap:

            self.heap[0] = ultimo

            self.descer(0)

        return maior


    def descer(self, indice):

        tamanho = len(self.heap)
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f

        while True:

            maior = indice
<<<<<<< HEAD
            esquerda = 2 * indice + 1
            direita = 2 * indice + 2

            if esquerda < n:
=======

            esquerda = 2 * indice + 1

            direita = 2 * indice + 2


            if esquerda < tamanho:
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f

                self.comparacoes += 1

                if self.heap[esquerda].score > self.heap[maior].score:
<<<<<<< HEAD
                    maior = esquerda

            if direita < n:
=======

                    maior = esquerda


            if direita < tamanho:
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f

                self.comparacoes += 1

                if self.heap[direita].score > self.heap[maior].score:
<<<<<<< HEAD
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
=======

                    maior = direita


            if maior == indice:

                break


            self.heap[indice], self.heap[maior] = (

                self.heap[maior],
                self.heap[indice]
            )

            indice = maior
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
