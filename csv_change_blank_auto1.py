import csv, codecs
import os


csv_file_dir = input("csv파일의 경로를 정확히 입력하세요. : ")


# csv 파일의 경로를 받아서 리스트로 만들어 csv파일만 골라낸 후 전부 돌린다.
csv_directory =csv_file_dir
csv_dir = os.listdir(csv_directory)

############################################
csv_list = []
for i in csv_dir:
    # 끝이 CS로 끝나는 파일만 찾아서
    if(i[-3:-1] == "CS"):
        k = i[0:1]
        for j in k:
            # 그중에 첫글자가 R인 파일들만 리스트에 추가
            if(j == 'R'):
                csv_list.append(i)
                
for f in csv_list:
    csv_file = csv_file_dir + "/" + f
    save_csv_file = "Z_" + f
    # 변환한 파일 이름 앞에 Z_ 붙이기
    save_csv_filename =csv_file_dir + "/" + "Z_" + f
    
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
    print(label)
    
    f = open(save_csv_filename,'w', encoding="utf-8", newline="") 
    # newline을 ""로 설정하여 빈칸이 생기는 현상을 막는다.(windows에서만 문제가 생김)
    # 쓰기모드의 새로운 csv파일을 열고

    for i in range(len(label)):
        csvWriter = csv.writer(f)
        csvWriter.writerow([label[i]])
        # 새로운 csv파일에 label을 입력한다.
    
    
    fp.close()
    f.close()
