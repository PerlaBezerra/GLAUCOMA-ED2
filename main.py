import os
import time

from modelo import predict
from paciente import Paciente

from heap_maxima import HeapMaxima
from abb import ABB
from avl import AVL


# =========================
# CARREGAR PACIENTES
# =========================

pacientes = []

for imagem in os.listdir("images"):

    if imagem.endswith(".jpg"):

        caminho = f"images/{imagem}"

        pred = predict(caminho)

        score = float(pred[0])

        paciente = Paciente(imagem, score)

        pacientes.append(paciente)

print(f"Pacientes carregados: {len(pacientes)}")


# =========================
# HEAP (ORGANIZAÇÃO)
# =========================

heap = HeapMaxima()

inicio = time.time()

for paciente in pacientes:
    heap.inserir(paciente)

fim = time.time()

tempo_heap_org = fim - inicio


# =========================
# ABB (ORGANIZAÇÃO)
# =========================

abb = ABB()

inicio = time.time()

for paciente in pacientes:
    abb.inserir(paciente)

fim = time.time()

tempo_abb_org = fim - inicio


# =========================
# AVL (ORGANIZAÇÃO)
# =========================

avl = AVL()

inicio = time.time()

for paciente in pacientes:
    avl.inserir(paciente)

fim = time.time()

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
# =========================

print("\n===== RESULTADOS =====\n")

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