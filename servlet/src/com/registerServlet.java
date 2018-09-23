package com;


import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@WebServlet("/registerServlet")
public class registerServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        response.setContentType("text/html,charset=utf-8");

        String username = request.getParameter("username");
        String password = request.getParameter("password");
        String repwd = request.getParameter("repwd");
        String telephone = request.getParameter("telephone");
        if (username.trim().isEmpty() || password.trim().isEmpty()) {
            request.setAttribute("msg", "用户名或密码不能为空！");
            request.getRequestDispatcher("/register.jsp").forward(request, response);
            return;
        }
        if (!repwd.equals(password)) {
            request.setAttribute("msg", "两次输入的密码不同！");
            request.getRequestDispatcher("/register.jsp").forward(request, response);
            return;
        }
        com.User userCheck = new com.userDAO().query(username);
        if (userCheck != null) {
            request.setAttribute("msg", "该用户名已被注册");
            request.getRequestDispatcher("/register.jsp").forward(request, response);
            return;
        }
        com.User user = new com.User();
        user.setUsername(username);
        user.setPassword(password);
        user.setRole(0);
        user.setTelephone(telephone);
        new com.userDAO().add(user);
        request.setAttribute("msg", "注册成功!");
        HttpSession session = request.getSession();
        session.setAttribute("username", username);
        request.getRequestDispatcher("/login.jsp").forward(request, response);
    }

    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request, response);
    }
}
