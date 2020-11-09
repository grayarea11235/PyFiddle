import feedparser
import pprint
from urllib.request import urlopen
import gzip

harmontown_url = 'http://feeds.feedburner.com/HarmontownPodcast'
#url = "http://download.thinkbroadband.com/10MB.zip"
skeptics_guide_url = "https://feed.theskepticsguide.org/feed/rss.aspx?feed=sgu"

class RssItemInfo:
    pass


def get_file_size(url):
    u = urlopen(url)
    meta = u.info()
    file_size = int(meta['Content-Length'])

    return file_size


def download_url(url, file_n):
    print(url)
    
    #file_name = url.split('/')[-1]
    file_name = file_n

    print(file_name)
    u = urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta['Content-Length'])
    #    file_size = int(meta.getheaders("Content-Length")[0])
    print("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status)

    f.close()

    return file_name, file_size

def get_file_sizes():
    pass


def compress_file(file_name):
    input = open(file_name, 'rb')
    s = input.read()
    input.close()

    output = gzip.GzipFile(file_name + ".gz", 'wb')
    output.write(s)
    output.close()
    
    print("Compress done")


def get_report(rss_url):
    feed = feedparser.parse(rss_url)

    entries = feed['entries']
    num_entries = len(feed['entries'])

    print("num_entries = {num_entries}".format(num_entries = num_entries)) 
   
    rss_info = []

    for entry in entries:
        print(entry['title'])
        
        file_info = "File = {f} Length = {l} Type = {t}".format(f=entry['enclosures'][0].href, 
                l=entry['enclosures'][0].length, t=entry['enclosures'][0].type)

        print(file_info)
        print(entry['description'])
#        print(entry['pubDate'])
        print(' -------------------------------------------------------------- ')


def main():
    print('In main')
    d = feedparser.parse(url)
#    print(d)
#    print(d['feed']['title'])
    #pprint.pprint(d['entries'][0]['links'][0]['href'])

    ents = d['entries']
    num_ents = len(d['entries'])
    print(num_ents)
    total = 0
    for ent in ents:
        #print(ent['links'][0]['href'])
        file_url = ent['links'][0]['href']
        file_name = 'Harmontown-' + str(num_ents) + '-' + ent['title'] + '.mp3'
        print(file_name)

        num_ents = num_ents - 1
#        file_size = get_file_size(file_url)
        file_name, downloaded_size = download_url(file_url, file_name)

#        compress_file(file_name)
        
        #print(file_size)

        #total += file_size

    #print(total)    
        
    #fileurl = d['entries'][0]['links'][0]['href']
    #print(get_file_size(fileurl))


    #    download_url(fileurl)
    #    urllib.request.urlretrieve(url, 'test.mp3')
    
#    for entry in d['entries']:
#        print(entry['title'])
    
#    print(pprint.pprint(d))
    
if __name__ == '__main__':
    get_report(harmontown_url)
    #get_report(skeptics_guide_url)
    #main()
