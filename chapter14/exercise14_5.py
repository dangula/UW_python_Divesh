
import urllib

conn = urllib.urlopen('http://www.uszip.com/zip/98004')
for line in conn.fp:
    print line.strip()