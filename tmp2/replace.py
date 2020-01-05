import sys, os

for fname in os.listdir(sys.argv[1]):
    if fname == 'replace.py': continue
    fname = os.path.join(sys.argv[1], fname)
    print(fname, '-'*20)
    fin = open(fname, encoding='utf-8') # open in utf8
    fdat = fin.read()
    fin.close()

    # edit file data
    fdat = fdat.replace('पीछले बार', 'पिछली बार')

#    print(fdat)
    fout = open(fname, 'w', encoding='utf-8')
    fout.write(fdat)
    fout.close()
#    print()
