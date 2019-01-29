# 第12章 作业，FTP

学完网络编程和并发编程这两部分可以看到，并没有太多的练习题。那么我们就来实现一个综合性的大作业来巩固所学。

## 12.1 功能概述

### 12.1.1 作业需求

首先让我们看下这个作业的需求什么。

- 注册
- 登录（支持多用户同时访问server端，并且在登录校验时，密码需要加密）
- 上传/下载文件，保证文件一致性
- 文件传输过程中实现进度条
- 支持断点续传
- 不同用户家目录不同，且只能访问自己的家目录，可以在自己的家目录内随意切换子目录
- 对用户进行磁盘配额，不同用户配额可不同
- 查看当前目录内的文件、目录
- 新建/删除文件夹
- 新建/删除文件
- 退出程序
- 用面向对象实现
- 支持扩展，比如再加几个需求

### 12.1.2 需求分析

由上一小节的需求来看，该作业必须支持可扩展，那就意味着我们在设计代码框架时，解耦合要放到第一位。只有提高了各功能之间的独立性，代码的扩展性才能提高。 在考虑扩展性之前，我们首先要简单的让程序在我们的`脑海`中运行一遍。大致的知道先干什么后干什么才好。

### 12.1.3 功能设计

我们在`脑海`中点击`run`按钮，程序第一步要干什么？登录或注册。是的，第一步就是登陆或者注册，用户所有的操作只有登录后才能完成。当注册或者登录后，应该让用户看到一个什么样的呈现？可以展示一个可供操作的列表，然后让用户选择序号进入具体的操作中。这个思路简单且易于实现，而且之前的作业中我们已经用过了(学生选课系统)。所以，这次我们试着来尝试新的思路。

- 默认进入家目录

当用户登录成功后，思考一个重要的问题，进到哪里？因为a用户不能方法b用户的数据。那就要在登录后就要为用户指定一个默认的目录。这很重要，因为仔细思考作业需求，所有的操作都是基于在某个目录下完成的。你可以在某个(当前)目录下，进行下载、上传、切换目录、创建、删除等操作；那么当你进入另一个目录后，这些操作也同样支持。所以，当用户登录成功后，默认进入家(根)目录。

- 命令 + 参数

现在，用户`oldboy`登录成功并且进入自己的家目录了。他要查看当前目录下都有什么内容。这个要求怎么实现呢？

我们可以理解为查看当前目录下的内容，是动作，我们就可以针对这个动作做具体的查询操作。那么该用户看到当前目录下有个`a.mp4`文件和`t1`目录，他想要下载`a.mp4`文件，我们又该如何做呢？这里我们可以认为`下载`也是动作，而想要的下载的`文件`则是一个具体的事物。 我们称`动作`为命令，而具体的事物则称为参数。我们在开发中，我们只要捕捉用户的命令以及参数来做具体的操作。但这里又要思考一个问题，有些命令(动作)是不需要参数的，比如退出功能。所以，我们要针对不同的命令有不同的处理办法。

### 12.1.4 约定

根据上一小节的命令和参数，我们可以在开发中与用户提前做个约定。比如，约定一个`dir`命令是用来查看当前目录有什么内容的。约定`quit`命令是用来退出程序的。 做好约定，只要用户输入对应的命令，我们就知道用户想干什么， 然后我们解析就好了。如果解析不了，那就意味着没有这个功能。可以给予相应的提示信息。 

约定如下：

| command | arguments | description                  |
| ------- | --------- | ---------------------------- |
| dir     | 无        | 查看当前目录内的文件或者目录 |
|         |           |                              |
|         |           |                              |



### 12.1.3 流程图

经过分析，我们可以画出流程图来更直观的理解作业需求。

![ftp](assets/ftp.bmp)



首先要知道，`ftp`作业是分`server`端和`client`端。那么就意味着

## 12.2 搭建框架

首先，创建如下的目录结构。

```python
'''
ftp/
    ├─ Client/
    │   ├─ bin/
    │   │   ├─ ftp_client.py
    │   │   └─ __init__.py
    │   ├─ conf/
    │   │   ├─ settings.py
    │   │   └─ __init__.py
    │   ├─ core/
    │   │   ├─ core.py
    │   │   └─ __init__.py
    │   ├─ db/
    │   │   └─ __init__.py
    │   └─ __init__.py
    ├─ Server/
    │   ├─ bin/
    │   │   ├─ ftp_server.py
    │   │   └─ __init__.py
    │   ├─ conf/
    │   │   ├─ settings.py
    │   │   └─ __init__.py
    │   ├─ core/
    │   │   ├─ core.py
    │   │   └─ __init__.py
    │   ├─ db/
    │   │   └─ __init__.py
    │   ├─ home/
    │   └─ __init__.py
    └─ __init__.py
'''
```



