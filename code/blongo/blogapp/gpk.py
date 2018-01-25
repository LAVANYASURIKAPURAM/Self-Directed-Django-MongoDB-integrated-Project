import csv

def fitem(item):
    item=item.strip()
    try:
        item=float(item)
    except ValueError:
        pass
    return item        

path = r'C:\Users\surikapuraml\Desktop\vphh\blongo\blogapp\Tesla_SRD_MonitorModes_IBP.csv'
with open(path, 'rb') as csvin:
    reader=csv.DictReader(csvin)
    data={k.strip():[fitem(v)] for k,v in reader.next().items()}
    for line in reader:
        for k,v in line.items():
            k=k.strip()
            data[k].append(fitem(v))
print data
for i in range(0,79):
    print data['\xef\xbb\xbf"Requirement_ID"'][i]
    print data['IsRequirement'][i]
    print data['Created By'][i]
    print data['Created On'][i]
    print data['Last Modified By'][i]
    print data['Last Modified On'][i]
    print data['Object Text'][i]

