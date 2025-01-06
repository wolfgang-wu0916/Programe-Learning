x = int(input("請輸入身分證後9碼"))
x1 = x%10

if x1==1:
   print("吳剛-基隆")
elif x1==2:
     print("吳剛-新北")
elif x1==3:
     print("吳剛-台北")
elif x1==4:
     print("吳剛-桃園")
elif x1==5:
     print("吳剛-新竹")
elif x1==6:
     print("吳剛-苗栗")
elif x1==7:
     print("吳剛-台中")
elif x1==8:
     print("吳剛-彰化")
elif x1==9:
     print("吳剛-台南")
else :
    print("吳剛-嘉義")

sum = x1
quot = x

for n in range(1,9) :
    quot = quot//(10)
    sum = sum + (quot%10)

print("身分證後9碼各數字總合為 :",sum)

if (sum%2)==0:
   print("211-13")
else :
   print("13-211")
