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
                    st.title("箕島工場屋外の風景")
                    st.balloons()
                    st.toast('ログイン成功', icon='😍')
                    #st.info('只今、準備中．．．', icon="ℹ️") 

                    st.text('')
                    st.text('')
                    st.text('①ゴキブリ　その1')
                    image1 = Image.open('./data/1-1.jpg')
                    image2 = Image.open('./data/1-2.jpg')
                    image2_route = image2.rotate(90,expand=True)
                    image3 = Image.open('./data/1-3.jpg')
                    image3_route = image3.rotate(90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2_route)
                    img_list.append(image3_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('②ゴキブリ　その2')
                    image1 = Image.open('./data/2-1.jpg')
                    image2 = Image.open('./data/2-2.jpg')
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('③ゴキブリ　その3')
                    image1 = Image.open('./data/3-1.jpg')
                    image2 = Image.open('./data/3-2.jpg')
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('④ゴキブリ　その4')
                    image1 = Image.open('./data/4-1.jpg')
                    image2 = Image.open('./data/4-2.jpg')
                    image3 = Image.open('./data/4-3.jpg')
                    image3_route = image3.rotate(-90,expand=True)
                    image4 = Image.open('./data/4-4.jpg')
                    image5 = Image.open('./data/4-5.jpg')
                    image5_route = image5.rotate(90,expand=True)
                    image6 = Image.open('./data/4-6.jpg')
                    image6_route = image6.rotate(-90,expand=True)
                    image7 = Image.open('./data/4-7.jpg')
                    image7_route = image7.rotate(90,expand=True)
                    image8 = Image.open('./data/4-8.jpg')
                    image8_route = image8.rotate(90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    img_list.append(image3)
                    st.image(img_list,width=1000)
                    st.text('')
                    st.text('')
                    img_list = []
                    img_list.append(image4)
                    img_list.append(image5_route)
                    st.image(img_list,width=1000)
                    st.text('')
                    st.text('')
                    img_list = []
                    img_list.append(image6)
                    img_list.append(image7_route)
                    img_list.append(image8_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑤ゴキブリ　その5')
                    image1 = Image.open('./data/5-1.jpg')
                    image2 = Image.open('./data/5-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)
                    
                    st.text('')
                    st.text('')
                    st.text('⑥ゴキブリ　その6')
                    image1 = Image.open('./data/6-1.jpg')
                    image2 = Image.open('./data/6-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑦ゴキブリ　その7')
                    image1 = Image.open('./data/7-1.jpg')
                    image2 = Image.open('./data/7-2.jpg')
                    image2_route = image2.rotate(90,expand=True)
                    image3 = Image.open('./data/7-3.jpg')
                    image3_route = image3.rotate(90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    img_list.append(image3_route)
                    st.image(img_list,width=1000)
                             
                    st.text('')
                    st.text('')
                    st.text('⑧ゴキブリ　その8')
                    image1 = Image.open('./data/8-1.jpg')
                    image2 = Image.open('./data/8-2.jpg')
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑨ゴキブリ　その9')
                    image1 = Image.open('./data/9-1.jpg')
                    image2 = Image.open('./data/9-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑩ゴキブリ　その10')
                    image1 = Image.open('./data/10-1.jpg')
                    image2 = Image.open('./data/10-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑪ゴキブリ　その11')
                    image1 = Image.open('./data/11-1.jpg')
                    image2 = Image.open('./data/11-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)
                    
                    st.text('')
                    st.text('')
                    st.text('⑫工具が落ちている?')
                    image1 = Image.open('./data/12-1.jpg')
                    image2 = Image.open('./data/12-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2_route)
                    st.image(img_list,width=1000)
                   
                    st.text('')
                    st.text('')
                    st.text('⑬液漏れ?')
                    image1 = Image.open('./data/13-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑭ゴキブリ　その12')
                    image1 = Image.open('./data/14-1.jpg')
                    image2 = Image.open('./data/14-2.jpg')
                    image2_route = image2.rotate(90,expand=True)
                    image3 = Image.open('./data/14-3.jpg')
                    image3_route = image3.rotate(90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    img_list.append(image3_route)
                    st.image(img_list,width=1000)

                    
                    st.text('')
                    st.text('')
                    st.text('⑮ゴキブリ　その13')
                    image1 = Image.open('./data/15-1.jpg')
                    image2 = Image.open('./data/15-2.jpg')
                    image2_route = image2.rotate(90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                                        
                    st.text('')
                    st.text('')
                    st.text('⑯原料を屋外で保管　大丈夫?')
                    image1 = Image.open('./data/16-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    st.image(img_list,width=1000)


                    st.text('')
                    st.text('')
                    st.text('⑰ゴキブリ　その14')
                    image1 = Image.open('./data/17-1.jpg')
                    image2 = Image.open('./data/17-2.jpg')
                    image2_route = image2.rotate(90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                                        
                    st.text('')
                    st.text('')
                    st.text('⑱製品を屋外で保管　大丈夫?')
                    image1 = Image.open('./data/18-1.jpg')
                    image1_route = image1.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    st.image(img_list,width=1000)

                    
                    st.text('')
                    st.text('')
                    st.text('⑲ゴキブリ　その15')
                    image1 = Image.open('./data/19-1.jpg')
                    image2 = Image.open('./data/19-2.jpg')
                    image2_route = image2.rotate(90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)
                    
                    #　動画
                    st.text('')
                    st.text('')
                    st.text('⑳工場屋外で生きたゴキブリ発見')
                    video_file = open('./data/生きたゴキブリ.mp4','rb')
                    video_bytes = video_file.read()
                    st.video(video_bytes)

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


