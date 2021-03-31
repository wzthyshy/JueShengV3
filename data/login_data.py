class LoginData(object):
    login_success_data = [
        (
            "linuxxiaochao",
            "xiaochao11520",
            "linuxxiaochao@126.com"
        )
    ]

    login_fail_data = [
        (
            "linuxxiaochao",
            "",
            "请输入密码"
        ),
        (
            "",
            "xiaochao11520",
            "请输入帐号"
        ),
        (
            "linux",
            "xiaochao",
            "帐号或密码错误"
        )
    ]


if __name__ == '__main__':
    pass
