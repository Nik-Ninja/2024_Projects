
# hail_stone_sequence=[]
def generate_hail_stone(n):
    while True:
        print(n)
        if(n==1):
            break
        if n % 2 == 0:
            n//=2
        else:
            n=3*n+1


generate_hail_stone(7)
# print(hail_stone_sequence)