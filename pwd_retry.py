pwd = 'a123456'
retry_count = 3
while True:
	user_pwd = input('請輸入密碼:')
	if user_pwd == pwd:
		print('登入成功')
		break
	else:
		retry_count = retry_count - 1 
		print('密碼錯誤!還有',retry_count,'機會')
		if retry_count < 1:
			break
