print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$二分搜尋法實作$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
for k in range(11) :
  print("********************第",k+1,"次測試********************************")
  length=int(input("請輸入資料長度:"))
  n = [0]*length
  for u in range(length) :
      n[u]=u*u  ##製造資料
  left = 0  ##左始點
  right = length-1  ##右始點  
  COUNTER=0
  target = int(input("輸入目標值: "))
  while left<=right:       ##對半分割條件
    mid = int((left+right)/2)   ##取左右中位數
    if n[mid] == target:    ##找到目標
       COUNTER=COUNTER+1   ##對折數累計
       print("在第", mid + 1, "位址找到", target)
       print("運算次數: ",COUNTER)
       break
    elif n[mid]>target:  ##取左半段
       right=mid-1 ####對折數累計
       COUNTER=COUNTER+1 ##對折數累計    
    elif n[mid]<target:    ##重訂左端點
       left = mid+1   ##重訂左端點
       COUNTER=COUNTER+1  ##對折數累計
    if(right<left):    ###找不到目標條件
    
      print("找不到",target)
      print("運算次數: ",COUNTER)
print("21113吳剛")
