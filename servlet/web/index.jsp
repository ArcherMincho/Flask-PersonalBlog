<%@ page language="java" import="java.util.*" pageEncoding="UTF-8" %>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort() + path + "/";
%>

<%
    if(session.getAttribute("username") == null){
        out.println("<a href=\"register.jsp\"><font size=\"2\"><i>没有帐号？点击注册</i></font></a>\n");
        out.println("</br>");
        out.println("<a href=\"login.jsp\"><font size=\"2\"><i>点击跳转登录页面</i></font></a>\n");
    }else {
        String username = session.getAttribute("username").toString();
        out.println("Welcome " + username + " to Echo's Java Web Demo");
    }
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <base href="<%=basePath%>">

    <title>My JSP 'welcome.jsp' starting page</title>

    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="cache-control" content="no-cache">
    <meta http-equiv="expires" content="0">
    <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
    <meta http-equiv="description" content="This is my page">
    <!--
    <link rel="stylesheet" type="text/css" href="styles.css">
    -->

</head>

<body>
<h1>TomcatDemo Home Here</h1>
<h2>${msg }</h2>
</body>
</html>