import streamlit as st
from src.verify import verify_signature

st.title("✍️ Signature Verification System")

img1 = st.file_uploader("Upload First Signature")
img2 = st.file_uploader("Upload Second Signature")

if img1 and img2:
    st.image(img1, caption="Signature 1")
    st.image(img2, caption="Signature 2")

    with open("temp1.png", "wb") as f:
        f.write(img1.read())

    with open("temp2.png", "wb") as f:
        f.write(img2.read())

    score = verify_signature("temp1.png", "temp2.png")

    st.write("### Similarity Score:", score)

    # 🔥 Updated threshold
    if score > 0.7:
        st.success("✅ Genuine Signature")
    else:
        st.error("❌ Forged Signature")