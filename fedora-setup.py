import pexpect
import os

print('...')
# 安装pexpect先
os.system('pip3 install pexpect')

# =必须配置=
# - rpmfusion 
#os.system('dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y')
# - 更新
os.system('dnf update -y')
os.system('dnf upgrade -y')

print()
print("#################################")
print("个性设置")

# =选装软件=
# - 安装全部？
all_QuanBu = input('是否安装全部包？[y/n]')
if (all_QuanBu == 'y'):
    supplement = ' -y'
else:
    supplement = ''

# 视频录制软件
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

# N卡驱动
print('N卡驱动?')
os.system('dnf install xorg-x11-drv-nvidia akmod-nvidia "kernel-devel-uname-r == $(uname -r)"' + supplement)
print("*********************************")

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

# lollypop音乐播放器

# terminix

# gnome-tweak-tool



















print()
print("#################################")
print("个性设置")
print(
"""1. 改头像
2. 改英文
3. 改键盘重复速度
4. 更改成x11模式，而非wayland
""")
print("gnome-shell-extension")

print()
print("#################################")
print('Done!')





















