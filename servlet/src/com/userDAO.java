package com;


import java.sql.*;

public class userDAO {

    private static String USER = "root";
    private static String PASSWORD = "qing1234.";
    private static String DB_URL = "jdbc:mysql://localhost:3306/tomcatdemo?serverTimezone=GMT";
    private static String DRIVER = "com.mysql.cj.jdbc.Driver";
    public Connection connection = null;
    public PreparedStatement pstatement = null;
    public ResultSet resultset = null;

    public userDAO() {
        try {
            Class.forName(DRIVER);
            connection = DriverManager.getConnection(DB_URL, USER, PASSWORD);
        } catch (ClassNotFoundException e) {
            System.out.println("------------------------ClassError");
            e.printStackTrace();
        } catch (SQLException e) {
            System.out.println("-------------------------SQLError");
            e.printStackTrace();
        }
    }


    public void closeAll() {
        try {
            if (resultset != null) {
                resultset.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (pstatement != null) {
                    pstatement.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            } finally {
                try {
                    if (connection != null) {
                        connection.close();
                    }
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public User query(String name) {
        User user = new User();
        String sql = "SELECT * FROM users WHERE username = ?";

        try {
            pstatement = connection.prepareStatement(sql);
            pstatement.setString(1, name);
            resultset = pstatement.executeQuery();
            if (!resultset.next()) {
                return null;
            } else{
                user.setUsername(resultset.getString("username"));
                user.setPassword(resultset.getString("password"));
                user.setRole(resultset.getInt("role"));
                user.setTelephone(resultset.getString("telephone"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }
        return user;
    }

    public boolean add(User user) {
        boolean flag = false;
        String sql = "INSERT users(username,password,role,telephone) VALUES(?,?,?,?)";

        try {
            pstatement = connection.prepareStatement(sql);
            pstatement.setString(1, user.getUsername());
            pstatement.setString(2, user.getPassword());
            pstatement.setInt(3, user.getRole());
            pstatement.setString(4, user.getTelephone());
            if (pstatement.executeUpdate() > 0) {
                flag = true;
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }
        return flag;
    }

    public boolean delete(User user) {
        boolean flag = false;
        String sql = "DELETE FROM users WHERE username=? ";

        try {
            pstatement = connection.prepareStatement(sql);
            pstatement.setString(1, user.getUsername());
            if (pstatement.executeUpdate() > 0) {
                flag = true;
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }
        return flag;
    }


}
