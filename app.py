import re
import streamlit as st
import pandas as pd

st.header("ID CARD VIETNAM")

type_extract = ["Mặt sau CMT", "Mặt trước CCCD", "Mặt sau CCCD"]
type_IDCard = st.radio("Chọn loại giấy tờ",type_extract)

IdCard = st.file_uploader(f"Upload ảnh {type_IDCard}")

center = st.columns(1)[0]
if IdCard:
    center.image(IdCard)
    submit = center.button("Trích xuất thông tin")
    clear = center.button("Xóa ảnh")
else:
    submit = clear = False