score_matrix=[["葉之媛",68,100,85,73,0,0],["吳碇彬",75,80,56,82,0,0],["鐘珣樺",36,80,61,78,0,0],["陳港波",40,45,50,30,0,0],["吳剛",64,95,63,83,0,0]]
#############以上是是初始化 score+matrix資料,編號5攔為總分,編號6列放名次###############################
average=[0]*5
seat=[0]*5
score_matrix2=score_matrix
for i in range(5):
    score_matrix[i][5]=((score_matrix[i][1]+score_matrix[i][2]+score_matrix[i][3])/3)*0.6+score_matrix[i][4]*0.4 ####計算總成績########                                                                                                           
    average[i]=score_matrix[i][5] #####備份總成績,在維備份###########
##################以下是2維排序,請參閱###################################
score_matrix2.sort(key=lambda x:x[5])
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(score_matrix2)

###############以下是一維排序#####################################
average.sort()
average.reverse()
for j in range(5):
   for k in range(5):                                                                                                             
     if(average[j]==score_matrix[k][5]) :####檢查總成績是否相等##########
         score_matrix[k][6]=j+1  #########備份名次至score_matrix######
         seat[j]=k   ########### 備份座號                                                                                                     
for n in range(5):
   
                                                                                                                
     print("第",n+1,"名為",score_matrix[seat[n]] [0],"座號為",seat[n]+1,"總成績為:",average[n])  ####讀取相關資料列印###########
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(score_matrix)
