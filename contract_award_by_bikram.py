import csv
import itertools as it

# open files in read mode
f1=open('contracts.csv','rb')
f2=open('awards.csv','rb')

contractname=[]
status=[]
bidPurchaseDeadline=[]
bidSubmissionDeadline=[]
bidOpeningDate=[]
tenderid=[]
publicationDate=[]
publishedIn=[]
contractName=[]
contractDate=[]
completionDate=[]
awardee=[]
awardeeLocation=[]
Amount=[]





csv_contracts=csv.reader(f1)
csv_awards=csv.reader(f2)


#create list of csv file 
for row in csv_contracts:
	contractname.append(row[0])
	status.append(row[1])
	bidPurchaseDeadline.append(row[2])
	bidSubmissionDeadline.append(row[3])
	bidOpeningDate.append(row[4])
	tenderid.append(row[5])
	publicationDate.append(row[6])
	publishedIn.append(row[7])

for awardrow in csv_awards:
	contractName.append(awardrow[0])
	contractDate.append(awardrow[1])
	completionDate.append(awardrow[2])
	awardee.append(awardrow[3])
	awardeeLocation.append(awardrow[4])
	Amount.append(awardrow[5])


	

		
# find the index of matched 
  
with open('final.csv','wb') as out:
	
	fwriter=csv.writer(out)
	index=[]
	for i in range(0,len(contractname)):
		for j in range(0,len(contractName)):
			if contractname[i]==contractName[j]:
				index.append(i)
	
#	print index


	
#create merged csv	
	fwriter.writerows(it.izip_longest(contractname,status,bidPurchaseDeadline,bidSubmissionDeadline,bidOpeningDate,tenderid,publicationDate,publishedIn,contractDate,completionDate,awardee,awardeeLocation,Amount))

#create list of list of csv
with open('final.csv','rb') as rd:
	temp=[]
	freader=csv.reader(rd)
	for row in freader:
		temp.append(row)
	
#rearrange data in csv
	j=1
	for i in index:
		if i not in range(1,len(index)):
		
			temp[i][8]=temp[j][8]
			temp[i][9]=temp[j][9]
			temp[i][10]=temp[j][10]
			temp[i][11]=temp[j][11]
			temp[i][12]=temp[j][12]
		
				
		
		j+=1

	
#equating the list length
new=[x for x in range(1,11) if x not in index]

for i in new:
	temp[i][8]=' '
	temp[i][9]=' '
	temp[i][10]=' '
	temp[i][11]=' '
	temp[i][12]=' '

#fil
sum=0
for i in index:

	if temp[i][1]=='Closed':
		sum+=int(temp[i][12])
print 'Total Amount of closed contracts:{}'.format(sum)

	
#write final data to csv
writer = csv.writer(open('final.csv', 'wb'))
writer.writerows(temp)
