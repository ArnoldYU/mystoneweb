用了django框架

如果你还未安装Python环境需要先下载Python安装包。
注意：目前Django 1.6.x以上版本已经完全兼容Python 3.x。
安装Python你只需要下载python-x.x.x.msi文件，然后一直点击"Next"按钮即可。
安装完成后你需要设置Python环境变量。 右击计算机->属性->高级->环境变量->修改系统变量path，添加Python安装地址，本文实例使用的是C:\Python27，你需要根据你实际情况来安装。

Django 安装（cmd里面）
下载 Django 压缩包，解压并和Python安装目录放在同一个根目录，进入 Django 目录，执行python setup.py install，然后开始安装，Django将要被安装到Python的Lib下site-packages。
然后是配置环境变量，将这几个目录添加到系统环境变量中： C:/Python27/Lib/site-packages/django;C:/Python27/Scripts。 添加完成后就可以使用Django的django-admin.py命令新建工程了。

输入以下命令进行检查:
python                   

import django
django.get_version()


如何启动网站，cmd 进入 mysite的位置 例如（cd c:/python/mysite）
然后运行manage.py runserver
网站打开127.0.0.1:8000
就可以进入网页了

网站功能是一个石材网站（网页是模仿http://www.hbshicaiwang.com/ ）
目前有效的连接是
		网页中的 “网站首页”“查看留言”“留言反馈”
		产品列表中的“黄金麻系列”“工程案例”（图片暂时用上面那个网站的图片，还没有更改）

目前只弄出这些来，后续还会继续修改（前段布局啥的会改变）