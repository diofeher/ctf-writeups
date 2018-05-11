def pkcs7_padding(key, BLOCK_SIZE=16):
    pad = BLOCK_SIZE - len(key)
    res = key.encode('hex') + str(pad).zfill(2) * pad
    return res.decode('hex')


assert pkcs7_padding("YELLOW SUBMARINE", BLOCK_SIZE=20) == "YELLOW SUBMARINE\x04\x04\x04\x04"
