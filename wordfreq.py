import sys
import string
newfile=open("output.txt","w+")
def compareItems((w1,c1), (w2,c2)):
    if c1 > c2:
        return - 1
    elif c1 == c2:
        return cmp(w1, w2)
    else:
        return 1

def main():
    fname = raw_input("File name: ")
    text = open(fname,'r').read()
    text = string.lower(text)
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = string.replace(text, ch, ' ')
    words = string.split(text)

  
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1

   
    n = input("no of words:")
    items = counts.items()
    items.sort(compareItems)
    for i in range(n):
	sys.stdout = newfile
        print "%-10s%5d" % items[i]

if __name__ == '__main__': main()


