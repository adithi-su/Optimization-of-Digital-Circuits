class HashTable:
	# Create empty bucket list of given size
	def __init__(self, size):
		self.size = size
		self.hash_table = self.create_buckets()
    
	def create_buckets(self):
		return [[] for _ in range(self.size)]
    
	# Insert values into hash map
	def set_val(self, key, val):
		# Get the index from the key
		# using hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			# check if the bucket has same key as
			# the key to be inserted
			if record_key == key:
				found_key = True
				break
		# If the bucket has same key as the key to be inserted,
		# Update the key value
		# Otherwise append the new key-value pair to the bucket
		if found_key:
			bucket[index] = (key, val)
		else:
			bucket.append((key, val))
 
	# Return searched value with specific key
	def get_val(self, key):
		
		# Get the index from the key using
		# hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key being searched
			if record_key == key:
				found_key = True
				break

		# If the bucket has same key as the key being searched,
		# Return the value found
		# Otherwise indicate there was no record found
		if found_key:
			return record_val
		else:
			return -1

	# Remove a value with specific key
	def delete_val(self, key):
		
		# Get the index from the key using
		# hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key to be deleted
			if record_key == key:
				found_key = True
				break
		if found_key:
			bucket.pop(index)
		return

	# To print the items of hash map
	def __str__(self):
		return "".join(str(item) for item in self.hash_table)
	
	def values(self):
		list1 = []
		for key,value in self:
			list1.append[value]
		return list1
    
N = int(input("Enter the number of variables, followed by the variables- "))
v = []
for i in range(N): 
    v.append(input())
n = int(input("Enter the number of cubes - "))
cover = []
for i in range(n): 
    cover.append(input())
print("you have entered: ", end = '')
print(*cover, sep='+')

def make_cof(v,cover):
    cof = {}
    for var in v:
        temp = var + '\''
        f = []
        f_temp = []
        for i in cover:
            # fa
            if i==var:
                f.append(1)
            else:
                if temp not in i:
                    if var not in i:
                        f.append(i)
                    else:
                        f.append(i.translate({ord(var): None}))
                if f == []:
                    f.append(0)
            # fa'
            if i==temp:
                f_temp.append(1)
            else:
                if temp in i:
                    f_temp.append(i.replace(temp,''))
                if var not in i:
                    f_temp.append(i)
                if f_temp == []:
                    f_temp.append(0)
        cof[var] = f
        cof[temp] = f_temp
    return cof

cof = make_cof(v,cover)

def cof(F,v_cof):
    cof = make_cof(v,F)
    if len(v_cof)==1 or (len(v_cof)==2 and v_cof[1]=='\''):
        print('f',v_cof, '=', end='')
        if 1 in cof[v_cof]:
            return '1'
        else:
            return cof[v_cof]
    else:
        curr_cof = cof
        curr_cov = cover
        for i in range(len(v_cof)):
            if v_cof[i] == '\'':
                continue
            if i!=(len(v_cof) - 1) and v_cof[i+1]=='\'':
                index = v_cof[i] + '\''
            else:
                index = v_cof[i]
            curr_cof = make_cof(v,curr_cov) 
            curr_cov = curr_cof[index]
        print('f',v_cof, '=', end='')
        if 1 in curr_cov:
            return '1'
        else:
            return curr_cov  
     
size = 20
unique_table = HashTable(size)
computed_table = HashTable(size)

def FindOrCreateNode(v, lo, hi):
    val_list = unique_table.values()
    val_list.sort(reverse=True) #sort in descending order
    if v==str and len(v)==1: #v is a constant, ex a, b, c
        if unique_table.get_val((v,1,0)) == -1: #constant not in unique table
            val = val_list[0] + 1
            unique_table.set_val((v,1,0), val) 
        else:
            val = unique_table.get_val((v,1,0))
        return val 
    elif lo == hi:
        return lo
    elif unique_table.get_val((v,1,0)) != -1:
        return unique_table.get_val((v,1,0))
    else:
        val = val_list[0] + 1
        unique_table.set_val((v,1,0), val) 
        return val   

def top_var(I):
    val_list = unique_table.values()
    value = val_list.index(I)
    return value[0]

def ITE(I,T,E):
    # Terminal cases
    if I==1:
        return T
    elif I==0:
        return E
    elif T==1 and E==0:
        return I
    elif T==E:
        return T
    
    # if computed table has entry for ITE 
    elif computed_table.get_val((I,T,E)) != -1:
        return computed_table.get_val((I,T,E))
    
    else:
        v = top_var(I)
        v_bar = top_var(I) + '\''
        posfactor = ITE(cof(I,v), cof(T,v), cof(E,v))
        negfactor = ITE(cof(I,v_bar), cof(T,v_bar), cof(E,v_bar))
        R = FindOrCreateNode(v, posfactor, negfactor)
        computed_table.set_val((I,T,E),R)
        return R 


