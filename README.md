# compliance-zhangfei

## English introduction

Special Thanks : Aboutcode project -- what makes our tools **SPDX-Native**

### What is compliance-zhangfei
A tool writtern by Python for open source copyright compliance and in future it can support other compliance scan.

### Why compliance-zhangfei?
“Open source compliance is the process by which users, integrators and developers of open source software observe copyright notices and satisfy license obligations for their open source software components” — The Linux Foundation

### What compliance-zhangfei now looks like?
Now compliance-zhangfei is in its prototype, it's only a cli-tool for scan software license and maybe other metadata. 

emmm ... Vue-UI and Django_rest_api is on the way.

Our purpose is to build a expert system to help people who uses opensource software to well obey their license and copyright obligations.

### How to build?
Build environment: Ubuntu Linux 20.04 (recommended) / M$ Windows 10 

Build tool: VC buildTool (if M$ Windows) | Python 3.6+ | pip 20.3.3+

* **PAY ATTENTION** : If you are in M$ windows, you should install VC buildTool and Windows SDK firstly. You can get it from (https://visualstudio.microsoft.com/zh-hans/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)

1 - Now you can simply git clone the code 

2 - just run "./configure" | in Windows 10 , just run ".\configure"

* **PAY ATTENTION** : If using venv, you should config pyvenv for your linux/windows

Have a cup of coffee and wait for everything to be done.

### How to use? 
  
#### scan the license info  

You can type : 

scancode -l -n 2 --json-pp license.json samples 

in Windows 10 :

.\scancode -l -n 2 --json-pp copyright.json samples


(If you need extract your files,you can type :

scancode --extractcode -l -n 2 --json-pp license.json samples

in Windows 10 :

.\scancode --extractcode -l -n 2 --json-pp copyright.json samples)


**--extractcode** means extract all of your files in folder

**-l** means license scan

**-n 2** means 2 threads will be used in scan

**--json-pp** means json will be used for output format

**license.json** means the output report's name

**samples** means what folder you will scan

### Using docker
docker pull smartsyoung/compliance-zhangfei:v0.2  

docker run -v $PWD/:/project smartsyoung/compliance-zhangfei:v0.2 -l --json-pp /project/scan_result.json /project


## 中文介绍

### 张飞合规工具简介
Python编写的用于扫描开源版权合规性的工具，未来可以支持其他合规扫描。

### 为什么使用张飞合规工具
“开源合规性是开源软件的用户、集成商和开发人员遵守版权声明并履行其开源软件组件许可义务的过程”——Linux 基金会

### 张飞合规工具开发进展
现在，张飞合规工具处于原型阶段，它只是一个用于扫描软件许可证和其他元数据的 cli 工具。 

Vue-UI 和 Django_rest_api 正在开发中。 

我们的目的是建立一个专家系统，帮助使用开源软件的人很好地遵守他们的许可和版权义务。

### 如何配置环境
运行系统需求: Ubuntu Linux 20.04 (recommended) / M$ Windows 10 

环境搭建工具: VC buildTool (if M$ Windows) | Python 3.6+ | pip 20.3.3+

* **注意** : 如果想要在 windows 系统运行该工具，你应当先安装 VC buildTool 和 Windows SDK 。链接：(https://visualstudio.microsoft.com/zh-hans/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)

1 - 现在，你可以直接克隆该项目代码 

2 - 接下来只需要运行 "./configure" | Windows 10 系统只需要运行 ".\configure"

* **注意** : 如果使用 venv，您应该为 linux/windows 配置 pyvenv

这时你可以喝杯咖啡休息一下，马上项目就可以正常使用

### 如何使用张飞合规工具
  
#### 扫描许可证信息  

你可以键入 : 

scancode -l -n 2 --json-pp license.json samples 

Windows 10 系统可以键入 :

.\scancode -l -n 2 --json-pp copyright.json samples


(如果你的文件夹中有压缩包需要解压，你可以直接键入 :

scancode --extractcode -l -n 2 --json-pp license.json samples

Windows 10 系统可以键入 :

.\scancode --extractcode -l -n 2 --json-pp copyright.json samples)


**--extractcode** 表示解压文件夹中所有的压缩包（压缩包中仍含有压缩包也会被解压）

**-l** 表示扫描license

**-n 2** 表示使用两个线程扫描文件

**--json-pp** 表示将以json的格式输出结果

**license.json** 表示输出的文件名

**samples** 表示你将要扫描的文件夹

### 使用 docker
docker pull smartsyoung/compliance-zhangfei:v0.2  

docker run -v $PWD/:/project smartsyoung/compliance-zhangfei:v0.2 -l --json-pp /project/scan_result.json /project