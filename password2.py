# 教學版本
# 密碼重試程式
# 先在程式碼中 設定好密碼password = 'a1234'
# 讓使用者'最多嘗試輸入3次密碼'
# 不正確就顯示'密碼錯誤' 還有_次機會
# 對的話顯示'登入成功'

password = 'a1234'
i = 3 #剩餘機會
while True:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    else:
        i = i - 1
        print('密碼錯誤,', '還有', i, '次機會')
        if i == 0:
            break


