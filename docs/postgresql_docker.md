# postgresSQL

## Docker 安裝postgres
下載docker desktop\
https://www.docker.com/get-started/

https://www.netapp.com/zh-hant/devops-solutions/what-are-containers/


拉最新版image
```
docker pull postgres
```
建立 container，設定 port 號，設定 postgres 最高權限的登入密碼 \
一定要指定port對應，官網上的說明沒有指定，在我的環境不會自動對應，會導致連不上
```
docker create --name my-postgres -p 5432:5432 -e POSTGRES_PASSWORD=123456 postgres
```
執行 container
```angular2html
docker start my-postgres
```
查看版本
```angular2html
docker exec my-postgres psql -V
```

## 安裝 client db tool
https://www.pgadmin.org/download/

好像最多人用，這就不細講，工具都大同小異

## 資料庫連線字串
DRIVER = 'psycopg2' -->這裡會覺得安裝psycopg2，但不會動，要psycopg2-binary\
client_encoding=utf8" -->這要指定編碼
```angular2html
DIALECT = 'postgresql'
DRIVER = 'psycopg2'
USERNAME = 'postgres'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '5432'
DATABASE = 'wbs'
DB_URI = "{}+{}://{}:{}@{}:{}/{}?client_encoding=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
```

## 安裝 db driver
不能裝psycopg2，要psycopg2-binary，裝最新版即可
```angular2html
pip install psycopg2-binary
```
