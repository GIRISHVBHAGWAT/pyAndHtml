import io 
ofile=io.open('tarkasangraha.txt','r',encoding='utf8')
rfile=ofile.readlines()
wfile=rfile.remove("\n")
print(wfile)
