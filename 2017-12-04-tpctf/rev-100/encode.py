for i in range(1,101):
    import builtins, random
    import_lib = getattr(builtins, "__import__")
    pil = import_lib("PIL.Image")
    image_module = pil.Image
    image = image_module.new("RGB", (len("REDACTED"), 1), "white")
    image_buffer = image.load()
    j = 0
    for letter in "REDACTED":
        x = ord(letter)
        rand1 = random.randint(1,256)
        rand2 = random.randint(1,256)
        rand3 = random.randint(1,256)
        rand1i = (rand1/256)
        rand2i = (rand2/256)
        char1 = x*rand1i
        char3 = char1*rand2i
        image_buffer[j,0] = (rand1, rand2, round(char3*10))
        j += 1
    print(image, i)
    image.save("out"+str(i)+".png")