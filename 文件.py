with open('1.txt','r' ) as f:
    print( f.read() )
	
with open('1.txt','r' ) as f:
    for line in f.readlines():     # 每次读取一行内容，并按行返回list
        print(line.strip())        # 把末尾的'\n'删掉
