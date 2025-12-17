"""
Natural sonning raqamlari soni va raqamlari yig'indisini
hisoblovchi DigitCountSum nomli funksiya hosil qiling.
"""
def DigitCountSum(son):
    natija = 0
    son2=son
    xona_soni= 0
    while son2>0:
        xona_soni +=1 
        natija += son2 % 10 
        son2= son2 // 10
    return xona_soni, natija
print(DigitCountSum(741))
        


