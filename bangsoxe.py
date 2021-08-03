list=[]
count=0
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                tong=a+b+c+d
                if tong % 10 == 9:
                    count += 1
                    socuoicung=a*1000+b*100+c*10+d
                    list.append(socuoicung)
print(list)
print("cac bien xe tong hop duoc: ",count)
