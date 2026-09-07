import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("灯油価格看板変更用")

price_int = st.text_input("灯油価格（整数部）", value="116")

if st.button("128x192 PNG画像を生成"):
    # 1. 数字を消したテンプレート画像を読み込む
    img = Image.open("template.png").convert("RGB")
    draw = ImageDraw.Draw(img)

    # 2. 数字用のフォント（縦長で太いフォントがベスト）を指定
    # ※同じフォルダに Impact や 太字ゴシックの .ttf を置くと元画像に近づきます
    try:
        font_num = ImageFont.truetype("DINBEK-Bold.ttf", 110)
    except:
        font_num = ImageFont.load_default()

    # 3. 元の「116」があった位置（X, Y座標）に数字を描画
    # （テンプレート画像のサイズに合わせて X=20, Y=200 などの位置を微調整します）
    draw.text((20, 200), price_int, fill=(255, 255, 255), font=font_num)

    # 4. 最終サイズ（128x192）に縮小して保存
    resized = img.resize((128, 192), Image.Resampling.LANCZOS)
    output_filename = "値段看板(灯油).png"
    resized.save(output_filename, format="PNG")

    st.image(resized, caption="生成プレビュー (128x192px)")
    with open(output_filename, "rb") as f:
        st.download_button("PNG画像をダウンロード", f, file_name="price_board.png", mime="image/png")