from collections import defaultdict

class FamilyForest:

    family = {}
    def make_family(self, s: str) -> None:
        # Create new individual group/Family
        famm = self.family
        famm[s] = 1

    def union(self, s: str, t: str) -> str:
        # Add s and t to make a new family and return representative
        fam = self.family
        parent = ""
        if type(fam[s]) and type(fam[t]) == int:
            xweight = fam[s]
            yweight = fam[t]
            fam[t] = s
            fam[s] = xweight + yweight
            parent = s
        else:
            parent1 = self.find(s)
            parent2 = self.find(t)
            weight1 = fam[parent1]
            weight2 = fam[parent2]
            
            if weight1 > weight2:
                parent = parent1
                fam[parent2] = parent1
                fam[parent1] = weight1 + weight2
            else:
                parent = parent2
                fam[parent1] = parent2
                fam[parent2] = weight1 + weight2
        return parent
                

    def find(self, s: str) -> str:
        fam = self.family
        if isinstance(fam[s], int):
            return s
        else:
            return self.find(fam[s])
            
if __name__ == "__main__":
    
    f = FamilyForest()
        
    for s in ["Ricardo", "Sean", "Maya", "Ishaan", "Chia-Lin"]:
        f.make_family(s)
        # each person should now be their own family representative
        assert f.find(s) == s

    rep = f.union("Sean", "Ishaan")
    var1 = f.find("Sean")
    var2 = f.find("Ishaan")
    print(var1)
    print(var2)
    
    f.union("Maya", "Ishaan")
    f.union("Ricardo", "Chia-Lin")

    # families: {"Sean", "Ishaan", "Maya"}, {"Ricardo", "Chia-Lin"}

    assert f.find("Sean") == f.find("Ishaan") == f.find("Maya")
    assert f.find("Ricardo") == f.find("Chia-Lin")
    assert f.find("Sean") != f.find("Chia-Lin")
