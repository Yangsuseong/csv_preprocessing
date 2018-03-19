import csv, codecs


csv_file_dir = input("csv파일의 경로를 정확히 입력하세요. : ")
csv_filename_user_input = input("불러올 csv파일의 이름을 입력하세요. : ")
N_csv_file_dir = input("변환한 csv파일을 저장할 경로를 정확히 입력하세요. :")
N_csv_filename = input("변환한 csv파일을 저장할 이름을 입력하세요. : ")

#####################################
#csv_file = '/Users/tntjd5596/Downloads/ML_Patient monitor data/RCM_ETCO2_1.CSV'
csv_file = csv_file_dir + "/" + csv_filename_user_input
# 기존의 csv파일 경로와 이름을 입력한다.

#save_csv_filename = '/Users/tntjd5596/Downloads/ML_Patient monitor data/N_RCM_ETCO2_1.CSV'
save_csv_filename = N_csv_file_dir + "/" + N_csv_filename
# N을 채운 새로운 csv파일을 저장할 경로와 파일 이름을 입력한다.
#####################################



fp = codecs.open(csv_file, "r", "utf-8")
# codecs.open() 함수를 사용하여 csv파일을 불러와 fp에 저장한다.

reader = csv.reader(fp)
# fp를 읽어온다.

i = 0
j = 0
k = 0
label = []
# label이라는 이름의 빈 리스트를 생성한다.

for cells in reader:
    if len(cells) == 0:
        label.append('Z')
        print(i)
        #바뀐 인덱스
        i += 1
        j += 1
    # 만약 reader(cells)의 길이가 0이면 빈칸이기 때문에 Z을 리스트에 추가한다.
    
    elif cells == [' ']:
        label.append('Z')
        print(i)
        #바뀐 인덱스
        i += 1
        j += 1
    # 만약 cells가 빈칸이라면 Z로 변환한다.
    
    
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
print(label)
print("------------------------------------------------------------------")

f = open(save_csv_filename,'w', encoding="utf-8", newline="")
# newline을 ""로 설정하여 빈칸이 생기는 현상을 막는다.(windows에서만 문제가 생김)
# 쓰기모드의 새로운 csv파일을 열고

for i in range(len(label)):
    csvWriter = csv.writer(f)
    csvWriter.writerow([label[i]])
# 새로운 csv파일에 label을 입력한다.



else:
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
    
    fp.close()
    f.close()

f.close()
