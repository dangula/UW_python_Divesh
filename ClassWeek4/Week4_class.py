f = open("../resource/Test.txt","r+")


for line in f:
    print line
    
f.write("\nHello\n")

f.close()