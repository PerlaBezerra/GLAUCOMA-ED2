import matplotlib.pyplot as plt

estruturas = ["HEAP", "ABB", "AVL"]

tempo_insercao = [0.001121, 0.002092, 0.007571]
tempo_ordenacao = [0.005470, 0.000210, 0.000208]
tempo_busca = [0.000001, 0.000193, 0.000135]

comparacoes = [17578, 10880, 8938]
altura = [0, 25, 12]
rotacoes = [0, 0, 688]

fig, axs = plt.subplots(2, 3, figsize=(15, 8))

# Função para colocar valores em cima das barras
def add_labels(ax, bars):
    ax.bar_label(bars, fmt="%.6f", fontsize=8)

# ===== 1 - Inserção =====
bars = axs[0, 0].bar(estruturas, tempo_insercao)
axs[0, 0].set_title("Tempo de Inserção")
add_labels(axs[0, 0], bars)

# ===== 2 - Ordenação =====
bars = axs[0, 1].bar(estruturas, tempo_ordenacao)
axs[0, 1].set_title("Tempo de Ordenação")
add_labels(axs[0, 1], bars)

# ===== 3 - Busca =====
bars = axs[0, 2].bar(estruturas, tempo_busca)
axs[0, 2].set_title("Tempo de Busca")
add_labels(axs[0, 2], bars)

# ===== 4 - Comparações =====
bars = axs[1, 0].bar(estruturas, comparacoes)
axs[1, 0].set_title("Comparações")
axs[1, 0].bar_label(bars)

# ===== 5 - Altura =====
bars = axs[1, 1].bar(estruturas, altura)
axs[1, 1].set_title("Altura da Estrutura")
axs[1, 1].bar_label(bars)

# ===== 6 - Rotações =====
bars = axs[1, 2].bar(estruturas, rotacoes)
axs[1, 2].set_title("Rotações (AVL)")
axs[1, 2].bar_label(bars)

plt.tight_layout()
plt.savefig("dashboard_resultados.png")
plt.show()