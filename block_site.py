import shutil
print('='*60)
print('특정 사이트 접속 차단 프로그램입니다.\nlink.txt에 차단을 원하는 사이트의 주소를 입력해주세요.\n"차단"을 입력하면 차단, "해제"를 입력하면 해제가 됩니다.')
print('='*60)
while True:
    menu = input('차단? 해제? ')
    if menu == '차단':
        shutil.copy("C:\Windows\System32\drivers\etc\hosts", "host.txt")
        f = open("link.txt", 'r')
        s = f.readline()
        f.close()
        with open("C:\Windows\System32\drivers\etc\hosts", 'a') as f:
            f.write("\n127.0.0.1 "+s)
        print('\n차단되었습니다! 재부팅해주세요!')
        break
    elif menu == '해제':
        f = open("host.txt", 'r')
        s = f.read()
        f.close()
        with open("C:\Windows\System32\drivers\etc\hosts", 'w') as f:
            f.write(s)
        print('\n해제되었습니다! 재부팅해주세요!')
        break
    else:
        print('\n"차단" 또는 "해제"를 입력해주세요!\n(다시 시도해보세요)')
        continue
