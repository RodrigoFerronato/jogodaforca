import tkinter as tk
from tkinter import messagebox
import random

class JogoForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.palavra_secreta = self.escolher_palavra()
        self.letras_corretas = []
        self.letras_erradas = []
        self.tentativas = 6

        self.label_palavra = tk.Label(root, text=self.mostrar_palavra(), font=("Helvetica", 20))
        self.label_palavra.pack(pady=20)

        self.label_tentativas = tk.Label(root, text=f"Tentativas restantes: {self.tentativas}", font=("Helvetica", 14))
        self.label_tentativas.pack(pady=10)

        self.label_letras_erradas = tk.Label(root, text="Letras erradas: ", font=("Helvetica", 14))
        self.label_letras_erradas.pack(pady=10)

        self.entry_letra = tk.Entry(root, font=("Helvetica", 14))
        self.entry_letra.pack(pady=10)
        self.entry_letra.bind("<Return>", self.verificar_letra)

        self.button_tentar = tk.Button(root, text="Tentar", command=self.verificar_letra, font=("Helvetica", 14))
        self.button_tentar.pack(pady=10)

    def escolher_palavra(self):
        lista_palavras = ["python", "desenvolvimento", "programacao", "jogo", "computador"]
        return random.choice(lista_palavras)

    def mostrar_palavra(self):
        return ' '.join([letra if letra in self.letras_corretas else '_' for letra in self.palavra_secreta])

    def verificar_letra(self, event=None):
        palpite = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if not palpite.isalpha() or len(palpite) != 1:
            messagebox.showwarning("Entrada inválida", "Por favor, digite uma única letra.")
            return

        if palpite in self.letras_corretas or palpite in self.letras_erradas:
            messagebox.showwarning("Letra repetida", "Você já tentou essa letra. Tente outra.")
            return

        if palpite in self.palavra_secreta:
            self.letras_corretas.append(palpite)
        else:
            self.letras_erradas.append(palpite)
            self.tentativas -= 1

        self.label_palavra.config(text=self.mostrar_palavra())
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
        self.label_letras_erradas.config(text=f"Letras erradas: {', '.join(self.letras_erradas)}")

        if set(self.letras_corretas) == set(self.palavra_secreta):
            messagebox.showinfo("Parabéns!", f"Você adivinhou a palavra: {self.palavra_secreta}")
            self.reset_game()
        elif self.tentativas == 0:
            messagebox.showinfo("Que pena!", f"Você perdeu. A palavra era: {self.palavra_secreta}")
            self.reset_game()

    def reset_game(self):
        self.palavra_secreta = self.escolher_palavra()
        self.letras_corretas = []
        self.letras_erradas = []
        self.tentativas = 6
        self.label_palavra.config(text=self.mostrar_palavra())
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
        self.label_letras_erradas.config(text="Letras erradas: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoForca(root)
    root.mainloop()
