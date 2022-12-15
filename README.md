# Django-Warehouse-App

# Getting Started
*python ==3.7 or up and django == 3 or up*
## Installing
open terminal and type 
    
    git clone https://github.com/getroundintheseason/warehouseWEB.git
    cd warehouse
    pip3 install -r requirements.txt

## Migrate the database
    python3 manage.py makemigrations
    python3 manage.py migrate
    
## Create admin account
    python3 manage.py createsuperuser

## Run the website!!
    python3 manage.py runserver

# Register User
可以提供使用者註冊及登入帳號

# 目的
紀錄蒐藏品的 *分類* *位置* *有沒有出界* 等資訊

# Collection 蒐藏 功能
-  CollectionDetail 瀏覽 蒐藏
-  CollectionCreate 新增 蒐藏
-  CollectionUpdate 更新 蒐藏
-  CollectionDelete 刪除 蒐藏

