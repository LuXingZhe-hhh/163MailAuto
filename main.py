import pywinauto
import lackey
import time
import pyautogui

# 启动Edge浏览器
path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
app = pywinauto.Application().start(path)
# 如果打开的浏览器是缩小的窗口，定位到“windows.png”处，点击
windows = lackey.exists('photo\windows.png')
if windows:
    lackey.click('photo\windows.png')
# 定位到搜索框并键入“163”
lackey.click('photo\SearchBox.png')
lackey.type('163')
# 选择下拉选项框中的“163邮箱"
lackey.click('photo\mail.png')
# 点击网页中的“163网易免费邮”
lackey.click('photo\wangyiMail.png')
# 定位到账号处，输入邮箱账号
# lackey.click('photo\account.png')
# lackey.type('luxingzhe666')
#定位到密码处，输入邮箱密码
lackey.click('photo\password.png')
lackey.type('pcd1817000093')
#定位到登录处，点击登录
lackey.click('photo\login.png')
# 定位到“写信”，点击
lackey.click('photo\XieXin.png')
# 定位到“收件人”，并输入“2558970169@qq.com”
lackey.click('photo\ShouJianRen.png')
lackey.type('2558970160@qq.com')
# pyautogui.press(['2','5','5','8','9','7','0','1','6','0','@','q','q','.','c','o','m'])
pyautogui.press('enter') # pyautogui库中的，按“回车”
# 定位到主题，并键入主题
lackey.click('photo\ZhuTi.png')
lackey.type('Test  Mail ')
# 定位到正文“text.png”，并输入正文
lackey.click('photo\ext2.png')
#
lackey.type('Hi')
pyautogui.press('enter')
lackey.type(',')
lackey.type(' ')
lackey.type('this')
pyautogui.press('enter')
lackey.type(' ')
lackey.type('is')
pyautogui.press('enter')
lackey.type(' ')
lackey.type('my')
pyautogui.press('enter')
lackey.type(' ')
lackey.type('test')
pyautogui.press('enter')
lackey.type(' ')
lackey.type('mail')
pyautogui.press('enter')
lackey.type('.')
# 发送并退出
lackey.click('photo\FaSong.png')
lackey.click('photo\ShouYe.png')
lackey.click('photo\qqhao.png')
lackey.click('photo\TuiChu.png')



