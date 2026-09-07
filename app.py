import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("灯油価格看板変更用")

price_int = st.text_input("灯油価格（整数部）", value="116")

if st.button("128x192 PNG画像を生成"):
    # 1. テンプレート画像を読み込む
    img = Image.open("template.png").convert("RGB")
    draw = ImageDraw.Draw(img)

    # 2. フォントの指定
    try:
        font_num = ImageFont.truetype("DINBEK-Bold.ttf", 68)
    except Exception as e:
        st.error(f"フォント読み込みエラー: {e}")
        font_num = ImageFont.load_default()

    # 3. 文字間隔を調整しながら1文字ずつ描画
    start_x = 0          # 1文字目の描画開始X座標
    y_pos = 105          # Y座標
    letter_spacing = -8  # 文字間隔（マイナス値にすると字間が詰まります）

    current_x = start_x
    for char in price_int:
        # 1文字を描画
        draw.text((current_x, y_pos), char, fill=(255, 255, 255), font=font_num)
        # 描画した文字の横幅を取得し、次の文字の位置を計算
        char_width = draw.textlength(char, font=font_num)
        current_x += char_width + letter_spacing

    # 4. 最終サイズ（念のため指定サイズにリサイズ）
    resized = img.resize((128, 192), Image.Resampling.LANCZOS)
    output_filename = "値段看板(灯油).png"
    resized.save(output_filename, format="PNG")

    st.image(resized, caption="生成プレビュー (128x192px)")
    with open(output_filename, "rb") as f:
        st.download_button("PNG画像をダウンロード", f, file_name="price_board.png", mime="image/png")