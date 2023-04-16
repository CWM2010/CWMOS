import datetime
import random
import time
import pygame

youxibi = 100
fileC = []
fileD = []
a = random.randint(1, 30)
print("系统正在启动")
print(a, "%")
time.sleep(1)
a = random.randint(30, 70)
print(a, "%")
time.sleep(1)
a = random.randint(70, 80)
print(a, "%")
time.sleep(1)
print("100%")
time.sleep(3)
print("Python CWM系统安装正在运行")
time.sleep(2)
running = False
user_input_key = input("输入密钥---(比如 rrrr5_69qqb_52qa5_212oo_77hfr)")
if user_input_key == "cc28m_l12er_4502w_7762u_yy9sb":
    running = True
else:
    print("激活吗错误，安装失败")
    running = False
if running:
    print("安装成功，正在重新启动")
    time.sleep(5)
    user_input_yn = input("许可条款：这个系统严禁转发不标明出处，获得源代码请找C站up主程文墨，源代码已开放。请输入Y/N")
    if user_input_yn == "Y":
        running = True
    else:
        print("必须同意许可才能安装，安装失败")
        running = False
    time.sleep(1)
    print("正在准备用户登录系统......")
    time.sleep(3)
    username = input("""请设置用户名
    记住，用户名不宜过长""")
    password = input("请设置密码")
    password_2 = input("确认你的密码")
    if password_2 == password:
        print("OK,正在保存......")
    else:
        print("密码确认错误，安装失败")
        running = False
    print("成功")
    time.sleep(1)
    run = True
    while run:
        print(username)
        denglu = input("请输入你的密码")
        if denglu == password:
            print("登陆成功")
            run = False
        else:
            print("密码错误，请重试")
    # print("抱歉，此系统还未完工，请后续期待")
    osrun = True
    while osrun:
        choose = input("""请选择：
                1 时间
                2 病毒程序
                3 系统信息
                4 退出系统
                5 游戏库
                6 字符打印机
                7 系统测试包
                8 计算器
                9 python for CWM
                10 文件资源管理器
                11 python浏览器
                12 微软挑战""")
        if choose == "1":
            shijianxitong = True
            while shijianxitong:
                print(datetime.datetime.now())
                tuichushijian = input("""请按5键退出""")
                if tuichushijian == "5":
                    shijianxitong = False
        if choose == "2":
            for j in range(random.randint(100, 120)):
                print("那么，成全你！！！谢谢你砸坏了你的电脑")
                time.sleep(0.1)
                osrun = False
        if choose == "3":
            settingchoose = input("""已进入页面
            1 系统信息
            2 软件更新""")
            if settingchoose == "1":
                print("""系统版本：Python系统2.2
                发布者：CWM 保留所有权利
                用户名：""", username, """
                系统激活状态：已激活""")
            if settingchoose == "2":
                print("正在检查更新...")
                time.sleep(2)
                gxlschoose = input("已是最新版本，是否查看更新历史 Y/N")
                if gxlschoose == "Y":
                    print("""Python系统1.0(pu100)
                    更新内容：Python系统正式版，可以进入系统
                    Python系统1.1(pu110)
                    更新内容：新增系统信息板块，可检查更新
                    Python系统1.2(pu120)
                    更新内容：新增游戏板块和一些bug修复
                    Python系统2.0(pu200)
                    更新内容：新增若干板块，史级大更新
                    Python系统2.1(pu210)
                    更新内容：新增文件资源管理器
                    Python系统2.2(pu220)
                    更新内容：行政python浏览器""")
        if choose == "4":
            print("感谢使用，再见")
            osrun = False
        if choose == "5":
            print("现有的游戏币数")
            print(youxibi)
            youxichoose = input("""选择游戏：
            1 猜数
            2 游戏币商店
            3 坦克大战（转载来自 Python小二）""")
            if youxichoose == "1":
                caishunandu = input("""选择难度：
                1 简单
                2 中等
                3 困难""")
                if caishunandu == "1":
                    caishurun1 = True
                    shu = random.randint(1, 20)
                    while caishurun1:
                        print("范围1~20")
                        yonghushurushu = int(input("请输入："))
                        if yonghushurushu > shu:
                            print("大了")
                        elif yonghushurushu < shu:
                            print("小了")
                        else:
                            print("答对了，游戏币+5")
                            youxibi += 5
                            caishurun1 = False
                if caishunandu == "2":
                    caishurun2 = True
                    shu = random.randint(1, 100)
                    while caishurun2:
                        print("范围1~100")
                        yonghushurushu = int(input("请输入："))
                        if yonghushurushu > shu:
                            print("大了")
                        elif yonghushurushu < shu:
                            print("小了")
                        else:
                            print("答对了，游戏币+10")
                            youxibi+=10
                            caishurun2 = False
                if caishunandu == "3":
                    caishurun = True
                    shu = random.randint(1, 1000)
                    while caishurun:
                        print("范围1~1000")
                        yonghushurushu = int(input("请输入："))
                        if yonghushurushu > shu:
                            print("大了")
                        elif yonghushurushu < shu:
                            print("小了")
                        else:
                            print("答对了，游戏币+20")
                            youxibi+=20
                            caishurun = False
            if youxichoose == "2":
                print("你的游戏币数量为", youxibi)
                if youxibi <= 15:
                    print("你的游戏等级为1")
                elif 15 < youxibi <= 30:
                    print("你的游戏等级为2")
                elif 30 < youxibi <= 50:
                    print("你的游戏等级为3")
                elif 50 < youxibi <= 70:
                    print("你的游戏等级为4")
                elif 70 < youxibi <= 100:
                    print("你的游戏等级为5")
                else:
                    print("你的游戏等级为6，很棒")
            if youxichoose == "3":
                if youxibi <= 15:
                    print("注意，要15游戏币使用费，你的游戏币不足")
                else:
                    youxibi -= 15
                    class Brick(pygame.sprite.Sprite):
                        def __init__(self):
                            pygame.sprite.Sprite.__init__(self)
                            self.brick = pygame.image.load('images/scene/brick.png')
                            self.rect = self.brick.get_rect()
                            self.being = False


                    # 钢墙
                    class Iron(pygame.sprite.Sprite):
                        def __init__(self):
                            pygame.sprite.Sprite.__init__(self)
                            self.iron = pygame.image.load('images/scene/iron.png')
                            self.rect = self.iron.get_rect()
                            self.being = False


                    # 冰
                    class Ice(pygame.sprite.Sprite):
                        def __init__(self):
                            pygame.sprite.Sprite.__init__(self)
                            self.ice = pygame.image.load('images/scene/ice.png')
                            self.rect = self.ice.get_rect()
                            self.being = False


                    # 河流
                    class River(pygame.sprite.Sprite):
                        def __init__(self, kind=None):
                            pygame.sprite.Sprite.__init__(self)
                            if kind is None:
                                self.kind = random.randint(0, 1)
                            self.rivers = ['images/scene/river1.png', 'images/scene/river2.png']
                            self.river = pygame.image.load(self.rivers[self.kind])
                            self.rect = self.river.get_rect()
                            self.being = False


                    # 树
                    class Tree(pygame.sprite.Sprite):
                        def __init__(self):
                            pygame.sprite.Sprite.__init__(self)
                            self.tree = pygame.image.load('images/scene/tree.png')
                            self.rect = self.tree.get_rect()
                            self.being = False


                    # 地图
                    class Map():
                        def __init__(self, stage):
                            self.brickGroup = pygame.sprite.Group()
                            self.ironGroup = pygame.sprite.Group()
                            self.iceGroup = pygame.sprite.Group()
                            self.riverGroup = pygame.sprite.Group()
                            self.treeGroup = pygame.sprite.Group()
                            if stage == 1:
                                self.stage1()
                            elif stage == 2:
                                self.stage2()

                        # 关卡一
                        def stage1(self):
                            for x in [2, 3, 6, 7, 18, 19, 22, 23]:
                                for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
                                    self.brick = Brick()
                                    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                                    self.brick.being = True
                                    self.brickGroup.add(self.brick)
                            for x in [10, 11, 14, 15]:
                                for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
                                    self.brick = Brick()
                                    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                                    self.brick.being = True
                                    self.brickGroup.add(self.brick)
                            for x in [4, 5, 6, 7, 18, 19, 20, 21]:
                                for y in [13, 14]:
                                    self.brick = Brick()
                                    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                                    self.brick.being = True
                                    self.brickGroup.add(self.brick)
                            for x in [12, 13]:
                                for y in [16, 17]:
                                    self.brick = Brick()
                                    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                                    self.brick.being = True
                                    self.brickGroup.add(self.brick)
                            for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25),
                                         (14, 25)]:
                                self.brick = Brick()
                                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                                self.brick.being = True
                                self.brickGroup.add(self.brick)
                            for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
                                self.iron = Iron()
                                self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
                                self.iron.being = True
                                self.ironGroup.add(self.iron)

                        # 关卡二
                        def stage2(self):
                            for x in [2, 3, 6, 7, 18, 19, 22, 23]:
                                for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
                                    self.brick = Brick()
                                    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                                    self.brick.being = True
                                    self.brickGroup.add(self.brick)
                            for x in [10, 11, 14, 15]:
                                for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
                                    self.brick = Brick()
                                    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                                    self.brick.being = True
                                    self.brickGroup.add(self.brick)
                            for x in [4, 5, 6, 7, 18, 19, 20, 21]:
                                for y in [13, 14]:
                                    self.brick = Brick()
                                    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                                    self.brick.being = True
                                    self.brickGroup.add(self.brick)
                            for x in [12, 13]:
                                for y in [16, 17]:
                                    self.brick = Brick()
                                    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                                    self.brick.being = True
                                    self.brickGroup.add(self.brick)
                            for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25),
                                         (14, 25)]:
                                self.brick = Brick()
                                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                                self.brick.being = True
                                self.brickGroup.add(self.brick)
                            for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
                                self.iron = Iron()
                                self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
                                self.iron.being = True
                                self.ironGroup.add(self.iron)

                        def protect_home(self):
                            for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25),
                                         (14, 25)]:
                                self.iron = Iron()
                                self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
                                self.iron.being = True
                                self.ironGroup.add(self.iron)
        if choose == "6":
            print("欢迎来到字符打印机")
            printzifu = input("你要输什么字符")
            time.sleep(2)
            print("你打印了", len(printzifu), "个字符")
            print("打印结果是 ", printzifu)
        if choose == "7":
            ceshibaochoose = input("""1 颜色字体""")
            if ceshibaochoose == "1":
                print("\033[34m%s\033[0m" % "输出蓝色字符")
                print("\033[31m%s\033[0m" % "输出红色字符")
                print("\033[32m%s\033[0m" % "输出绿色字符")
                print("\033[33m%s\033[0m" % "输出黄色字符")
                print("\033[36m%s\033[0m" % "输出青色字符")
        if choose == "8":
            print("请输入第一个数")
            fnum = int(input())
            print("请输入第二个数")
            snum = int(input())
            print("请输入符号（+,-,*,/,**）")
            fuhao = input()
            if fuhao == "+":
                print(fnum + snum)
            if fuhao == "-":
                print(fnum - snum)
            if fuhao == "*":
                print(fnum * snum)
            if fuhao == "/":
                print(fnum - snum)
            if fuhao == "**":
                print(fnum ** snum)
            else:
                print("符号错误")
        if choose == "9":
            print("""Python 1.0.0 for CWM OS
            请输入help()帮助，输入exit()退出
            注意！！！请切换至英文输入法！""")
            runpython = True
            while runpython:
                yonghushurupythonyufa = input(">>>")
                if yonghushurupythonyufa == "help()":
                    print("""这个是pythonCWM系统的命令行版本
                    兼开发程序。
                    当前大部分功能在开发中，请耐心等待。
                    Python 1.0.0 for CWM OS
                    已是最新版本""")
                elif yonghushurupythonyufa == "exit()":
                    print("感谢使用，再见")
                    runpython = False
                else:
                    print("正在开发中，请耐心等待")
        if choose == "10":
            print("这是你的文件")
            print("你有C盘和D盘")
            print("C盘里有", fileC)
            print("D盘里有", fileD)
            tianjiawenjianhuoshanchu = input("你要添加或删除文件吗（Y/N）")
            if tianjiawenjianhuoshanchu == "Y":
                tianjiahuoshanchuwenjian = input("添加/删除")
                if tianjiahuoshanchuwenjian == "添加":
                    tianjiapan = input("那个盘里(C/D)")
                    if tianjiapan == "C":
                        wenjian = input("要添加什么")
                        fileC.append(wenjian)
                        print("添加后的是", fileC)
                    if tianjiapan == "D":
                        wenjian = input("要添加什么")
                        fileD.append(wenjian)
                        print("添加后的是", fileD)
                if tianjiahuoshanchuwenjian == "删除":
                    shanchupan = input("哪个盘里(C/D)")
                    if shanchupan == "C":
                        print(fileC)
                        shanchuwenjianmingc = input("哪个文件")
                        if shanchuwenjianmingc in fileC:
                            fileC.remove(shanchuwenjianmingc)
                            print("删除后的C盘：", fileC)
                    if shanchupan == "D":
                        print(fileD)
                        shanchuwenjianmingd = input("哪个文件")
                        if shanchuwenjianmingd in fileD:
                            fileC.remove(shanchuwenjianmingd)
                            print("删除后的D盘：", fileD)
        if choose == "11":
            print("欢迎来到python浏览器")
            webchoosetips = input("""选择：
            1 百度百科
            2 浏览器版本""")
            if webchoosetips == "1":
                print("该功能正在开发中，请耐心等待")
            if webchoosetips == "2":
                print("python web 1.0.00")
        if choose == "12":
            print("欢迎来到微软挑战")
            ask1 = input("什么是Windows")
