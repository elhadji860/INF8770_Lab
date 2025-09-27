import pandas as pd
import matplotlib.pyplot as plt
import LZW_compress as lzw
import LZ77_compress as lz77
import huffman_compress as huffman
import arithmetical_compress as art
import time

def presenter_resultats(resultats, titre="Résultats de compression"):

    df = pd.DataFrame(resultats)
    
    print("\n=== " + titre +  "===")
    print(df.to_string(index=False))  # tableau propre
    
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    fig.suptitle(titre, fontsize=14, fontweight="bold")
    
    # Graphique 1 : Taux de compression
    axes[0].bar(df["méthode"], df["taux"], color="skyblue")
    axes[0].set_title("Taux de compression (%)")
    axes[0].set_ylabel("Taux (%)")
    axes[0].set_xticklabels(df["méthode"], rotation=30, ha="right")
    
    # Graphique 2 : Temps d’exécution
    axes[1].bar(df["méthode"], df["temps"], color="salmon")
    axes[1].set_title("Temps d'exécution (s)")
    axes[1].set_ylabel("Temps (s)")
    axes[1].set_xticklabels(df["méthode"], rotation=30, ha="right")
    
    plt.tight_layout()



# fichier texte

NATURAL_TEXT_PATH = "C:/Users/elhad/Desktop/INF8770_Lab/Tp1/assets/text_natural_1.txt"
f= open(NATURAL_TEXT_PATH, "r")

textString = f.read()

startTimelzw = time.time()
compressLzw = lzw.compress(textString)
exectimelzw = float(time.time() - startTimelzw)
taux_lzw = len(compressLzw)/len(textString)

startTimelz77 = time.time()
compressLz77 = lz77.compress(textString, len(textString)/10)
exectimelz77 = float(time.time() - startTimelz77)
taux_lz77 = len(compressLz77)/len(textString)

startTimeHuffman = time.time()
compressHuffman = huffman.compress(textString)
exectimeHuffman = float(time.time() - startTimeHuffman)
taux_Huffman = len(compressHuffman)/len(textString)

startTimeArithmetical = time.time()
compressArithmetical = art.compress(textString)
exectimeArithmetical = float(time.time() - startTimeArithmetical)
taux_Arithmetical = len(compressArithmetical)/len(textString)

resultats = [
    {"méthode": "LZW", "taux": taux_lzw, "temps": exectimelzw},
    {"méthode": "LZ77", "taux": taux_lz77, "temps": exectimelz77},
    {"méthode": "Huffman", "taux": taux_Huffman, "temps": exectimeHuffman},
    {"méthode": "Arithmetique", "taux": taux_Arithmetical, "temps": exectimeArithmetical}
]

presenter_resultats(resultats, "Comparaison des méthodes de compression fichier text")

f.close()