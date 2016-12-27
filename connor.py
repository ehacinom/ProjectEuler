# write way more partitions into a file
import ast

def memo(f):
    cache = {}
    def wrap(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return wrap

def writepartitions(x = 10, fp = '078_partitions2.txt'):
    with open(fp, 'w') as f:
        # zero
        f.write("(0,1)")
        for n in xrange(1, x+1):
            a = partition(n)
            b = ",(" + str(n) + "," + str(a) + ")"
            f.write(b)

# saving the 10k I wrote to memory to file 078_partitions.txt
#writepartitions(10000)

def readpartitions(fp = '078_partitions.txt'):
    with open(fp, 'r') as f:
        partitions = ast.literal_eval('({0})'.format(f.read()))
    return partitions

def partition_script(x=0, y=0, fp='078_partitions-.txt'):
    pre0 = readpartitions('078_partitions50000.txt')
    prev = readpartitions(fp)
    
    # new partition
    def partition(n):
        # solved
        if n < 50001:
            if n < 0: return 0
            elif n == 0: return 1
            return pre0[n][1]
        elif n < x:
            return prev[n-50000][1]
        
        # unsolved
        p = 0
        for k in xrange(1, n+1):
            if k % 2: i = 1
            else: i = -1
            a, b = n - k*(3*k-1)/2, n - k*(3*k+1)/2
            aa, bb = partition(a), partition(b)
            #print a, b, aa, bb
            p += i*(aa+bb)


        # print "whoopee", n, p # only prints on numbers that haven't been run
        return p
    
#     # new memoization
#     for n in xrange(x, y):
#         a = partition(n)
#         if a % 1000000 == 0:
#             print n, a
#             break
#     print n, a
    
    # new memo
    with open(fp, 'a') as f:
        for n in xrange(x+1, y+1):
            a = partition(n)
            b = ",(" + str(n) + "," + str(a) + ")"
            f.write(b)