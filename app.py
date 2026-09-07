import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("灯油価格看板変更用")

price_int = st.text_input("灯油価格（整数部）", value="116")

if st.button("128x192 PNG画像を生成"):
    # 1. テンプレート画像を読み込む
    img = Image.open("template.png").convert("RGB")
    draw = ImageDraw.Draw(img)

    # 2. フォントの指定（128x192の画像に合わせてサイズを縮小）
    try:
        # ⚠️ GitHubにあるファイル名と大文字・小文字・拡張子まで完全に一致させる必要があります
        font_num = ImageFont.truetype("DINBEK-Bold.ttf", 60)
    except Exception as e:
        # 読み込めなかった場合に画面に赤文字でエラーを出すように変更
        st.error(f"フォント読み込みエラー: {e}")
        font_num = ImageFont.load_default()

    # 3. 描画位置を画像の中に収める（X=10, Y=85 くらいに修正）
    draw.text((5, 135), price_int, fill=(255, 255, 255), font=font_num)

    # 4. 最終サイズ（念のため指定サイズにリサイズ）
    resized = img.resize((128, 192), Image.Resampling.LANCZOS)
    output_filename = "値段看板(灯油).png"
    resized.save(output_filename, format="PNG")

    st.image(resized, caption="生成プレビュー (128x192px)")
    with open(output_filename, "rb") as f:
        st.download_button("PNG画像をダウンロード", f, file_name="price_board.png", mime="image/png")