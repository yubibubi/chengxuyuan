import random
import time
import re
import os
# 生成“图标”库
def lists(num):
    x=set("123456789abcdefghj")
    a=[x.pop() for i in range(int(num*num/2))]
    a*=2
    random.shuffle(a)
    matrix=[[] for j in range(num)]
    for m in range(num):
        matrix[m]=a[:num]
        del a[:num]
    return matrix
# 重排列
def rerank(matrix):
    length=len(matrix)
    ls=[]
    matrix2=[[] for p in range(length)]
    for i in range(length):
        for q in range(length):
            ls.append(matrix[i][q])
    random.shuffle(ls)
    for m in range(length):
        matrix2[m]=ls[:length]
        del ls[:length]
    return matrix2
# 输出图形矩阵
def printf(matrix):
    length=len(matrix)
    for i in range(length):
        for j in range(length):
            print(matrix[i][j],end="   ")
        print('\n')
# 判断同处一行或一列的图标能否被消除
def removeOne(matrix,a,b,c,d,):
    boolen=1
    if a==c:
        row=a
        if b>d:
            max,min=b,d
        else:
            max,min=d,b
        if min+1!=max:
            for i in range(min+1,max):
                if matrix[row][i]!=" ":
                    boolen=0
    if b==d:
        col=b
        if a>c:
            max,min=a,c
        else:
            max,min=c,a
        if min+1!=max:
            for i in range(min+1,max):
                if matrix[i][col]!=" ":
                    boolen=0
    return boolen
# 判断输入坐标是否合乎规范并且以removeOne为基本单位实现一折和两折消除工作
def remove(matrix,a,b,c,d):
    length=len(matrix)
    boolen=1
    row1,col1,row2,col2=a-1,b-1,c-1,d-1
    if matrix[row1][col1]!=matrix[row2][col2] or matrix[row1][col1]==" ":
        print("错误的消除！")
        boolen=0
        return matrix,boolen
    if row1==0 and row2==0 or row1==length-1 and row2==length-1 or col1==0 and col2==0 or col1==length-1 and col2==length-1:
        matrix[row1][col1]=" "
        matrix[row2][col2]=" "  
        return matrix,boolen      
    if row1==row2 or col1==col2:
        if removeOne(matrix,row1,col1,row2,col2)==1:
            matrix[row1][col1]=" "
            matrix[row2][col2]=" "  
            return matrix,boolen      
    for i in range(length):
        if removeOne(matrix,i,col1,row1,col1)==1 and removeOne(matrix,i,col2,row2,col2)==1:
            if i==0 or removeOne(matrix,i,col1,i,col2)==1:                
                if (matrix[i][col1]==" " or i==row1) and (matrix[i][col2]==" " or i==row2):
                    matrix[row1][col1]=" "
                    matrix[row2][col2]=" "  
                    return matrix,boolen      
        if removeOne(matrix,row1,i,row1,col1)==1 and removeOne(matrix,col2,i,row2,col2)==1:
            if i==0 or removeOne(matrix,i,col1,i,col2)==1:
                if (matrix[row1][i]==" " or i==col1) and (matrix[row2][i]==" " or i==col2):
                    matrix[row1][col1]=" "
                    matrix[row2][col2]=" "  
                    return matrix,boolen 
    boolen=0
    print("错误的消除！")
    return matrix,boolen     
# 录入记录
def record(row,userName,timing):
    try:
        f=open("D:/连连看.txt","r")
        bool=0
        i=0
        lists1=f.readlines()
        lists2=[[],[],[],[]]
        f.close()
        for j in range(4):
            lists2[j]=lists1[j].split("&")
            lists2[j][4]=lists2[j][4].strip('\n')
        if row==4:
            while i<5 and bool==0:
                if eval(lists2[0][i])>timing:
                    lists2[0].insert(i,str(timing))
                    lists2[1].insert(i,userName)
                    del lists2[0][5]
                    del lists2[1][5]
                    bool=1
                if eval(lists2[0][i])==-1:
                    lists2[0][i]=str(timing)
                    lists2[1][i]=userName
                    bool=1
                i=i+1
        if row==6:
            while i<5 and bool==0:
                if eval(lists2[2][i])>timing:
                    lists2[2].insert(i,str(timing))
                    lists2[3].insert(i,userName)
                    del lists2[2][5]
                    del lists2[3][5]
                    bool=1
                if eval(lists2[2][i])==-1:
                    lists2[2][i]=str(timing)
                    lists2[3][i]=userName
                    bool=1
                i=i+1
        f=open("D:/连连看.txt","w")
        for i in range(4):
            lists="&".join(lists2[i])
            f.writelines(lists+'\n')
        f.close()
        if bool==1:
            return 1
        else:
            return 0
    except:
        f=open("D:/连连看.txt","w")
        lists1=[['-1' for i in range(5)],['*' for i in range(5)],\
            ['-1' for i in range(5)],['*' for i in range(5)]]
        lists2=[]
        if row==4:
            lists1[0][0]=str(timing)
            lists1[1][0]=userName
        if row==6:
            lists1[2][0]=str(timing)
            lists1[3][0]=userName
        for i in range(4):
            lists2="&".join(lists1[i])
            f.writelines(lists2+'\n')
        f.close()
        return 1
# robot消除
def rremove(matrix,a,b,c,d):
    length=len(matrix)
    boolen=1
    row1,col1,row2,col2=a-1,b-1,c-1,d-1
    if matrix[row1][col1]!=matrix[row2][col2] or matrix[row1][col1]==" ":
        boolen=0
        return matrix,boolen
    if (row1==0 and row2==0) or (row1==length-1 and row2==length-1) or (col1==0 and col2==0) or (col1==length-1 and col2==length-1):
        matrix[row1][col1]=" "
        matrix[row2][col2]=" "  
        return matrix,boolen      
    if row1==row2 or col1==col2:
        if removeOne(matrix,row1,col1,row2,col2)==1:
            matrix[row1][col1]=" "
            matrix[row2][col2]=" "  
            return matrix,boolen      
    for i in range(length):
        if removeOne(matrix,i,col1,row1,col1)==1 and removeOne(matrix,i,col2,row2,col2)==1:
            if i==0 or removeOne(matrix,i,col1,i,col2)==1:                
                if (matrix[i][col1]==" " or i==row1) and (matrix[i][col2]==" " or i==row2):
                    matrix[row1][col1]=" "
                    matrix[row2][col2]=" "  
                    return matrix,boolen      
        if removeOne(matrix,row1,i,row1,col1)==1 and removeOne(matrix,col2,i,row2,col2)==1:
            if i==0 or removeOne(matrix,i,col1,i,col2)==1:
                if (matrix[row1][i]==" " or i==col1) and (matrix[row2][i]==" " or i==col2):
                    matrix[row1][col1]=" "
                    matrix[row2][col2]=" "  
                    return matrix,boolen 
    boolen=0
    return matrix,boolen   
 

                    
def main():
    boolen=1
    while(boolen==1):
        t=os.system("cls")
        # 菜单选项
        print("1.无限模式")
        print("2.计时模式")
        print("3.记录查询")
        print("4.电脑玩家")
        print("5.退出")
        choise=eval(input("请输入你的选项："))
        if choise == 1:
            t=os.system("cls")
            row=eval(input("请输入你想要的规格(4/6)："))
            while row!=4 and row!=6:
                row=eval(input("请输入你想要的规格(4/6)："))
            matrix=lists(row)
            printf(matrix)
            print("输入restart重排列")
            print("输入return返回菜单")
            i=0
            while i < int(row*row/2):
                i+=1
                str=input("请输入想消除的图形坐标(如(1,1)(1,2))：")
                if str=="restart":
                    matrix=rerank(matrix)
                    printf(matrix)
                    i-=1
                    continue
                if str=="return":
                    break
                if str[0]!='(' or  str[2]!=',' or str[4]!=')' or str[5]!='(' or str[7]!=',' or str[9]!=')':
                    print("格式错误！")
                    i-=1
                    continue
                a,b,c,d=eval(str[1]),eval(str[3]),eval(str[6]),eval(str[8])
                if a<1 and a>row or b<1 and b>row or c<1 and c>row or d<1 and d>row:
                    print("下标越界！")
                    i-=1
                    continue
                if a==c and b==d:
                    print("输入错误！")
                    i-=1
                    continue
                matrix,bool=remove(matrix,a,b,c,d)
                if bool==0:
                    i-=1
                printf(matrix)
            if i >= int(row*row/2):
                print("你成功了！")
                str=input("回车返回主菜单")    
        if choise == 2:
            t=os.system("cls")
            row=eval(input("请输入你想要的规格(4/6)："))
            while row!=4 and row!=6:
                row=eval(input("请输入你想要的规格(4/6)："))
            matrix=lists(row)
            printf(matrix)
            print("输入restart重排列")
            print("输入return返回菜单")
            print("计时开始！")
            start=time.perf_counter()
            i=0
            while i < int(row*row/2):
                i+=1
                str=input("请输入想消除的图形坐标(如(1,1)(1,2))：")
                if str=="restart":
                    matrix=rerank(matrix)
                    printf(matrix)
                    i-=1
                    continue
                if str=="return":
                    break
                if str[0]!='(' or  str[2]!=',' or str[4]!=')' or str[5]!='(' or str[7]!=',' or str[9]!=')':
                    print("格式错误！")
                    i-=1
                    continue
                a,b,c,d=eval(str[1]),eval(str[3]),eval(str[6]),eval(str[8])
                if a<1 and a>row or b<1 and b>row or c<1 and c>row or d<1 and d>row:
                    print("下标越界！")
                    i-=1
                    continue
                if a==c and b==d:
                    print("输入错误！")
                    i-=1
                    continue
                matrix,bool=remove(matrix,a,b,c,d)
                if bool==0:
                    i-=1
                printf(matrix)
            end=time.perf_counter()
            print("你成功了！")
            timing=round(end-start,1)
            print("用时：{0}s".format(timing))
            userName=input("请留名：")
            if record(row,userName,timing)==1:
                print("成绩进入前五了！")
            else:
                print("未破纪录！")
            str=input("回车返回主菜单")
        if choise == 3:
            t=os.system("cls")
            fl=open("D:/连连看.txt","r")
            lists1=fl.readlines()
            lists2=[[],[],[],[]]
            fl.close()
            for j in range(4):
                lists2[j]=lists1[j].split("&")
                lists2[j][4]=lists2[j][4].strip('\n')
            print("4*4:")
            for j1 in range(5):
                print("第%d"%(j1+1)+"名："+lists2[1][j1]+" "+"用时："+lists2[0][j1]+"s")
            print("6*6:")
            for j2 in range(5):
                print("第%d"%(j2+1)+"名："+lists2[3][j2]+" "+"用时："+lists2[2][j2]+"s")
            str=input("回车返回主菜单")
        if choise==4:
            t=os.system("cls")
            print("请输入你想要的规格(4/6):",end="")
            num=random.choice([4,6])
            time.sleep(3)
            print(num)
            matrix=lists(num)
            printf(matrix)
            print("输入restart重排列")
            print("输入return返回菜单")  
            all=num*num/2
            while all>0:
                for i in range(num):
                    for j in range(num):
                        for m in range(num):
                            for n in range(num):
                                if matrix[i][j]==matrix[m][n] and (i!=m or j!=n) and matrix[i][j]!=" ":
                                    matrix,bool=rremove(matrix,i+1,j+1,m+1,n+1)
                                    if bool==0:
                                        continue
                                    else:
                                        all=all-1
                                        time.sleep(3)
                                        print("请输入坐标：({0},{1})({2},{3})".format(i+1,j+1,m+1,n+1))
                                        time.sleep(3)
                                        printf(matrix)
                if all>0:
                    print("请输入坐标：rerank")
                    matrix=rerank(matrix)
                    printf(matrix)
            str=input("回车返回主菜单")
        if choise==5:
            boolen=0



main()  
