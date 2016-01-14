#!/usr/bin/env python
# dot2tex --autosize InfiniteNumberOfPrimes.parts.dot > InfiniteNumberOfPrimes.parts.tex; pdflatex InfiniteNumberOfPrimes.parts.tex ; open InfiniteNumberOfPrimes.parts.pdf
import sys,os
name=sys.argv[1]

def runit(command):
    print "running ",command
    os.system(command)

runit("dot2tex --autosize --usepdflatex %s.dot > %s.tex"%(name,name))

import shutil
with open(name+".tex") as old, open(name+".tmp", 'w') as new:
    for line in old:
        if "documentclass" in line:
            line="\documentclass{standalone}\n"
        if "enlargethispage" in line:
            line=""
        new.write(line)

shutil.move(name+".tmp", name+".tex")

runit("pdflatex %s.tex"%name)
runit("open %s.pdf"%name)



