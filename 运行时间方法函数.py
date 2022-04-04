import  time
def timemaster(func):
    def call_function():
        start = time.time()
        func()
        end = time.time()
        print(f"{(end - start):.2f} 秒。")
    return call_function
@timemaster  #装饰器
def lala():
    time.sleep(2)
    print("你好啊")
lala()



