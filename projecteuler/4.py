def is_pal(pal):
    return pal == pal[::-1]
    
print max([x*y for x in range(1,1000) for y in range(1,1000) if is_pal(str(x*y))])