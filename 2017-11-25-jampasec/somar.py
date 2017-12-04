# Write-up here: https://www.youtube.com/watch?v=p0xy4M5Zeqs

import telnetlib
import heapq

def somar(lst):
    heapq.heapify(lst)
    s = 0
    while len(lst) > 1:
        first = heapq.heappop(lst)
        second = heapq.heappop(lst)
        value = first + second
        s += value
        heapq.heappush(lst, value)
    return s

def conectar():
    conn = telnetlib.Telnet('138.197.10.170', '1313')
    conn.read_until('start:')
    conn.write('start')
    for i in range(1000):
        print conn.read_until('(I):')
        lst = eval(conn.read_until(']'))
        conn.write(str(somar(lst)))
        print conn.read_some()
    
    
    print conn.read_some()
    print conn.read_some()

conectar()