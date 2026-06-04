import os
import time

from modelo import predict
<<<<<<< HEAD
=======

>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
from paciente import Paciente

from heap_maxima import HeapMaxima
from abb import ABB
from avl import AVL


# =========================
<<<<<<< HEAD
# CARREGAR PACIENTES
=======
# gerar pacientes
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
# =========================

pacientes = []

<<<<<<< HEAD
for imagem in os.listdir("images"):
=======
for imagem in os.listdir("images") :
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f

    if imagem.endswith(".jpg"):

        caminho = f"images/{imagem}"

        pred = predict(caminho)

        score = float(pred[0])

<<<<<<< HEAD
        paciente = Paciente(imagem, score)

        pacientes.append(paciente)

=======
        paciente = Paciente(

            imagem,
            score
    )

        pacientes.append(paciente)


>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
print(f"Pacientes carregados: {len(pacientes)}")


# =========================
<<<<<<< HEAD
# HEAP (ORGANIZAÇÃO)
=======
# HEAP
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
# =========================

heap = HeapMaxima()

inicio = time.time()

for paciente in pacientes:
<<<<<<< HEAD
=======

>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
    heap.inserir(paciente)

fim = time.time()

<<<<<<< HEAD
tempo_heap_org = fim - inicio


# =========================
# ABB (ORGANIZAÇÃO)
=======
tempo_heap = fim - inicio


# =========================
# ABB
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
# =========================

abb = ABB()

inicio = time.time()

for paciente in pacientes:
<<<<<<< HEAD
=======

>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
    abb.inserir(paciente)

fim = time.time()

<<<<<<< HEAD
tempo_abb_org = fim - inicio


# =========================
# AVL (ORGANIZAÇÃO)
=======
tempo_abb = fim - inicio


# =========================
# AVL
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
# =========================

avl = AVL()

inicio = time.time()

for paciente in pacientes:
<<<<<<< HEAD
=======

>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
    avl.inserir(paciente)

fim = time.time()

<<<<<<< HEAD
tempo_avl_org = fim - inicio


# =========================
# ESCOLHER PACIENTE PARA BUSCA
# =========================

imagem_busca = pacientes[len(pacientes) // 2].id_imagem


# =========================
# BUSCA ABB
# =========================

inicio = time.time()
resultado_abb = abb.buscar(imagem_busca)
fim = time.time()
tempo_abb_busca = fim - inicio


# =========================
# BUSCA AVL
# =========================

inicio = time.time()
resultado_avl = avl.buscar(imagem_busca)
fim = time.time()
tempo_avl_busca = fim - inicio


# =========================
# BUSCA HEAP (LINEAR)
# =========================

inicio = time.time()

resultado_heap = None

for p in heap.heap:
    if p.id_imagem == imagem_busca:
        resultado_heap = p
        break

fim = time.time()

tempo_heap_busca = fim - inicio


# =========================
# RESULTADOS
=======
tempo_avl = fim - inicio


# =========================
# resultados
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
# =========================

print("\n===== RESULTADOS =====\n")

<<<<<<< HEAD
print("HEAP")
print(f"Tempo organização: {tempo_heap_org:.6f}")
print(f"Tempo busca: {tempo_heap_busca:.6f}")
print(f"Comparações: {heap.comparacoes}")
print()

print("ABB")
print(f"Tempo organização: {tempo_abb_org:.6f}")
print(f"Tempo busca: {tempo_abb_busca:.6f}")
print(f"Comparações: {abb.comparacoes}")
print(f"Altura: {abb.altura()}")
print()

print("AVL")
print(f"Tempo organização: {tempo_avl_org:.6f}")
print(f"Tempo busca: {tempo_avl_busca:.6f}")
print(f"Comparações: {avl.comparacoes}")
print(f"Altura: {avl.altura()}")
print(f"Rotações: {avl.rotacoes}")
print()
=======

print("HEAP")

print(f"Tempo: {tempo_heap:.6f}")

print(f"Comparações: {heap.comparacoes}")

print()


print("ABB")

print(f"Tempo: {tempo_abb:.6f}")

print(f"Comparações: {abb.comparacoes}")

print(f"Altura: {abb.altura()}")

print()


print("AVL")

print(f"Tempo: {tempo_avl:.6f}")

print(f"Comparações: {avl.comparacoes}")

print(f"Altura: {avl.altura()}")

print(f"Rotações: {avl.rotacoes}")
>>>>>>> e20cc8ef63140f68e9561497dad77d3bd2329e2f
