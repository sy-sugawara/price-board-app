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
        font_num = ImageFont.truetype("bahnschrift.ttf", 72)
    except Exception as e:
        st.error(f"フォント読み込みエラー: {e}")
        font_num = ImageFont.load_default()

    # 3. 指定領域の中央に文字を配置して描画
    center_x = 45       # 数字を表示したい領域の中心X座標（要微調整）
    y_pos = 115         # Y座標
    letter_spacing = -4 # 字間

    # 文字列全体の合計幅を計算
    total_width = sum(draw.textlength(c, font=font_num) for c in price_int)
    if len(price_int) > 1:
        total_width += letter_spacing * (len(price_int) - 1)

    # 中央揃えになる開始X座標を算出
    start_x = center_x - (total_width / 2)

    # 算出された位置から1文字ずつ描画
    current_x = start_x
    for char in price_int:
        draw.text((current_x, y_pos), char, fill=(255, 255, 255), font=font_num)
        char_width = draw.textlength(char, font=font_num)
        current_x += char_width + letter_spacing

    # 4. 最終サイズ（念のため指定サイズにリサイズ）
    resized = img.resize((128, 192), Image.Resampling.LANCZOS)
    output_filename = "値段看板(灯油).png"
    resized.save(output_filename, format="PNG")

    st.image(resized, caption="生成プレビュー (128x192px)")
    with open(output_filename, "rb") as f:
        st.download_button("PNG画像をダウンロード", f, file_name="price_board.png", mime="image/png")