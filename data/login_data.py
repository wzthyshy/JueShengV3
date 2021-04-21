class LoginData(object):
    login_success_data = [
        (
            "汤直营",
            "0",
            "0000"
        )
    ]

    login_fail_data = [
        (
            "",
            "",
            "",
            "用户名不得为空"
        ),
        (
            "asd",
            "",
            "caa",
            "密码不得为空"
        ),
        (
            "linux",
            "xiaochao",
            "",
            "验证码不得为空"
        ),
        (
            "linux",
            "xiaochao",
            "122",
            "验证码输入有误"
        ),
        (
            "linux",
            "xiaochao",
            "0000",
            "用户或密码有误"
        )
    ]


if __name__ == '__main__':
    pass
