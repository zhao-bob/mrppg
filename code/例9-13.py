import pickle

with open('test.txt') as src, open('test_pickle.dat', 'wb') as dest:
    for line in src:
        pickle.dump(line, dest)
        
with open('test_pickle.dat', 'rb') as fp:
    while True:
        try:
            print(pickle.load(fp))
        except:
            break
