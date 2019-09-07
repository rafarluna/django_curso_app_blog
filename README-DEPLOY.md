# instalacion

## instalar virtualenv
sudo apt update
sudo apt install python3-pip
sudo pip3 install virtualenv

virtualenv env --python=python3
source env/bin/activate

## clonar proyecto

git clone https://darkkase@bitbucket.org/darkkase/bedu_blog_example.git

cd bedu_blog_example

(pip freeze > requirments.txt)
pip install -r requirments.txt

## instalar y configurar nginx 

sudo apt install nginx
 
sudo rm  /etc/nginx/sites-enabled/default 
 
sudo nano /etc/nginx/sites-enabled/default 

>server {
>    listen 80;
>    server_name example.org;
>    access_log  /var/log/nginx/blog.log;
>
>    location / {
>        proxy_pass http://127.0.0.1:8000;
>        proxy_set_header Host $host;
>        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
>    }
>
>  }

sudo service nginx restart

## instalar y configurar supervisor

sudo apt install supervisor
sudo nano /etc/supervisor/supervisord.conf 

>[program: blog]
>command=/home/ubuntu/env/bin/gunicorn blog_test.wsgi
>directory=/home/ubuntu/bedu_blog_example/
>user=ubuntu
>autostart=true
>autorestart=true
>redirect_stderr=true


sudo supervisorctl reload
