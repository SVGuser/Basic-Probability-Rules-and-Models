pmb = float(input().strip())
pab = float(input().strip())
p1 = float(input().strip())

# Probability of meeting during travel
meet_during_travel = (pmb * pab) + ((1 - pmb) * (1 - pab))

# Probability of meeting only at the lake in the rain
prs = p1 * (1 - meet_during_travel)

# Print result rounded to six decimal places
print(f"{prs:.6f}")
