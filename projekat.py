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
