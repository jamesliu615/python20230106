while True:
    try:
        輸入=int(input())
        if 輸入 >31:
         print("輸入不能超過31")
        else:
            r=2**輸入
            print(r)
    except(EOFError):
        break     



