import csv

#readFile = open('yourmom.txt')

# numLines = readFile.readlines()

xAccelRaw = []
xAccelCal = []
datas = []
time = []
timediff = []
velocity = []
velocity.insert(0, 0)

with open('/media/gcs-14/D606-E03A/DATALOG.CSV', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        datas.append(line)

for x in range(len(datas)):
    if datas[x][0] != '':
        time.append(datas[x][0])
        timediff.append(((int(datas[x][0])-(int(datas[0][0])-1))/1000))
        xAccelRaw.append(datas[x][1])
        cal = float(xAccelRaw[x])*(-1.085)-26.272
        xAccelCal.append(cal)
    else:
        break

xAccelCal.insert(0, 0)
timediff.insert(0, 0)

for x in range(1, len(xAccelCal)):
    velocity.append(float(velocity[x-1]) + (float(timediff[x])-float(timediff[x-1]))*(float(xAccelCal[x])+ float(xAccelCal[x-1]))/2)

for x in range(len(xAccelCal)):
    print(str(timediff[x]) + '\t' + str(velocity[x]))
csv_file.close()
