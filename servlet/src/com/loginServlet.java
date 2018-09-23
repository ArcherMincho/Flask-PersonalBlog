package com;



import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;


@WebServlet("/loginServlet")
public class loginServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        response.setContentType("text/html;charset=utf-8");

        String username = request.getParameter("username");
        String password = request.getParameter("password");
        if (username.trim().isEmpty() || password.trim().isEmpty()) {
            request.setAttribute("msg", "用户名或密码不能为空！");
            request.getRequestDispatcher("/login.jsp").forward(request, response);
            return;
        }
        com.User user = new com.userDAO().query(username);
        if (user == null) {
            request.setAttribute("msg", "不存在该用户！");
            request.getRequestDispatcher("/login.jsp").forward(request, response);
            return;
        }
        if (!user.getPassword().equals(password)) {
            request.setAttribute("msg", "密码错误！");
            request.getRequestDispatcher("/login.jsp").forward(request, response);
            return;
        }
        HttpSession session = request.getSession();
        session.setAttribute("username", username);
        ServletContext context = this.getServletContext();
        System.out.println(context.getContextPath());
        request.getRequestDispatcher("homeServlet").forward(request, response);
    }


    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request, response);
    }
}