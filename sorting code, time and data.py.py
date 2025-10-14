import pandas as pd
import matplotlib.pyplot as plt
import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:
            break

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def medir_tempo(algoritmo, dados):
    inicio = time.perf_counter()
    algoritmo(dados.copy()) 
    fim = time.perf_counter()
    return fim - inicio


def gerar_dados():
    dados = {
        "pequena_100": random.sample(range(1000), 100),
        "media_1000": random.sample(range(10000), 1000),
        "grande_10000": random.sample(range(100000), 10000), 
        "muito_grande_50000": random.sample(range(100000), 5000)
    }
    return dados


dados_base = gerar_dados()


algoritmos = [
    ("Bubble Sort", bubble_sort),
    ("Merge Sort", merge_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort)
]

resultados = []


for nome, func in algoritmos:
    for tamanho, dados in dados_base.items():
        tempo = medir_tempo(func, dados)
        resultados.append({"Algoritmo": nome, "Tamanho de Entrada": tamanho, "Tempo (s)": tempo})


df_resultados = pd.DataFrame(resultados)


print(df_resultados)


plt.figure(figsize=(10, 6))


tamanho_map = {"pequena_100": 100, "media_1000": 1000, "grande_10000": 10000, "muito_grande_50000": 5000}


for nome in df_resultados["Algoritmo"].unique():
    dados_algoritmo = df_resultados[df_resultados["Algoritmo"] == nome]
    dados_algoritmo["Tamanho de Entrada Numérico"] = dados_algoritmo["Tamanho de Entrada"].map(tamanho_map)
    plt.plot(dados_algoritmo["Tamanho de Entrada Numérico"], dados_algoritmo["Tempo (s)"], label=nome)

plt.title("Comparação de Performance dos Algoritmos de Ordenação")
plt.xlabel("Tamanho da Entrada")
plt.ylabel("Tempo de Execução (Segundos)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()