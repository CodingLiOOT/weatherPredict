<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>用户注册</title>
    <meta name="author" content="zzh" />
    <link rel="stylesheet" href="css/register.css" />
</head>
<body>
<div class="register-box">
    <div class="register-title">气温预测系统用户注册</div>
    <div class="register-form">
        <form action="" id="form">
            <!--账户名-->
            <div class="form-item user">
                <div class="form-ctrl">
                    <input type="text" id="userID" name="username" placeholder="请输入用户名" style="vertical-align:top">
                </div>
                <div class="form-tips">
                    <span class="error" id="user_error" style="display: none;">用户名不能为空</span>
                </div>
            </div>
            <!--密码-->
            <div class="form-item pass">
                <div class="form-ctrl">
                    <input type="password" id="userPassword" name="password" placeholder="请输入密码">
                </div>
                <div class="form-tips">
                    <span class="error" id="pass_error" style="display: none;">密码不能为空</span>
                </div>
            </div>
            <div class="form-item pass-again">
                <div class="form-ctrl">
                    <input type="password" id="userPassword-again" name="password" placeholder="请再次输入密码">
                </div>
                <div class="form-tips">
                    <span class="error" id="pass_error-again" style="display: none;">密码不能为空</span>
                </div>
            </div>
            <!--登录按钮-->
            <div class="form-item form-button">
                <button type="button" class="button" >注册 </button>
            </div>

        </form>
    </div>
</div>
</body>
</html>
