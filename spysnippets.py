import random
import string

def gen_doc():
	return (''.join(random.choice(string.ascii_lowercase)+' ' for _ in range(501)))
#adding stuff!
def answer(document, searchTerms):
	#need to be able to quickly find a value from a list
	def binsearch(x, lst):
		if(len(lst) == 1):
			# print("returning... %s" % lst[0])
			return lst[0]
		mid = int(len(lst)/2)
		lsta = lst[:mid]
		lstb = lst[mid:]
		# print("list a: %s \t list b: %s" % (lsta, lstb))
		if((abs(x - lsta[len(lsta)-1])) < (abs(x-lstb[0]))):
			return binsearch(x, lsta)
		else:
			return binsearch(x, lstb)
			
	#parse document, get tokens
	tokens = document.split()
	#get locations in document for all search terms
	buckets = {k: [] for k in searchTerms}
	testkey = searchTerms[0]
	count = 0
	for i in tokens:
		if (i in buckets):
			buckets[i].append(count)
		count+=1
	print(buckets)
    
    # Now we have bunch of buckets with all the terms' locations.
    # Let's find a set for a single bucket that represents the 
    # distance to the nearest next required term for each term
    
    # set each var to have a max distance of 501 (this is above the max limit anyway)
	distances = []
	distance_records = []
	curr_distances = {k: 501 for k in searchTerms}
	print("************************************")
	count = 0
	for val in buckets[testkey]:  # for each value in the test bucket
		curr_distances[testkey] = val
		for key in buckets:       #we want to search the other buckets
			print("Searching key %s" % key)
			if(key == testkey):
				print("skipping...")
				continue 				#except the test bucket
			else:
				# get closest value to val from the other buckets, find a candidate solution!!
				curr_distances[key] = binsearch(val, buckets[key])
				
				print("CURRENT DISTANCE: %s" % curr_distances[key])
		for (key, val) in curr_distances.items():
			distances.append(val)
		print("DISTANCE %s: "  % distances)
		distance_records.append(distances)
		distances = []
		curr_distances = {k: 501 for k in searchTerms}
    # end with an array of tuples representing sets with the smallest possible distance for each key in the test bucket
    
	# need to sort each tuple
	for i in distance_records:
		i.sort()
	
	#tuples are sorted, now we find the shortest by doing max - min and taking the smallest
	smallest = 501 #pls no
	smallest_tuple = []
	for i in distance_records:
		temp = i[0] - i[len(i)-1]
		if( temp < smallest):
			smallest = temp
			smallest_tuple = i
	print("**SMALLEST TUPLE: %s ***" % smallest_tuple)
	#we have the smallest distance, and its tuple, now we need to return the sub-list between the min and max
	return tokens[smallest_tuple[0]: smallest_tuple[len(smallest_tuple)-1]+1] # done!


print(answer("a b c d a", ['a','c','d']))
print(answer("many google employees can program", ["google", "program"]))
#print(answer(gen_doc(), ['a','c','d']))
