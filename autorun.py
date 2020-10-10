from pywinauto import application
from pywinauto import timings
import time
import os

app = application.Application()
app.start("C:/KiwoomFlash3/Bin/NKMiniStarter.exe")

title = "번개3 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

# 로그인 비밀번호 입력
pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys('xxxx')

# 인증 비밀번호 입력
cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys('xxxx')

btn_ctrl = dlg.Button0
btn_ctrl.Click()

# 로그인 후 업데이트 시간을 고려하여 대기시간을 지정후 종료
time.sleep(40)
os.system("taskkill /im khmini.exe")

