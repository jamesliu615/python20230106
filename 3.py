while True:
    try:
        輸入=int(input())
        NT50=輸入 // 50
        輸入=輸入 % 50
        NT10=輸入 // 10
        輸入=輸入 % 10
        NT5=輸入 // 5
        輸入=輸入 % 5
        print("NT50="+str (NT50))
        print("NT10="+str (NT10))
        print("NT5="+str (NT5))
        print("NT1="+str (輸入))
    except(EOFError):
        break 


