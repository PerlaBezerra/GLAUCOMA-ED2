import os
import time

from modelo import predict
from paciente import Paciente

from heap_maxima import HeapMaxima
from abb import ABB
from avl import AVL


# =========================
# FUNÇÃO DE RISCO
# =========================
def classificar_risco(score):
    if score <= 0.33:
        return "RISCO BAIXO"
    elif score <= 0.66:
        return "RISCO MÉDIO"
    else:
        return "RISCO ALTO"


# =========================
# CARREGAR PACIENTES
# =========================
pacientes = []

for imagem in os.listdir("images"):
    if imagem.endswith(".jpg"):

        caminho = f"images/{imagem}"
        pred = predict(caminho)

        score = float(pred[0])

        pacientes.append(Paciente(imagem, score))

print(f"Pacientes carregados: {len(pacientes)}")


# =========================
# HEAP
# =========================
heap = HeapMaxima()

inicio = time.time()
for p in pacientes:
    heap.inserir(p)
tempo_heap_org = time.time() - inicio


# =========================
# ABB
# =========================
abb = ABB()

inicio = time.time()
for p in pacientes:
    abb.inserir(p)
tempo_abb_org = time.time() - inicio


# =========================
# AVL
# =========================
avl = AVL()

inicio = time.time()
for p in pacientes:
    avl.inserir(p)
tempo_avl_org = time.time() - inicio


# =========================
# BUSCA
# =========================
img_busca = pacientes[len(pacientes)//2].id_imagem

inicio = time.time()
abb.buscar(img_busca)
tempo_busca_abb = time.time() - inicio

inicio = time.time()
avl.buscar(img_busca)
tempo_busca_avl = time.time() - inicio

inicio = time.time()
for p in heap.heap:
    if p.id_imagem == img_busca:
        break
tempo_busca_heap = time.time() - inicio


# =========================
# RESULTADOS
# =========================
print("\n===== RESULTADOS =====\n")

print("HEAP")
print(f"Tempo inserção: {tempo_heap_org:.6f}")
print(f"Tempo organização: {tempo_heap_org:.6f}")
print(f"Tempo busca: {tempo_busca_heap:.6f}")
print(f"Comparações: {heap.comparacoes}\n")

print("ABB")
print(f"Tempo inserção: {tempo_abb_org:.6f}")
print(f"Tempo organização: {tempo_abb_org:.6f}")
print(f"Tempo busca: {tempo_busca_abb:.6f}")
print(f"Comparações: {abb.comparacoes}")
print(f"Altura: {abb.altura()}\n")

print("AVL")
print(f"Tempo inserção: {tempo_avl_org:.6f}")
print(f"Tempo organização: {tempo_avl_org:.6f}")
print(f"Tempo busca: {tempo_busca_avl:.6f}")
print(f"Comparações: {avl.comparacoes}")
print(f"Altura: {avl.altura()}")
print(f"Rotações: {avl.rotacoes}\n")


# =========================
# FILAS (TOP 10 COM RISCO)
# =========================

print("\nFILA DE PACIENTES (ABB)")
for i, p in enumerate(abb.listar_ordenado()[:10], start=1):
    print(f"{i}. {p.id_imagem} - {p.score:.6f} - {classificar_risco(p.score)}")

print("\nFILA DE PACIENTES (AVL)")
for i, p in enumerate(avl.listar_ordenado()[:10], start=1):
    print(f"{i}. {p.id_imagem} - {p.score:.6f} - {classificar_risco(p.score)}")

print("\nFILA DE PACIENTES (HEAP)")
for i, p in enumerate(heap.listar_ordenado()[:10], start=1):
    print(f"{i}. {p.id_imagem} - {p.score:.6f} - {classificar_risco(p.score)}")