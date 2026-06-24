     def napravi_potez(self, v, c):
         if self.T[v][c] == 0:
             self.T[v][c] = self.igrac
              if self.provjeri_pobjedu(): return "pobjeda"
              self.igrac = 2 if self.igrac == 1 else 1
              if not any(0 in red for red in self.T): return "remi"
              return "nastavi"
         return "nevalidno"

     def provjeri_pobjedu(self):
         for i in range(3):
             if self.T[i][0] == self.T[i][1] == self.T[i][2] != 0: return True
             if self.T[0][i] == self.T[1][i] == self.T[2][i] != 0: return True
         if self.T[0][0] == self.T[1][1] == self.T[2][2] != 0: return True
         if self.T[0][2] == self.T[1][1] == self.T[2][0] != 0: return True
         return False
 
 class IksOksGUI:
     def __init__(self, root):
         self.root = root
         self.root.title("Iks-Oks Postavke")
         self.root.geometry("350x450") # Fiksna veličina za uredniji izgled
         self.root.configure(bg="#f0f8ff") # Svijetla pozadina cijelog prozora
        
         self.igra = IksOks()
        
         # Proširena lista simbola
         self.lista_simbola = ["X", "O", "😊", "😎", "🔥", "❄️", "🚀", "🛸", "🍕", "🍔", "🐱", "🐶", "💎", "⭐", "⚽", "🏀"]
        
         self.izbor_1 = tk.StringVar(root)
         self.izbor_1.set(self.lista_simbola[0])
         self.izbor_2 = tk.StringVar(root)
         self.izbor_2.set(self.lista_simbola[1])
        
         self.prikazi_meni()
     
      def kreiraj_tablu(self):
          self.buttons = [[None for _ in range(3)] for _ in range(3)]
          for v in range(3):
              for c in range(3):
                  self.buttons[v][c] = tk.Button(
                      self.root, text="", font=('Segoe UI Emoji', 28),
                      width=4, height=2, bg="skyblue", activebackground="#a1d6f2",
                      relief="flat", bd=2, command=lambda r=v, col=c: self.klik_na_dugme(r, col)
                  )
                  self.buttons[v][c].grid(row=v, column=c, padx=5, pady=5)

      def klik_na_dugme(self, v, c):
          trenutni_igrac = self.igra.igrac
          simbol = self.simbol_1 if trenutni_igrac == 1 else self.simbol_2
          boja_teksta = "#00008B" if trenutni_igrac == 1 else "#8B0000"
        
          rezultat = self.igra.napravi_potez(v, c)
        
          if rezultat != "nevalidno":
              self.buttons[v][c].config(text=simbol, state="disabled", disabledforeground=boja_teksta)
            
              if rezultat == "pobjeda":
                  messagebox.showinfo("Kraj", f"Pobijedio je igrač {trenutni_igrac} {simbol}!")
                  self.root.destroy()
              elif rezultat == "remi":
                  messagebox.showinfo("Kraj", "Nerešeno je! 😐")
                  self.root.destroy()

if __name__ == "__main__":
    prozor = tk.Tk()
    app = IksOksGUI(prozor)
    prozor.mainloop()
    

'''
#f0f8ff (Alice Blue): Vrlo svijetla, skoro bijela nijansa plave. Koristi se za pozadinu cijelog prozora da bi sve izgledalo prozračno.

white (Bijela): Boja centralne "kartice" u meniju.

#bdd7ee (Svijetloplava): Boja tankog okvira oko menija (onaj highlightthickness).

#ecf0f1 (Clouds): Svijetlo siva boja unutar padajućih menija za izbor smajlija.

skyblue (Nebesko plava): Glavna boja tvojih 9 polja na tabli.

#a1d6f2 (Svijetlo-nebeska): Boja koja se pojavi na polju dok ga igrač drži pritisnutim (activebackground).

#2ecc71 (Smaragdno zelena): Boja dugmeta "Započni Duel". Zelena signalizira kretanje i početak.

#27ae60 (Tamnije zelena): Boja zelenog dugmeta u trenutku klika.

#2c3e50 (Ponoćno plava): Skoro crna, koristi se za glavni naslov "IKS-OKS" i tekstove u meniju radi maksimalne čitljivosti.

#3498db (Bright Blue): Svijetla plava boja kojom piše "Igrač 1" u meniju.

#e74c3c (Alizarin Red): Jarka crvena boja kojom piše "Igrač 2" u meniju.

#00008B (Dark Blue): Boja smajlija/simbola prvog igrača nakon što se postavi na tablu.

#8B0000 (Dark Red): Boja smajlija/simbola drugog igrača nakon što se postavi na tablu.
'''
