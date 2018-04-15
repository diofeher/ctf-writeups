import struct
import hashlib

def parse(a):
    return "".join(reversed([a[i:i+2] for i in range(0, len(a), 2)]))

version = parse('20000000')
hash_prev_block = parse('0000000000000000002a04ab206fb34125af8d74385dfe30669410d89f6bc794')
hash_merkle_root = parse('edc0ae8ea8e512cfea047d7b521862438e9c9362de58ef1ecf3bc2c8de06d0d4')
datime = parse('5ad1451a')  # 2018-04-14 00:02:34
bits = parse('17502ab7')  # 391129783
nonce = parse('64804c66')  # 1686129766

header_hex = (version + hash_prev_block + hash_merkle_root + datime + bits + nonce)
print(header_hex)
header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
print hash.encode('hex_codec')
print hash[::-1].encode('hex_codec')
final_hash = '0000000000000000000854f801e84750ffa9aaa97e74c36e975df3fa2ad5627c'
print(final_hash)