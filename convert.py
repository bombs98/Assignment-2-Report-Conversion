f = open("data.csv", "r")

for line in f.readlines():
    print(line)
    
f.close()
