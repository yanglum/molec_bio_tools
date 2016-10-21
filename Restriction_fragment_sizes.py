# this function calculates the number and sizes of fragments after restriction digest of a plasmid or BAC 

# restfrag(x)
# takes argument x, which is a vector containing list of cut sites
# predicted cut sites can be obtained from http://www.restrictionmapper.org/
# calculates number of fragments and fragment sizes

def restfrag(x):
    size = raw_input("Enter size of plasmid or BAC in bp: ") # assume circular BAC vector
    fragment_sizes = []
    first = x[0]+(int(size)-x[len(x)-1])
    fragment_sizes.append(first)
    for i in range(1,len(x)):
            rest = x[i]-x[i-1]
            fragment_sizes.append(rest)
    list.sort(fragment_sizes)
    print "Number of fragments: %s" % len(fragment_sizes)
    print "Fragment sizes: %s" % fragment_sizes
