class Haybonlar:
    def __init__(self,nomi, rangi):
        self.nomi = nomi
        self.rangi = rangi
    def __str__(self):
        return f"{self.nomi}, {self.rangi}"  

class Uy(Haybonlar):
    def __init__(self, nomi, rangi, uyi) :
        super().__init__(nomi, rangi,)
        self.uyi = uyi

    def ch(self):
        print(self.nomi, self.rangi, self.uyi)   
        print("Nomi", self.nomi, "Rangi", self.rangi, "Uyi", self.uyi)
uy1 = Uy ("ayiq","qora","tog")

print(uy1.ch())

class Turi(Haybonlar):
    def __init__(self, nomi, rangi, turi) :
        super().__init__(nomi, rangi,)
        self.turi = turi

    def tt(self):
        print(self.nomi, self.rangi, self.turi)   
        print("Nomi", self.nomi, "Rangi", self.rangi, "Turi", self.turi)
turi1 = Turi ("ayiq","qora","g")

print(turi1.tt())

class Laqabi(Haybonlar):
    def __init__(self, nomi, rangi, laqabi) :
        super().__init__(nomi, rangi,)
        self.laqabi = laqabi

    def tb(self):
        print(self.nomi, self.rangi, self.laqabi)   
        print("Nomi", self.nomi, "Rangi", self.rangi, "Laqabi", self.laqabi)
laqabi1 = Laqabi ("ayiq","qora","givi")

print(laqabi1.tb())