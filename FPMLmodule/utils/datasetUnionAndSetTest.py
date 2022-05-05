
def datasetUASTest(datasets):
    print("\n"+(" "*45)+"Dataset Check")
    unionSet = set()
    interSet = set()
    sets = []
    for ds in datasets:
        dsSet = set()
        for _, labels in ds.as_numpy_iterator():
            for label in labels:
                parseLabel = label.decode('utf-8')
                dsSet.add(parseLabel)
        sets.append(dsSet)
        unionSet = unionSet.union(dsSet) 
        interSet = interSet.intersection(dsSet) 
        
    print('Union of splitted ds subject: {}, intersaction: {}'.format(len(unionSet), len(interSet)))