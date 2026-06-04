class NoABB:

    def __init__(self, paciente):
        self.paciente = paciente
        self.esquerda = None
        self.direita = None


class ABB:

    def __init__(self):
        self.raiz = None
        self.comparacoes = 0

    def inserir(self, paciente):
        self.raiz = self._inserir(self.raiz, paciente)

    def _inserir(self, no, paciente):

        if no is None:
            return NoABB(paciente)

        self.comparacoes += 1

        if paciente.score < no.paciente.score:
            no.esquerda = self._inserir(no.esquerda, paciente)
        else:
            no.direita = self._inserir(no.direita, paciente)

        return no

    def buscar(self, nome_imagem):
        return self._buscar(self.raiz, nome_imagem)

    def _buscar(self, no, nome_imagem):

        if no is None:
            return None

        if no.paciente.id_imagem == nome_imagem:
            return no.paciente

        res = self._buscar(no.esquerda, nome_imagem)
        if res:
            return res

        return self._buscar(no.direita, nome_imagem)

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, no):
        if no is None:
            return 0

        return max(
            self._altura(no.esquerda),
            self._altura(no.direita)
        ) + 1

    # 🔥 NOVO: lista ordenada (in-order)
    def listar_ordenado(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, lista):
        if no:
            self._em_ordem(no.esquerda, lista)
            lista.append(no.paciente)
            self._em_ordem(no.direita, lista)