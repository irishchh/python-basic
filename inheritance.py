class Cricket:
    def __init__(self, country, playedhowmany, wins):
        self.country = country
        self.playedhowmany = playedhowmany
        self.wins = wins
        
    def Icc(self):
        print(f"{self.country} National cricket has played on {self.playedhowmany}")


class Worldcup(Cricket):
    def Worldcup(self):
        print(f"{self.country}won the Icc {self.wins} in Icc")

    
def main():
    India = Worldcup("India", "Austrilia", 5)
    India.Icc()
    India.Worldcup()


        
        
    