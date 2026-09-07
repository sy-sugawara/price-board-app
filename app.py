import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("灯油価格看板ジェネレーター")

price_int = st.text_input("灯油価格（整数部）", value="116")

if st.button("128x192 PNG画像を生成"):
    w, h = 320, 480
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 同じフォルダ内のフォントファイルを指定
    try:
        font_title = ImageFont.truetype("ipaexg.ttf", 36)
        font_label = ImageFont.truetype("ipaexg.ttf", 52)
        font_num = ImageFont.truetype("ipaexg.ttf", 110)
        font_small = ImageFont.truetype("ipaexg.ttf", 40)
    except:
        font_title = font_label = font_num = font_small = ImageFont.load_default()

    # 文字と背景の描画
    draw.text((30, 20), "プリカ最安値", fill=(230, 0, 18), font=font_title)
    draw.rectangle([0, 80, w, h], fill=(230, 0, 18))
    draw.text((80, 100), "灯  油", fill=(255, 255, 255), font=font_label)
    draw.text((20, 210), price_int, fill=(255, 255, 255), font=font_num)
    draw.text((230, 220), ".9", fill=(255, 255, 255), font=font_small)
    draw.text((210, 360), "円/ℓ", fill=(255, 255, 255), font=font_small)

    resized = img.resize((128, 192), Image.Resampling.LANCZOS)
    output_filename = "output_128x192.png"
    resized.save(output_filename, format="PNG")

    st.image(resized, caption="生成プレビュー (128x192px)")
    with open(output_filename, "rb") as f:
        st.download_button("PNG画像をダウンロード", f, file_name="price_board.png", mime="image/png")