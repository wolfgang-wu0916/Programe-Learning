print("準備輸入學生各項考察分數: ")
n = int(input("請輸入學生人數: "))
maxscore = 0.0
for i in range(1,n+1) :
        scoresum=0.0
        score=0
        print("請輸入座號第",i,"位學生成績:")
        print("請輸入座號第",i,"位學生姓名:")
        name = input("請在此輸入姓名====> ")
        for j in range(1,5) :
             if(j<=3) :
        
                print("請輸入第",j,"次考察成績: ")
                score=int(input("請在此輸入====> "))
                scoresum=scoresum+(score*0.6)/3
             else :

                print("請輸入第",j,"次考察成績: ")
                score=int(input("請在此輸入====> "))
                scoresum=scoresum+score*0.4
        print("座號第",i,"位學生","姓名為",name,"的總成績為====>: ",scoresum)

        if(maxscore <=scoresum) :
            maxscore=scoresum
            maxseat=i
            maxname=name
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("座號第",maxseat,"位學生","姓名為",maxname,"成績是總平均的最高分====>: ",maxscore)                          
