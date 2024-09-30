# 小红书电商计算利润或售价的计算器
![微信截图_20240930140241](https://github.com/user-attachments/assets/8b8e2cbf-44dc-4d1d-ad8c-35898bae1589)
![微信截图_20240930140224](https://github.com/user-attachments/assets/0e522529-ced6-4139-bbfe-f6b68ddbabfe)

# 打包步骤

1. 安装 PyInstaller
首先，确保你已经安装了 PyInstaller。你可以通过 pip 来安装它。
> pip install pyinstaller

2. 运行 PyInstaller 打包 Python 脚本
在命令行中，进入你的 Python 脚本所在的目录，然后运行以下命令：<br/>
> pyinstaller --onefile --windowed script_name.py

--onefile：将所有文件打包为一个独立的 .exe 文件。
--windowed：在 Windows 上打包时，不显示控制台窗口（适用于 GUI 应用）。
script_name.py：替换为你要打包的 Python 脚本名称。

3. 打包完成后
打包完成后，生成的 .exe 文件会在 dist 目录下。你可以进入该目录找到生成的 .exe 文件。

# 详细示例
假设你的 Python 脚本文件名是 app.py，打包的命令如下：
> pyinstaller --onefile --windowed app.py

运行此命令后，PyInstaller 会生成两个文件夹：
build：包含临时构建文件，可以忽略。
dist：这是最终生成的 .exe 文件所在的文件夹。
你可以在 dist 文件夹中找到 app.exe，这就是打包后的可执行文件。

# CMD运行
本地创建 main.py 复制代码进去
文件夹地址栏输入CMD 
> python （把文件拉进去）
