
# coding: utf-8

# 다시..

# In[1]:


import csv, codecs, os


# In[2]:


csv_list = []


# In[3]:


csv_file_dir = input("csv파일의 경로를 정확히 입력하세요. : ")
#csv_file_dir = '/Users/tntjd5596/Desktop/ML_Patient monitor data'


# csv 파일의 경로를 받아서 리스트로 만들어 csv파일만 골라낸 후 전부 돌린다.
csv_dir = os.listdir(csv_file_dir)
for i in csv_dir:
    # 끝이 CS로 끝나는 파일만 찾아서
    if(i[-3:-1] == "CS"):
        k = i[0:1]
        for j in k:
            # 그중에 첫글자가 R인 파일들만 리스트에 추가
            if(j == 'R'):
                csv_list.append(i)
csv_list.sort()

# image 파일이 들어있는 디렉토리의 리스트를 만든다.
image_dirs = csv_file_dir + "/RCM/"
image_dir_list = os.listdir(image_dirs)[2:]


# In[4]:


for f in csv_list:
    csv_file = csv_file_dir + "/" + f   # csv 파일
    save_csv_filename ="/" + "Z_" + f    # 변환한 파일 이름 앞에 Z_ 붙이기
    save_csv_file_dir = csv_file_dir + "/" + "Z_" + f
    #original_image_dir = 
    move_image_dir = image_dirs + "/Z_" + f   # 
    
    print(f + "  ->  " + save_csv_filename)
    
    fp = codecs.open(csv_file, "r", "utf-8")
    # codecs.open() 함수를 사용하여 csv파일을 불러와 fp에 저장한다.

    reader = csv.reader(fp)
    # fp를 읽어온다.
################################################################## 추가된부분. 리스트로 돌려서 .CSV파일 한번에 작업하기.

    i = 0
    j = 0
    k = 0
    label = []
    # label이라는 이름의 빈 리스트를 생성한다.
    print('change_index : ')

    for cells in reader:
        if len(cells) == 0:
            label.append('Z')
            print(i)
            #바뀐 인덱스
            i += 1
            j += 1
        # 만약 reader(cells)의 길이가 0이면 빈칸이기 때문에 Z을 리스트에 추가한다.
        
        elif cells==[' ']:
            label.append('Z')
            print(i)
            #바뀐 인덱스
            i += 1
            j += 1
        # Space인 경우에도 Z로 변환.
    
        # 'N'들을 모두 'Z'로 바꾼다.
        elif cells==['N']:
            label.append('Z')
            print(i)
            #바뀐 인덱스
            i += 1
            k += 1
            # 빈칸을 변경한 것이 아니기 때문에 따로 센다.

        else:
            label.append(cells[0])
            i += 1
        # reader(cells)의 길이가 0이 아니면 자기 자신을 리스트에 추가한다.
    else:
        print("changes blank -> N :", j)
        print("changes N -> Z :", k)
        print("total changes = ", j+k)
        
        # 바뀐 인덱스의 갯수

    print("csv_len : ",len(label))
    #print(label)
    
    n_0 = 0
    n_1 = 0
    n_2 = 0
    n_3 = 0
    n_4 = 0
    n_5 = 0
    n_6 = 0
    n_7 = 0
    n_8 = 0
    n_9 = 0
    n_Z = 0
    
    for i in label:
        if i=='0':
            n_0 += 1 
        elif i=='1':
            n_1 += 1
        elif i=='2':
            n_2 += 1
        elif i=='3':
            n_3 += 1
        elif i=='4':
            n_4 += 1 
        elif i=='5':
            n_5 += 1 
        elif i=='6':
            n_6 += 1 
        elif i=='7':
            n_7 += 1 
        elif i=='8':
            n_8 += 1
        elif i=='9':
            n_9 += 1
        else:
            n_Z += 1
            
    else:
        print("0_num : ", n_0)
        print("1_num : ", n_1)
        print("2_num : ", n_2)
        print("3_num : ", n_3)
        print("4_num : ", n_4)
        print("5_num : ", n_5)
        print("6_num : ", n_6)
        print("7_num : ", n_7)
        print("8_num : ", n_8)
        print("9_num : ", n_9)
        print("Z_num : ", n_Z)
    
    print("----------------------------------------------------------")
    f = open(save_csv_file_dir,'w', encoding="utf-8", newline="") 
    # newline을 ""로 설정하여 빈칸이 생기는 현상을 막는다.(windows에서만 문제가 생김)
    # 쓰기모드의 새로운 csv파일을 열고

    for i in range(len(label)):
        csvWriter = csv.writer(f)
        csvWriter.writerow([label[i]])
        # 새로운 csv파일에 label을 입력한다.

    fp.close()
    f.close()
