## Install PostgreSQL 11 and PgAdmin4 on Ubuntu 18.04

### PostgreSQL

PostgreSQL is a free and open source cross-platform Relational Database Management System (RDBMS). It is widely used by developers in the development environment and in production environments as well. PostgreSQL 11 was released in November 2018 and comes with a wealth of new and exciting features.

### PgAdmin


PgAdmin 4 is a free and open source web-based administration and development platform that helps users to administer, manage and monitor Postgres databases in a graphical manner. Let’s now dive in and see how we can install the two.

#### Install PostgreSQL on Ubuntu

#### Step 1: Importing GPG key & adding PostgreSQL APT repository

To get started, begin by importing the GPG key for the PostgreSQL packages. Use the command below to download the CA certificates.

```
$ sudo apt install wget ca-certificates
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
$ sudo apt-get update
$ sudo apt-get install postgresql postgresql-contrib
$ sudo su - postgres
psql
postgres-# \conninfo
quit
exit

$ sudo apt-get install pgadmin4 pgadmin4-apache2

Enter email and password in popup window when appears
```
#### Connecting to PgAdmin4
open browser and type `http://127.0.0.1:39621/browser/` for your local system  or either your `http://server-ip:39621/browser/`





