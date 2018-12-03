import anytree
from anytree.exporter import DotExporter
from collections import Counter

def solve(N,M,edges,queries):
    nodes = dict()
    ans = []
    for a, b in edges:
        node_a = nodes.get(a)
        if not node_a:
            node_a = anytree.Node(a)
            nodes[a] = node_a 
        
        node_b = nodes.get(b)
        if not node_b:
            nodes[b] = anytree.Node(b, parent=node_a)
    
    for a, b in queries:
        anc_a = nodes[a].__repr__()[7:-2].split('/')
        anc_b = nodes[b].__repr__()[7:-2].split('/')
        counter = Counter(anc_a + anc_b)
        resp = len([i for i in counter.viewvalues() if i > 1])
        ans.append(resp)
    # Solution here, ans = array of answers to each of the queries
    # DotExporter(nodes[b].root).to_picture("nodes.png")
    return '\n'.join(map(str,ans)).strip()

    
import ssl, socket

class Connect(object):
    def __init__(self, host, port):
        self.context = ssl.create_default_context()
        self.conn = self.context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=host)
        self.conn.connect((host, port))
        self.f = self.conn.makefile('rwb', 0)
    def __enter__(self):
        return self.f
    def __exit__(self, type, value, traceback):
        self.f.close()

with Connect('programming.pwn2.win', 9003) as f:
    inew,M = 0,0
    edges = list()
    queries = list()
    for il,line in enumerate(f):
        line = line.strip()
        print('received line %d: %s' % (il,line))
        
        if b'CTF-BR{' in line or b'WRONG' in line: break
            
        if il==inew:
            N,M = map(int,line.split())
            edges = list()
            queries = list()
        elif il<=inew+N:
            a,b = line.split()
            edges.append((a.strip(),b.strip()))
        elif il<=inew+N+M:
            a,b = line.split()
            queries.append((a.strip(),b.strip()))
        
        if il==inew+N+M:
            ans = solve(N,M,edges,queries)
            # import pdb; pdb.set_trace()

            f.write((ans+'\n').encode('utf-8'))
            # print('sending line ' + ans)  # for debugging purposes
            
            inew = il+1
