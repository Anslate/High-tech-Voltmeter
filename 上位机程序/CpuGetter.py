#8位数据，无校验，1停止位
import psutil
import serial,serial.tools.list_ports
import sys
def main():#主函数
    port = serial.tools.list_ports.comports()
    if(len(sys.argv)!=3):#传参有3个，0是脚本名，1是端口号，2是比特率
        print("检测到传入参数有误，请核验")
        if(len(port)==0):
            print("无可用端口")
        else:
            print("可使用端口列表：")
            for i in port:
                print(i.device)
        #print("8位数据，无校验，1停止位")
        input("按下任意按键退出")
        return
    else:
        try:
            s = serial.Serial(sys.argv[1],int(sys.argv[2]))#打开串口
        except:
            print("串口启动失败，请检查  ：\n传入端口<%s>，传入比特率<%s>" % (sys.argv[1],sys.argv[2]))#打开失败，发出通知
            if(len(port)==0):
                print("无可用端口")
            else:
                print("可使用端口列表：")
            for i in port:
                print(i.device)
            input("按下任意按键退出")
            return
    while(1):
        try:#用USB拓展坞时会中断，放个try在这防止程序停止
            cpu = psutil.cpu_percent(0.5)
            #print(int(655.35*cpu).to_bytes(2,"big").hex(),cpu)
            s.write(int(655.35*cpu).to_bytes(2,"big"))
        except:
            pass
        
if(__name__ == "__main__"):
    main()#运行主函数