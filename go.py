#! python

# Set the topics you want to work on here.
Files=["abstract-algebra", "category-theory", "topology"]

import subprocess

def go(dothis):
    print(dothis)
    return subprocess.getoutput(dothis)

# For now, leave cards as avery5371, but shift to onecard on compilation.
Ftex=[i + ".tex" for i in Files]
for i in Ftex:
    go("sed 's/avery5371/onecard/' <" + i + " > tmp."+i)
    go("pdflatex tmp."+i)

Count=go("egrep '(\\\\Card|begin.flashcard)' " + " ".join(Ftex)  + " | wc -l")
Count=int(Count)-len(Files) #strip the first copyright/attribution card
print("--------------------\n\t"+str(Count)+" cards.\n--------------------")

go("rm counts; for i in `seq 1 2 " + str(2*Count-2) + "`; do echo $i >> counts; done")
Pages=go("shuf counts | awk '{print $1 \",\" $1+1}'| tr '\n' ','|sed 's/,$//'")

go("rm -f mid.pdf mid1.pdf")
go("pdfjam  " + "  ".join([" tmp."+i +".pdf " for i in Files]) + " 3- -o mid1.pdf")
go("pdfjam mid1.pdf \"" + Pages + "\" --no-tidy -o mid.pdf")
go("pdfcrop --clip mid.pdf cards.pdf")
