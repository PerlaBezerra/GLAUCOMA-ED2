class NoABB:

    def __init__(self, paciente):

        self.paciente = paciente
<<<<<<< HEAD
        self.esquerda = None
=======

        self.esquerda = None

>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
        self.direita = None


class ABB:

    def __init__(self):

        self.raiz = None
<<<<<<< HEAD
        self.comparacoes = 0


    # =========================
    # INSERÇÃO
    # =========================
    def inserir(self, paciente):

        self.raiz = self._inserir(self.raiz, paciente)
=======

        self.comparacoes = 0


    def inserir(self, paciente):

        self.raiz = self._inserir(

            self.raiz,
            paciente
        )
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f


    def _inserir(self, no, paciente):

        if no is None:
<<<<<<< HEAD
            return NoABB(paciente)

        self.comparacoes += 1

        if paciente.score < no.paciente.score:

            no.esquerda = self._inserir(no.esquerda, paciente)

        else:

            no.direita = self._inserir(no.direita, paciente)
=======

            return NoABB(paciente)


        self.comparacoes += 1


        if paciente.score < no.paciente.score:

            no.esquerda = self._inserir(

                no.esquerda,
                paciente
            )

        else:

            no.direita = self._inserir(

                no.direita,
                paciente
            )
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f

        return no


<<<<<<< HEAD
    # =========================
    # BUSCA POR ID DA IMAGEM
    # =========================
    def buscar(self, nome_imagem):

        return self._buscar(self.raiz, nome_imagem)


    def _buscar(self, no, nome_imagem):

        if no is None:
            return None

        if no.paciente.id_imagem == nome_imagem:
            return no.paciente

        esquerda = self._buscar(no.esquerda, nome_imagem)
        if esquerda:
            return esquerda

        return self._buscar(no.direita, nome_imagem)


    # =========================
    # ALTURA
    # =========================
=======
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
    def altura(self):

        return self._altura(self.raiz)


    def _altura(self, no):

        if no is None:
<<<<<<< HEAD
            return 0

        return max(
            self._altura(no.esquerda),
            self._altura(no.direita)
        ) + 1
=======

            return 0

        esquerda = self._altura(no.esquerda)

        direita = self._altura(no.direita)

        return max(esquerda, direita) + 1
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
