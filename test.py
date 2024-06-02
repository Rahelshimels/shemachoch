import LCD1602
import time
LCD1602.init(0x27, 1)
try:
    while True:
        LCD1602.write(0,0, 'hello world')
        LCD1602.write(0,1, 'well come')
         
except KeyboardInterrupt:
    LCD1602.clear()
    print("lcd good to go")
    
    
