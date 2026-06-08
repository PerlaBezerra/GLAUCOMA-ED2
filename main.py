#MAIN
import os
import time
import csv

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

imagens = [
    img for img in os.listdir("images")
    if img.endswith(".jpg")
][:1020]

for img in imagens:
    caminho = os.path.join("images", img)
    pred = predict(caminho)
    score = float(pred[0])

    pacientes.append(Paciente(img, score))

print("Pacientes carregados:", len(pacientes))


# =========================
# HEAP
# =========================

heap = HeapMaxima()

inicio = time.perf_counter()
for p in pacientes:
    heap.inserir(p)
tempo_heap_insercao = time.perf_counter() - inicio

inicio = time.perf_counter()
ordem_heap = []
while not heap.vazia():
    ordem_heap.append(heap.remover_maior())
tempo_heap_ordem = time.perf_counter() - inicio


# =========================
# ABB
# =========================

abb = ABB()

inicio = time.perf_counter()
for p in pacientes:
    abb.inserir(p)
tempo_abb_insercao = time.perf_counter() - inicio

inicio = time.perf_counter()
ordem_abb = []
abb._em_ordem(abb.raiz, ordem_abb)
tempo_abb_ordem = time.perf_counter() - inicio


# =========================
# AVL
# =========================

avl = AVL()

inicio = time.perf_counter()
for p in pacientes:
    avl.inserir(p)
tempo_avl_insercao = time.perf_counter() - inicio

inicio = time.perf_counter()
ordem_avl = []
avl._em_ordem(avl.raiz, ordem_avl)
tempo_avl_ordem = time.perf_counter() - inicio


# =========================
# BUSCA
# =========================

img_busca = pacientes[len(pacientes) // 2].id_imagem

inicio = time.perf_counter()
for p in heap.heap:
    if p.id_imagem == img_busca:
        break
tempo_busca_heap = time.perf_counter() - inicio

inicio = time.perf_counter()
abb.buscar(img_busca)
tempo_busca_abb = time.perf_counter() - inicio

inicio = time.perf_counter()
avl.buscar(img_busca)
tempo_busca_avl = time.perf_counter() - inicio


# =========================
# RESULTADOS
# =========================

print("\n===== RESULTADOS =====\n")

print("HEAP")
print(f"Insercao: {tempo_heap_insercao:.6f}")
print(f"Ordem: {tempo_heap_ordem:.6f}")
print(f"Busca: {tempo_busca_heap:.6f}")
print(f"Comparacoes: {heap.comparacoes}\n")

print("ABB")
print(f"Insercao: {tempo_abb_insercao:.6f}")
print(f"Ordem: {tempo_abb_ordem:.6f}")
print(f"Busca: {tempo_busca_abb:.6f}")
print(f"Comparacoes: {abb.comparacoes}")
print(f"Altura: {abb.altura()}\n")

print("AVL")
print(f"Insercao: {tempo_avl_insercao:.6f}")
print(f"Ordem: {tempo_avl_ordem:.6f}")
print(f"Busca: {tempo_busca_avl:.6f}")
print(f"Comparacoes: {avl.comparacoes}")
print(f"Altura: {avl.altura()}")
print(f"Rotacoes: {avl.rotacoes}")


# =========================
# FILA DOS 10 PRIMEIROS
# =========================

print("\n===== FILA DOS 10 PRIMEIROS PACIENTES =====\n")

print("HEAP")
for i, p in enumerate(ordem_heap[:10], 1):
    print(f"{i}. {p.id_imagem} - {p.score:.6f} - {classificar_risco(p.score)}")

print("\nABB")
for i, p in enumerate(ordem_abb[:10], 1):
    print(f"{i}. {p.id_imagem} - {p.score:.6f} - {classificar_risco(p.score)}")

print("\nAVL")
for i, p in enumerate(ordem_avl[:10], 1):
    print(f"{i}. {p.id_imagem} - {p.score:.6f} - {classificar_risco(p.score)}")


# =========================
# SALVAR RESULTADOS.TXT
# =========================

with open("resultados.txt", "w", encoding="utf-8") as f:

    f.write("===== RESULTADOS =====\n\n")

    f.write("HEAP\n")
    f.write(f"Insercao: {tempo_heap_insercao:.6f}\n")
    f.write(f"Ordem: {tempo_heap_ordem:.6f}\n")
    f.write(f"Busca: {tempo_busca_heap:.6f}\n")
    f.write(f"Comparacoes: {heap.comparacoes}\n\n")

    f.write("ABB\n")
    f.write(f"Insercao: {tempo_abb_insercao:.6f}\n")
    f.write(f"Ordem: {tempo_abb_ordem:.6f}\n")
    f.write(f"Busca: {tempo_busca_abb:.6f}\n")
    f.write(f"Comparacoes: {abb.comparacoes}\n")
    f.write(f"Altura: {abb.altura()}\n\n")

    f.write("AVL\n")
    f.write(f"Insercao: {tempo_avl_insercao:.6f}\n")
    f.write(f"Ordem: {tempo_avl_ordem:.6f}\n")
    f.write(f"Busca: {tempo_busca_avl:.6f}\n")
    f.write(f"Comparacoes: {avl.comparacoes}\n")
    f.write(f"Altura: {avl.altura()}\n")
    f.write(f"Rotacoes: {avl.rotacoes}\n\n")

    f.write("===== FILA DOS 10 PRIMEIROS PACIENTES =====\n\n")

    f.write("HEAP\n")
    for i, p in enumerate(ordem_heap[:10], 1):
        f.write(f"{i}. {p.id_imagem} - {p.score} - {classificar_risco(p.score)}\n")

    f.write("\nABB\n")
    for i, p in enumerate(ordem_abb[:10], 1):
        f.write(f"{i}. {p.id_imagem} - {p.score} - {classificar_risco(p.score)}\n")

    f.write("\nAVL\n")
    for i, p in enumerate(ordem_avl[:10], 1):
        f.write(f"{i}. {p.id_imagem} - {p.score} - {classificar_risco(p.score)}\n") 