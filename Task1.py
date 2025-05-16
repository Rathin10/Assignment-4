file = open('sample.txt','r')
lines = file.readlines()
count = 0
for line in lines:
    count += 1
    print('Line',count,':',line.strip())
file.close()
