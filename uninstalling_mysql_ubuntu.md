### Uninstalling MySQL from Ubuntu

`sudo apt-get remove --purge mysql*`

`sudo apt-get purge mysql*`

`sudo apt-get autoremove`

`sudo apt-get autoclean`

`sudo apt-get remove dbconfig-mysql`

`sudo apt-get dist-upgrade`


### Installing MySQL in Ubuntu

`sudo apt-get install mysql-server`
`sudo mysql`
`SELECT user,authentication_string,plugin,host FROM mysql.user;`
`ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';`
`FLUSH PRIVILEGES;`
`exit`
`mysql -u root -ppassword`
