def prikazi_meni(self):
        # Glavni kontejner sa efektom kartice
        self.frame_meni = tk.Frame(self.root, bg="white", highlightbackground="#bdd7ee", highlightthickness=2, padx=30, pady=30)
        self.frame_meni.place(relx=0.5, rely=0.5, anchor="center") # Centriranje na ekranu

        # Naslov
        tk.Label(self.frame_meni, text="🎮 IKS-OKS", font=("Verdana", 20, "bold"), bg="white", fg="#2c3e50").pack(pady=(0, 20))

        # Sekcija za Igrača 1
        tk.Label(self.frame_meni, text="Igrač 1:", font=("Arial", 11, "bold"), bg="white", fg="#3498db").pack()
        self.menu1 = tk.OptionMenu(self.frame_meni, self.izbor_1, *self.lista_simbola)
        self.stil_menija(self.menu1)
        self.menu1.pack(pady=(0, 15))

        # Sekcija za Igrača 2
        tk.Label(self.frame_meni, text="Igrač 2:", font=("Arial", 11, "bold"), bg="white", fg="#e74c3c").pack()
        self.menu2 = tk.OptionMenu(self.frame_meni, self.izbor_2, *self.lista_simbola)
        self.stil_menija(self.menu2)
        self.menu2.pack(pady=(0, 25))

        # Dugme za početak
        btn_start = tk.Button(
            self.frame_meni, text="Započni Duel", font=("Arial", 12, "bold"),
            bg="#2ecc71", fg="white", activebackground="#27ae60", activeforeground="white",
            padx=20, pady=10, bd=0, cursor="hand2", command=self.pokreni_igru
        )
        btn_start.pack()

    def stil_menija(self, menu):
        menu.config(bg="#ecf0f1", fg="#2c3e50", font=("Arial", 10), width=10, bd=1, relief="flat")
        menu["menu"].config(bg="white", fg="#2c3e50", font=("Arial", 10))

    def pokreni_igru(self):
        if self.izbor_1.get() == self.izbor_2.get():
            messagebox.showwarning("Ups!", "Izaberite različite simbole!")
            return
        
        self.simbol_1 = self.izbor_1.get()
        self.simbol_2 = self.izbor_2.get()
        
        self.frame_meni.destroy()
        self.root.geometry("380x420") # Malo veće za samu tablu
        self.root.title(f"{self.simbol_1} vs {self.simbol_2}")
        self.kreiraj_tablu()