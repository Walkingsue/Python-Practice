def nb_year(p0, percent, aug, p):
    percent /= 100 
    years = 0
    while p0 < p:
        p0 = p0 + round(p0 * percent) + aug
        years += 1
    return years

print(nb_year(1500000, 2.5, 10000, 2000000))

print(round(252.8))