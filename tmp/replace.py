import sys, os

for fname in os.listdir(sys.argv[1]):
    fname = os.path.join(sys.argv[1])
    print(fname, '-'*20)
    fin = open(fname) # open in utf8
    fdat = fin.read()
    fin.close()
    
    # edit file data
    fdat = fdat.replace('पिछली बार', 'पीछले बार')
    
    print(fdat)
    fout = open(fname, 'w')
    fout.write(fdat)
    fout.close()
    print()