import streamlit as st
from aip import AipImageClassify
import chardet
APP_ID = '28403043'  # APP_ID
API_KEY = '4lYddF4ByuwIqdKCOEV0yQ5U'  # API_KEY
SECRET_KEY = '3bthDQ9FH14qg9R5KVFiBW2xFURimjQq'  # SECRET_KEY

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

# 网站标题
st.title('动物识别')

# 图片选择框
uploaded_file = st.file_uploader('选择一张图片', type=['jpg', 'png', 'bmp', 'gif'])
if uploaded_file is not None:
    # 显示已选的文件
    st.image(uploaded_file, caption='已选文件', use_column_width=True)
    bs = uploaded_file.read()

    """ 动物识别结果 """
    options = {"top_num": 3}
    res = client.animalDetect(bs, options)  # 调用百度api识别动物
    res['result']  # 显示输出结果（最有可能）

    """ 该动物最有可能是 """, res['result'][0]['name']  # 取预测概率最大的结果
    """ 也有可能是 """, res['result'][1]['name'], """和""", res['result'][2]['name']