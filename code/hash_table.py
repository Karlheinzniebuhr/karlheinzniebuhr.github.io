import time
from pythonbenchmark import compare, measure

def add_to_index(index,keyword,url):
   for entry in index:
       if entry[0] == keyword:
           entry[1].append(url)
           return
   index.append([keyword,[url]])

def make_string(p):
   s=""
   for e in p:
       s = s + e
   return s

def make_big_index(size):
  index = []
  letters = ['a','a','a','a','a','a','a','a']
  while len(index) < size:
    word = make_string(letters)
    add_to_index(index, word, 'fake')
    for i in range(len(letters) - 1, 0, -1):
      if letters[i] < 'z':
        letters[i] = chr(ord(letters[i])+ 1)
        break
      else:
        letters[i] = 'a'
  return index






def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

def lookup(index, keyword):
   for entry in index:
       if entry[0] == keyword:
           return entry[1]
   return None

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
  return s % buckets # modulus performed here

def hashtable_get_bucket(htable,keyword):
  bucket = htable[hash_string(keyword, len(htable))]
  # print('returning bucket '+str(bucket))
  return bucket

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


# f = open('words.txt', 'r').read()
# words = f.split() # initialize all the words from the page 'Adventures of Sherlock Holmes'
# counts = test_hash_function(bad_hash_string, words, 12) # obtain the counts for the bad hash string
# print('bad hash_string:  ' + str(counts))
# # [725, 1509, 1066, 1622, 1764, 834, 1457, 2065, 1398, 750, 1045, 935]
# counts = test_hash_function(hash_string, words, 12) # find the distribution for the good hash function
# print('good hash_string:  ' + str(counts))
# # [1363, 1235, 1252, 1257, 1285, 1256, 1219, 1252, 1290, 1241, 1217, 1303]


index100000 = make_big_index(100000)
# compare_function(function1, function2, number_of_tests, htable, lookup_key)
compare(lookup, hashtable_lookup, 10, index100000, 'udacity')
