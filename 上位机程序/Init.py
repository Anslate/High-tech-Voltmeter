import os
def main():
    print("High-tech Voltmeter项目上位机软件快速配置脚本\n由Anslate制作")
    print("在正式开始之前，请您阅读教程。自行承担风险。")
    if (0 != os.system("echo \"*PLEASE DELETE THIS FILE* This is a temporary file. You can see this file stating that auto-delete didn't work. Please delete it manually.\" > \"C:\\please delete this file.txt\"")):
        print("请以管理员身份重新运行此程序")
        input("按下任意按键退出")
        return
    os.system("del /F \"C:\\please delete this file.txt\"")
    while(1):
        addr = input("请输入软件安装目录:\n>")
        print(".\\CpuGetter.exe文件将会复制到\"%sCpuGetter.exe\"，是否确认[y/n]" % addr)
        a = input(">")
        if(a == "y"):
            if(" " in addr):
                space = True
            else:
                space = False
            if (0 != os.system("echo *PLEASE DELETE THIS FILE* This is a temporary file. You can see this file stating that auto-delete didn't work. Please delete it manually. > \"%s\"" % (addr + "please delete this file.txt"))):
                print("此目录不可用")
                continue
            break
    os.system("del /F \"%s\"" % (addr + "please delete this file.txt"))
    addr = addr + "CpuGetter.exe"
    if(space):
        os.system("copy .\CpuGetter.exe \"%s\"" % addr)
    else:
        os.system("copy .\CpuGetter.exe "+addr)
    COM = input("请输入端口:\n>")
    bps = input("请输入比特率:\n>")
    if(space):
        #sc create CpuGetter type= own start= auto binpath= "%s"
        os.system("sc create CpuGetter type= own start= auto binpath= \"%s\"" % addr)
        #reg add HKLM\SYSTEM\CurrentControlSet\Services\CpuGetter /f /v ImagePath /t REG_EXPAND_SZ /d "%s" %s %s
        os.system("reg add HKLM\SYSTEM\CurrentControlSet\Services\CpuGetter /f /v ImagePath /t REG_EXPAND_SZ /d \"\\\"%s\\\" %s %s\"" % (addr,COM,bps))
    else:
        #sc create CpuGetter type= own start= auto binpath= %s
        os.system("sc create CpuGetter type= own start= auto binpath= %s" % addr)
        #reg add HKLM\SYSTEM\CurrentControlSet\Services\CpuGetter /f /v ImagePath /t REG_EXPAND_SZ /d "%s %s %s"
        os.system("reg add HKLM\SYSTEM\CurrentControlSet\Services\CpuGetter /f /v ImagePath /t REG_EXPAND_SZ /d \"%s %s %s\"" % (addr,COM,bps))
if(__name__ == "__main__"):
    main()