import os

print('...')
# 安装pexpect先
os.system('pip3 install pexpect')
import pexpect

# =必须配置=
# - rpmfusion 
os.system('dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y')
# - 更新
os.system('dnf update -y')
os.system('dnf upgrade -y')

print()
print("#################################")
print("选择安装包")

# =选择安装包=
# - 安装全部？
all_QuanBu = input('是否安装全部包？[y/n] ')
if (all_QuanBu == 'y'):
    supplement = ' -y'
else:
    supplement = ''

# - 视频录制软件
print('需要录屏软件simple screen recorder?')
x = pexpect.spawn('dnf install simplescreenrecorder' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")

# flac支持 
print('FLAC支持?')
x = pexpect.spawn('dnf install flac' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")

# Steam平台
print('Steam平台?')
x = pexpect.spawn('dnf install steam' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")

# Thunderbird
print('Thundirdbird Email Client?')
x = pexpect.spawn('dnf install thunderbird' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")

# polari(IRC)
print('Polari(An IRC Client)?')
x = pexpect.spawn('dnf install polari' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")


# chromium浏览器
print('Chromium浏览器?')
os.system('dnf copr enable churchyard/chromium-russianfedora -y')
x = pexpect.spawn('dnf install chromium' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")


# N卡驱动
print('N卡驱动?')
os.system('dnf install xorg-x11-drv-nvidia akmod-nvidia "kernel-devel-uname-r == $(uname -r)"' + supplement)
#print("*********************************")

# Dropbox
print('Dropbox?')
x = pexpect.spawn('dnf install dropbox' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")

# Xournal
print('Xournal?')
x = pexpect.spawn('dnf install xournal' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")

# StarDict

# Wine

# cmus
print('cmus音乐播放器?')
x = pexpect.spawn('dnf install cmus' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")


# lollypop音乐播放器

# terminix
print('terminix终端？')
os.system("dnf copr enable heikoada/terminix -y")
x = pexpect.spawn('dnf install terminix' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")


# gnome-tweak-tool
print("Gnome Tweak Tool?")
x = pexpect.spawn('dnf install gnome-tweak-tool' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")


# simple-scan
print('扫描仪？')
x = pexpect.spawn('dnf install simple-scan' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")


# teamspeak

# skype

# 格式转换

# Transmission

# p7zip

# Alarm Clock闹钟?
print('Alarm Clock闹钟?')
x = pexpect.spawn('dnf install ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/GNOME:/Apps/openSUSE_Factory+GNOME_Factory/x86_64/alarm-clock-applet-0.3.4-1.9.x86_64.rpm' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")


# 解码器
print('解码器multimedia codecs?')
x = pexpect.spawn('dnf install gstreamer1-plugins-base gstreamer1-plugins-good gstreamer1-plugins-ugly gstreamer1-plugins-bad-free gstreamer1-plugins-bad-free gstreamer1-plugins-bad-freeworld gstreamer1-plugins-bad-free-extras ffmpeg' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")

# virtualbox

# VLC播放器
print('VLC播放器?')
x = pexpect.spawn('dnf install vlc mozilla-vlc' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")

# mypaint
print('MyPaint?')
x = pexpect.spawn('dnf install mypaint' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")


#pitivi

#blender

#






print()
print("#################################")
print("开发工具")
# - 安装全部？
all_QuanBu = input('是否安装全部包？[y/n] ')
if (all_QuanBu == 'y'):
    supplement = ' -y'
else:
    supplement = ''

if (supplement == ''):
    jdk_boolean = input('安装Java SE Development Kit 8?[y/n] ')
if (supplement == ' -y' or jdk_boolean == 'y'):
    # JDK8
    print('手动下载:\nhttp://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html')
    print('选择对象:') 
    print('alternatives --config java')
    print('alternatives --config javac')
#print("*********************************")



print()
print("#################################")
print("个性设置")
# - 安装全部？
all_QuanBu = input('使用/安装全部个性配置？[y/n] ')
if (all_QuanBu == 'y'):
    supplement = ' -y'
else:
    supplement = ''

print(
"""1. 改头像
2. 改英文
3. 改键盘重复速度
4. 更改成x11模式，而非wayland
""")
# 解码器
print('Plank(一个非常棒的dock?)')
x = pexpect.spawn('dnf install plank' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")

# 字体
# Flash

# 字体渲染优化
print('字体渲染优化')
x = pexpect.spawn('dnf install freetype-freeworld' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("""然后添加或修改 ~/.Xresources

在 ~/.Xresources 里头添加如下一行：

Xft.lcdfilter: lcddefault""")
print("source from: https://polog.in/@hemashu/log/fedora-24-font-rendering-improvement")

print("*********************************")


print("gnome-shell-extension")
# Media player indicator 
# https://github.com/codito/gnome-pomodoro

# 解码器
print('PAPER主题?')
os.system("dnf config-manager --add-repo http://download.opensuse.org/repositories/home:snwh:paper/Fedora_25/home:snwh:paper.repo -y")
x = pexpect.spawn('dnf install paper-icon-theme paper-gtk-theme' + supplement)
x.interact()
if (x.isalive() == False):
    x.close()
print("*********************************")


print()
print("#################################")
print('Done!')





















