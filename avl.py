class NoAVL:

    def __init__(self, paciente):

        self.paciente = paciente
<<<<<<< HEAD
        self.esquerda = None
        self.direita = None
=======

        self.esquerda = None

        self.direita = None

>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
        self.altura = 1


class AVL:

    def __init__(self):

        self.raiz = None
<<<<<<< HEAD
        self.comparacoes = 0
        self.rotacoes = 0


    # =========================
    # ALTURA
    # =========================
    def altura_no(self, no):

        if not no:
=======

        self.comparacoes = 0

        self.rotacoes = 0


    def altura_no(self, no):

        if not no:

>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
            return 0

        return no.altura


    def fator_balanceamento(self, no):

        if not no:
<<<<<<< HEAD
            return 0

        return self.altura_no(no.esquerda) - self.altura_no(no.direita)


    # =========================
    # ROTAÇÕES
    # =========================
=======

            return 0

        return (

            self.altura_no(no.esquerda)
            -
            self.altura_no(no.direita)
        )


>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
    def rotacao_direita(self, y):

        self.rotacoes += 1

        x = y.esquerda
<<<<<<< HEAD
        t2 = x.direita

        x.direita = y
        y.esquerda = t2

        y.altura = 1 + max(self.altura_no(y.esquerda), self.altura_no(y.direita))
        x.altura = 1 + max(self.altura_no(x.esquerda), self.altura_no(x.direita))
=======

        t2 = x.direita

        x.direita = y

        y.esquerda = t2

        y.altura = 1 + max(

            self.altura_no(y.esquerda),

            self.altura_no(y.direita)
        )

        x.altura = 1 + max(

            self.altura_no(x.esquerda),

            self.altura_no(x.direita)
        )
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f

        return x


    def rotacao_esquerda(self, x):

        self.rotacoes += 1

        y = x.direita
<<<<<<< HEAD
        t2 = y.esquerda

        y.esquerda = x
        x.direita = t2

        x.altura = 1 + max(self.altura_no(x.esquerda), self.altura_no(x.direita))
        y.altura = 1 + max(self.altura_no(y.esquerda), self.altura_no(y.direita))
=======

        t2 = y.esquerda

        y.esquerda = x

        x.direita = t2

        x.altura = 1 + max(

            self.altura_no(x.esquerda),

            self.altura_no(x.direita)
        )

        y.altura = 1 + max(

            self.altura_no(y.esquerda),

            self.altura_no(y.direita)
        )
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f

        return y


<<<<<<< HEAD
    # =========================
    # INSERÇÃO
    # =========================
    def inserir(self, paciente):

        self.raiz = self._inserir(self.raiz, paciente)
=======
    def inserir(self, paciente):

        self.raiz = self._inserir(

            self.raiz,
            paciente
        )
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f


    def _inserir(self, no, paciente):

        if not no:
<<<<<<< HEAD
            return NoAVL(paciente)

        self.comparacoes += 1

        if paciente.score < no.paciente.score:

            no.esquerda = self._inserir(no.esquerda, paciente)

        else:

            no.direita = self._inserir(no.direita, paciente)

        no.altura = 1 + max(
            self.altura_no(no.esquerda),
            self.altura_no(no.direita)
        )

        balanceamento = self.fator_balanceamento(no)

        if balanceamento > 1 and paciente.score < no.esquerda.paciente.score:
            return self.rotacao_direita(no)

        if balanceamento < -1 and paciente.score > no.direita.paciente.score:
            return self.rotacao_esquerda(no)

        if balanceamento > 1 and paciente.score > no.esquerda.paciente.score:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        if balanceamento < -1 and paciente.score < no.direita.paciente.score:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no


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

            return NoAVL(paciente)


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


        no.altura = 1 + max(

            self.altura_no(no.esquerda),

            self.altura_no(no.direita)
        )


        balanceamento = self.fator_balanceamento(no)


        if balanceamento > 1 and paciente.score < no.esquerda.paciente.score:

            return self.rotacao_direita(no)


        if balanceamento < -1 and paciente.score > no.direita.paciente.score:

            return self.rotacao_esquerda(no)


        if balanceamento > 1 and paciente.score > no.esquerda.paciente.score:

            no.esquerda = self.rotacao_esquerda(no.esquerda)

            return self.rotacao_direita(no)


        if balanceamento < -1 and paciente.score < no.direita.paciente.score:

            no.direita = self.rotacao_direita(no.direita)

            return self.rotacao_esquerda(no)


        return no


>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
    def altura(self):

        return self.altura_no(self.raiz)