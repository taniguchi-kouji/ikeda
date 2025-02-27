import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import sqlite3 
import hashlib
import subprocess
import sys

conn = sqlite3.connect('database.db')
c = conn.cursor()

conn2 = sqlite3.connect('NGdatabase.db')
c2 = conn2.cursor()

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def create_user():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_user(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def check_login_user(username,password):
    c2.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c2.fetchall()
    return data

def main():
    #st.title("ログイン画面")
    st.sidebar.title('ログイン・サインアップ')
    menu = ["ログイン","サインアップ"]
    choice = st.sidebar.selectbox("メニュー",menu)
    if choice == "ログイン":
        #st.subheader("ログイン画面です")
        username = st.sidebar.text_input("ユーザー名を入力してください")
        password = st.sidebar.text_input("パスワードを入力してください",type='password')
        if st.sidebar.button('ログイン'):
            create_user()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                password = username
                result2 = check_login_user(username,password)
                if result2:
                    st.sidebar.title("{}は利用権がありません".format(username))
                    st.snow()
                    st.toast('ログイン失敗', icon='😂')
                else:
                    st.sidebar.title("{}でログインしました".format(username)) 
                    st.title("箕島工場屋内の風景")
                    st.balloons()
                    st.toast('ログイン成功', icon='😍')
                   
                    # 画像
                    st.text('・原料仮置場の様子(封を開封しての保管)')
                    image1 = Image.open('./data/101-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    image2 = Image.open('./data/101-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    
                    st.text('')
                    st.text('')
                    st.text('・エアーシャワー有るのに未使用(入口と出口開放中)')
                    image1 = Image.open('./data/102-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    image2 = Image.open('./data/102-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    img_list.append(image2_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('・工場内のドア　開放中')
                    image1 = Image.open('./data/103-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('・工場内の壁埃だらけ')
                    image1 = Image.open('./data/104-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('・工場内ゴミだらけ')
                    image1 = Image.open('./data/105-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    image2 = Image.open('./data/105-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)
                   
                    st.text('')
                    st.text('')
                    st.text('・工場内に自転車?')
                    image1 = Image.open('./data/106-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    st.image(img_list,width=1000)
                   
                    st.text('')
                    st.text('')
                    st.text('・タンクと原料')
                    image1 = Image.open('./data/107-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('・錆だらけのタンク')
                    image1 = Image.open('./data/108-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('・沢山の製品タンク')
                    image1 = Image.open('./data/109-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('・一斗缶汚いパレット直置き異物混入大丈夫?')
                    image1 = Image.open('./data/110-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    st.image(img_list,width=1000)

                    
                    st.text('')
                    st.text('')
                    st.text('・原料 パレット直置き大丈夫?')
                    image1 = Image.open('./data/111-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    image2 = Image.open('./data/111-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    image3 = Image.open('./data/111-3.jpg')
                    image3_route = image3.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    img_list.append(image2_route)
                    img_list.append(image3_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('・「レモンダイス」無防備な保管体制')
                    image1 = Image.open('./data/112-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('・工場内にフォークリフト?')
                    image1 = Image.open('./data/113-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    st.image(img_list,width=1000)

                
                    st.text('')
                    st.text('')
                    st.text('・アセプ　調合室奇麗ですが、階段は埃だらけ')
                    image1 = Image.open('./data/114-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    image2 = Image.open('./data/114-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    image3 = Image.open('./data/114-3.jpg')
                    image3_route = image3.rotate(-90,expand=True)
                    image4 = Image.open('./data/114-4.jpg')
                    image4_route = image4.rotate(-90,expand=True)
                    image5 = Image.open('./data/114-5.jpg')
                    image5_route = image5.rotate(-90,expand=True)
                    image6 = Image.open('./data/114-6.jpg')
                    image6_route = image6.rotate(-90,expand=True)
                    image7 = Image.open('./data/114-7.jpg')
                    image7_route = image7.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    img_list.append(image3)
                    img_list.append(image4)
                    img_list.append(image5)
                    img_list.append(image6)
                    img_list.append(image7)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('・レトルト工場ですが奇麗です')
                    image1 = Image.open('./data/115-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    image2 = Image.open('./data/115-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    image3 = Image.open('./data/115-3.jpg')
                    image3_route = image3.rotate(-90,expand=True)
                    image4 = Image.open('./data/115-4.jpg')
                    image4_route = image4.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    img_list.append(image3)
                    img_list.append(image4)
                    st.image(img_list,width=1000)
                    
                    st.text('')
                    st.text('')
                    st.text('・パレットを立てて保管は危険です')
                    image1 = Image.open('./data/116-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    st.image(img_list,width=1000)
                    
                    st.info('随時更新予定．．．', icon="ℹ️") 
            else:
                st.warning("ユーザー名かパスワードが間違っています")
                st.snow()
                st.toast('ログイン失敗', icon='😂')

    elif choice == "サインアップ":
        st.subheader("新しいアカウントを作成します")
        new_user = st.text_input("ユーザー名を入力してください")
        new_password = st.text_input("パスワードを入力してください",type='password')
        if st.button("サインアップ"):
            create_user()
            add_user(new_user,make_hashes(new_password))
            st.success("アカウントの作成に成功しました")
            st.info("ログイン画面からログインしてください")
            st.balloons()
            st.toast('サインアップ成功', icon='😍')
            
if __name__ == '__main__':
    main()
