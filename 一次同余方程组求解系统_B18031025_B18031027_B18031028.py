import tkinter as tk
from main import *
import tkinter.font as tkFont
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk


def Run():
    def compute():
        file = open("src_data/data.txt", "w")
        data = t.get(0.0, tk.END)
        file.write(data)
        file.close()


        # solution 是最后的结果，数据类型为字符串，形如 "解为: x=1(mod 2)"
        solution = main()
        result_var.set(solution)

    def selectPath():
        file = open("src_data/data.txt", "w")
        file.close()

        # 选择文件path_接收文件地址
        path_ = tk.filedialog.askopenfilename()
        # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取
        # 注意：\\转义后为\，所以\\\\转义后为\\
        path_ = path_.replace("/", "\\\\")

        # 读取文件
        out_file = open(path_)
        # 逐行写入
        for line in out_file.readlines():
            with open("src_data/data.txt", "a") as file:
                file.write(line)
        out_file.close()

        solution = main()
        result_var.set(solution)



    # 实例化object，建立窗口window
    window = tk.Tk()

    # 给窗口的可视化起名字
    window.title('My Window')

    # 设定窗口的大小(长 * 宽)
    window.geometry('400x520')

    # 在图形界面上设定标签
    font_title = tkFont.Font(family='微软雅黑', size=15)
    font_result = tkFont.Font(family='微软雅黑', size=12)

    result_var = tk.StringVar()


    # 设置背景图片
    img_open = Image.open("gray.jpg")

    img = ImageTk.PhotoImage(img_open)

    background = tk.Label(window, width=800, height=600)
    background.config(image=img)
    background.image = img  # keep a reference


    # 设置标签
    title = tk.Label(window, text='求解一次同余方程组\n示例:x=1(mod2)', bg='white', font=font_title, width=25, height=2)
    result = tk.Label(window, textvariable=result_var, bg='white', font=font_result, width=30, height=2)




    # 创建一个多行文本框text用以显示，指定height为文本框高度
    font_text = tkFont.Font(family='微软雅黑', size=16)
    t = tk.Text(window, height=15, width=39, font=font_text)


    # 设置text控件的滚动条
    scroll = tk.Scrollbar()
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    scroll.config(command=t.yview)  # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
    t.config(yscrollcommand=scroll.set)  # 将滚动条关联到文本框



    # 在窗口界面设置Button按键
    compute_button = tk.Button(window, text="计算", font=font_result,
                               width=5, height=1, bd=5, command=compute)
    browse_button = tk.Button(window, text="路径选择", font=font_result,
                               width=5, height=1, bd=5,command=selectPath)




    # 控件放置顺序 （绝对位置）
    background.pack()
    title.place(x=45,y=15)
    t.place(x=66,y=90,width=260,height=250)
    result.place(x=66,y=360,width=260,height=50)
    compute_button.place(x=66,y=430,width=120,height=50)
    browse_button.place(x=210,y=430,width=120,height=50)




    # 主窗口循环显示 阻止Python GUI的大小调整
    window.resizable(0, 0)
    window.mainloop()





Run()
