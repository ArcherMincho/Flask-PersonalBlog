<%@ page language="java" import="java.util.*" pageEncoding="UTF-8" %>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort() + path + "/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <base href="<%=basePath%>">

    <title>TomcatDemo Register</title>

    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="cache-control" content="no-cache">
    <meta http-equiv="expires" content="0">
    <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
    <meta http-equiv="description" content="This is my page">
    <!--
    <link rel="stylesheet" type="text/css" href="styles.css">
    -->
    <script type="text/javascript">
        function register(form) {
            if (form.username.value == "") {
                alert("ID不能为空！");
                return false;
            }
            if (form.password.value == "") {
                alert("密码不能为空！");
                return false;
            }

            if (form.repwd.value != form.password.value) {
                alert("两次输入密码不一致！");
                return false;
            }

        }
    </script>

</head>

<body>
<center>
    <div>
        <h1>注册</h1>
        <form action="registerServlet" onSubmit="return login(this);" method="post">
            请输入帐号：<input type="text" name="username"><br/>
            请输入密码：<input type="password" name="password"><br/>
            请确认密码：<input type="password" name="repwd"><br/>
            <input type="submit" value="注册">
        </form>
        <a href="login.jsp"><font size="2"><i>点击跳转登录页面</i></font></a>
        <font color="red" size="5"> ${msg }</font>
    </div>
</center>
</body>
</html>