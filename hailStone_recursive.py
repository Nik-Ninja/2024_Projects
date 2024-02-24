def generate_hail_stone_rec(n):
    print(n)
    if n==1:
        return
    elif n%2==0:
        generate_hail_stone_rec(n//2)
    else:
        generate_hail_stone_rec(3*n+1)


generate_hail_stone_rec(7)