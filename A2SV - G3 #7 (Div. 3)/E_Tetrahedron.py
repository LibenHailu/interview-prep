from collections import defaultdict


adj = defaultdict(list)
adj["D"].append("A")
adj["D"].append("B")
adj["D"].append("C")
adj["A"].append("D")
adj["A"].append("B")
adj["A"].append("C")
adj["B"].append("A")
adj["B"].append("D")
adj["B"].append("C")
adj["C"].append("A")
adj["C"].append("B")
adj["C"].append("D")

def dp()