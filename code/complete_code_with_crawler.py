import time
from pythonbenchmark import compare, measure

def get_page(url):
 try:
     import urllib
     return urllib.urlopen(url).read()
 except:
     return ""

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index






def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

def lookup(index, keyword):
  if keyword in index:
    return index[keyword]
  else:
    return none

def hashtable_lookup(htable,key):
    bucked = hashtable_get_bucket(htable,key)
    for i in bucked:
        if key in i:
            return i[1]
    else:
        return None


def bad_hash_string (keyword, buckets):
  return ord(keyword[0]) % buckets # output is the bucket (hash) based on the first letter of the keyword

def hash_string(keyword, buckets):
  # this function generates a hash based on the entire word
  s = 0
  for c in keyword:
    s += ord(c)
  return s % buckets

def hashtable_get_bucket(htable,keyword):
  return htable[hash_string(keyword, len(htable))]

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])

def hashtable_update(htable,key,value):
    v = hashtable_lookup(htable,key)
    if v == None:
        hashtable_add(htable,key,value)
    else:
        bucket = hashtable_get_bucket(htable,key)
        for i in bucket:
            if i[0] == key:
                i[1] = value
    return htable

def test_hash_function(func, keys, size):
   results = [0] * size
   keys_used = []
   for w in keys:
       if w not in keys_used:
           hv = func(w, size)
           results[hv] += 1
           keys_used.append(w)
   return results


f = open('words.txt', 'r').read()
words = f.split()
# words = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split() # initialize all the words from the page 'Adventures of Sherlock Holmes'
counts = test_hash_function(bad_hash_string, words, 12) # obtain the counts for the bad hash string
print 'bad hash_string:  ' + str(counts)
# [725, 1509, 1066, 1622, 1764, 834, 1457, 2065, 1398, 750, 1045, 935]
counts = test_hash_function(hash_string, words, 12) # find the distribution for the new function
print 'good hash_string:  ' + str(counts)
# [1363, 1235, 1252, 1257, 1285, 1256, 1219, 1252, 1290, 1241, 1217, 1303]




