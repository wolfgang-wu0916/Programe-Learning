for excel in range(10):  ##10筆資料圈數
  print("*************************************第",excel+1,"測試*******************************************")
  num=int(input("請輸入資料量個數: "))
  g = [0]*num
  for u in range(num):
    g[u]=-3*u+1  ##製造指定資料
  print("原始資料排序前", g)
  print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
  counter=0
  for i in range(num-1):  ##外迴圈數
      for j in range(num-i-1):  ##內迴圈數
        if g[j] > g[j+1]:  #置換條件
           tmp=g[j]      ##置換
           g[j]=g[j+1]
           g[j+1]=tmp
           counter=counter+1   #比大小次數累計
        else :
           counter=counter+1  #比大小次數累計
  print("氣泡排序後結果:====>")
  print("排序後", g) 
  print("氣泡排序法比大小次數總計: ",counter)
  print("================================================================")

  n = [0]*num
  for uu in range(num):
    n[uu]=-3*uu+1   ##製造指定資料
  counter=0
  for k in range(num-1):
    min_index = k   #指定min_index
    for jj in range(min_index+1, num):  ##指定min_index後的工作
        if n[min_index] > n[jj] :  #min_index內與後數比較大
             min_index=jj  ##min_index移交
             counter=counter+1 #比大小次數累計 
        else:
             counter=counter+1    #比大小次數累計
    if k != min_index:  ##
        
        tmp=n[k]
        n[k]=n[min_index]
        n[min_index]=tmp
  print("選擇排序後結果:====>")
  print("排序後", n)      
  print("選擇排序法比大小次數總計: ",counter)
print("21113吳剛")  
