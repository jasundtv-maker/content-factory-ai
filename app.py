import streamlit as st
import google.generativeai as genai
from datetime import datetime

st.set_page_config(page_title="Content Factory AI V5", page_icon="🚀", layout="wide")

st.markdown("""
<style>
.card{
background:#1f2937;padding:22px;border-radius:18px;
border:1px solid #374151;margin-bottom:18px;
}
.hero{font-size:42px;font-weight:900;}
.muted{color:#9ca3af;}
.step{
background:#111827;padding:16px;border-radius:14px;
border:1px solid #374151;margin-bottom:12px;
}
</style>
""", unsafe_allow_html=True)

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

def generate_ai(prompt):
    if not st.session_state.api_key:
        return "MODE DEMO AKTIF\n\nMasukkan Gemini API Key di Settings agar hasil AI asli keluar."

    try:
        genai.configure(api_key=st.session_state.api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        return "API ERROR - MODE DEMO AKTIF\n\nGemini API sedang limit atau API key bermasalah."

def output_box(title, text, key):
    st.markdown(f"### {title}")
    st.text_area("Copy dari sini", text, height=260, key=key)
    st.download_button(
        f"⬇️ Download {title}",
        text,
        file_name=f"{title.replace(' ','_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain"
    )

st.sidebar.title("🚀 Content Factory AI V5")
menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "🏠 Dashboard",
        "🛍️ Affiliate Ultimate",
        "🎬 Film Ultimate",
        "🕌 Dakwah Ultimate",
        "🌴 Luxury Music",
        "⚙️ Settings"
    ]
)

st.markdown("<div class='hero'>🚀 Content Factory AI V5 Ultimate</div>", unsafe_allow_html=True)
st.markdown("<div class='muted'>Studio konten AI untuk Affiliate, Film, Dakwah, dan Luxury Music.</div>", unsafe_allow_html=True)
st.divider()

if menu == "🏠 Dashboard":
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='card'><h3>🛍️ Affiliate Ultimate</h3><p>UGC, Commercial, Mirror Check, POV Review.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><h3>🎬 Film Ultimate</h3><p>Karakter referensi, storyboard, dialog, prompt video.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><h3>🕌 Dakwah Ultimate</h3><p>Judul, narasi, thumbnail, prompt visual, hashtag.</p></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='card'><h3>🌴 Luxury Music</h3><p>Deep House / Chill House target US.</p></div>", unsafe_allow_html=True)

elif menu == "⚙️ Settings":
    st.subheader("⚙️ Settings")
    api_key = st.text_input("Gemini API Key", type="password")
    if st.button("💾 Simpan API Key"):
        st.session_state.api_key = api_key
        st.success("API Key tersimpan.")
    st.warning("Jangan tampilkan API key di screenshot.")

elif menu == "🛍️ Affiliate Ultimate":
    st.subheader("🛍️ Affiliate Pro Generator Ultimate")

    st.markdown("<div class='step'><b>01. Pilih Mode Visual</b></div>", unsafe_allow_html=True)
    mode_visual = st.radio(
        "Mode Visual",
        ["UGC Natural", "Commercial", "Mirror Check", "POV Hand Review", "CEO Luxury"],
        horizontal=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='step'><b>02. Upload Model / Base Model</b></div>", unsafe_allow_html=True)
        model_img = st.file_uploader("Upload foto model", type=["jpg", "jpeg", "png"], key="model_aff")
        if model_img:
            st.image(model_img, caption="Model Referensi", width=260)

    with col2:
        st.markdown("<div class='step'><b>03. Upload Produk</b></div>", unsafe_allow_html=True)
        product_img = st.file_uploader("Upload foto produk", type=["jpg", "jpeg", "png"], key="product_aff")
        if product_img:
            st.image(product_img, caption="Produk Referensi", width=260)

    st.markdown("<div class='step'><b>04. Detail Kampanye</b></div>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)

    with col3:
        product_name = st.text_input("Nama Produk")
        product_desc = st.text_area("Deskripsi Produk")
        target = st.selectbox("Target Audience", ["Indonesia", "USA"])
        engine = st.selectbox("Mesin Video", ["Opal", "Omni Flash", "Gemini", "Seedance", "Kling"])

    with col4:
        platform = st.selectbox("Platform", ["TikTok Affiliate", "YouTube Shorts", "Instagram Reels", "Facebook Reels"])
        duration = st.selectbox("Durasi", ["8 detik", "15 detik", "30 detik", "60 detik"])
        bahasa = "Bahasa Indonesia" if target == "Indonesia" else "English"
        model_desc = st.text_area("Deskripsi Model", placeholder="Contoh: perempuan muda memakai outfit casual")

    if st.button("🚀 Generate Affiliate Ultimate"):
        prompt = f"""
Buatkan paket konten affiliate profesional.

MODE VISUAL: {mode_visual}
PRODUK: {product_name}
DESKRIPSI PRODUK: {product_desc}
DESKRIPSI MODEL: {model_desc}
TARGET: {target}
BAHASA: {bahasa}
PLATFORM: {platform}
DURASI: {duration}
MESIN VIDEO: {engine}

User memakai foto model dan foto produk sebagai referensi.

Output wajib dipisah rapi:
1. JUDUL KONTEN
2. HOOK 3 DETIK
3. SCRIPT VIDEO
4. STORYBOARD 5 SCENE
5. PROMPT IMAGE TO VIDEO UNTUK {engine}
6. PROMPT THUMBNAIL
7. CTA KERANJANG KUNING
8. HASHTAG
9. NEGATIVE PROMPT SUPER KETAT

Aturan produk:
- produk harus 100% sama seperti foto referensi
- jangan ubah warna, logo, bentuk, tulisan, bahan, ukuran, motif
- jangan tambah aksesoris
- jangan hilangkan detail produk
- jangan produk blur
- jangan produk dobel
- jangan produk berubah desain
- jangan mengubah wajah model
- jangan mengubah pakaian model jika memakai referensi
- gerakan natural, realistis, cinematic
"""
        hasil = generate_ai(prompt)
        output_box("🛍️ Hasil Affiliate Ultimate", hasil, "affiliate_ultimate_result")

elif menu == "🎬 Film Ultimate":
    st.subheader("🎬 Film AI Ultimate")

    st.markdown("<div class='step'><b>01. Upload Karakter</b></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)

    with c1:
        char1 = st.file_uploader("Karakter Utama", type=["jpg", "jpeg", "png"], key="char1")
        if char1:
            st.image(char1, caption="Karakter Utama", width=220)

    with c2:
        char2 = st.file_uploader("Karakter Kedua", type=["jpg", "jpeg", "png"], key="char2")
        if char2:
            st.image(char2, caption="Karakter Kedua", width=220)

    with c3:
        char3 = st.file_uploader("Karakter Ketiga", type=["jpg", "jpeg", "png"], key="char3")
        if char3:
            st.image(char3, caption="Karakter Ketiga", width=220)

    st.markdown("<div class='step'><b>02. Detail Film</b></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        genre = st.selectbox("Genre", ["Komedi Kampung", "Drama", "Action", "Horor", "CEO Story", "Romantis Aman"])
        target = st.selectbox("Target Audience", ["Indonesia", "USA"], key="film_target")
        engine = st.selectbox("Mesin Video", ["Opal", "Omni Flash", "Gemini", "Seedance", "Kling"], key="film_engine")

    with col2:
        scene_count = st.selectbox("Jumlah Scene", [5, 10])
        idea = st.text_area("Ide Cerita")
        style = st.text_input("Gaya Visual", value="realistis, sinematik, natural, tanpa subtitle")

    if st.button("🚀 Generate Film Ultimate"):
        prompt = f"""
Buatkan paket film pendek AI.

GENRE: {genre}
TARGET: {target}
MESIN VIDEO: {engine}
JUMLAH SCENE: {scene_count}
IDE CERITA: {idea}
GAYA VISUAL: {style}

User memakai foto karakter sebagai referensi.

Output wajib:
1. JUDUL FILM
2. SINOPSIS
3. DAFTAR KARAKTER
4. STORYBOARD {scene_count} SCENE
5. PROMPT VIDEO PER SCENE UNTUK {engine}
6. DIALOG PER SCENE
7. PROMPT THUMBNAIL
8. NEGATIVE PROMPT SUPER KETAT
9. CATATAN TEKNIS

Aturan:
- wajah karakter harus sama dengan referensi
- pakaian tetap sama
- umur tetap sama
- bentuk tubuh tetap sama
- jangan ganti identitas karakter
- jangan ada subtitle
- jangan ubah wajah antar scene
- jangan ubah pakaian antar scene
- gerakan natural dan realistis
"""
        hasil = generate_ai(prompt)
        output_box("🎬 Hasil Film Ultimate", hasil, "film_ultimate_result")

elif menu == "🕌 Dakwah Ultimate":
    st.subheader("🕌 Dakwah AI Ultimate")

    col1, col2 = st.columns(2)

    with col1:
        tema = st.text_input("Tema Dakwah")
        target = st.selectbox("Target Audience", ["Indonesia", "USA"], key="dakwah_target")
        durasi = st.selectbox("Durasi", ["60 detik", "3 menit", "10 menit"])
        gaya = st.selectbox("Gaya Narasi", ["Menyentuh", "Tegas", "Tenang", "Dramatis", "Lucu Hikmah"])

    with col2:
        ref = st.file_uploader("Upload gambar referensi opsional", type=["jpg", "jpeg", "png"], key="dakwah_ref")
        if ref:
            st.image(ref, caption="Referensi", width=260)

    if st.button("🚀 Generate Dakwah Ultimate"):
        prompt = f"""
Buatkan paket konten dakwah profesional.

TEMA: {tema}
TARGET: {target}
DURASI: {durasi}
GAYA: {gaya}

Output wajib dipisah:
1. 10 PILIHAN JUDUL
2. 5 HOOK PEMBUKA
3. NASKAH NARASI {durasi}
4. THUMBNAIL TEXT
5. PROMPT GAMBAR THUMBNAIL
6. PROMPT VIDEO ISLAMI
7. VOICE OVER SCRIPT
8. DESKRIPSI YOUTUBE
9. HASHTAG
10. KEYWORD SEO

Gaya bahasa:
- sopan
- menyentuh
- mudah dipahami
- tidak berlebihan
- sesuai target audience
"""
        hasil = generate_ai(prompt)
        output_box("🕌 Hasil Dakwah Ultimate", hasil, "dakwah_ultimate_result")

elif menu == "🌴 Luxury Music":
    st.subheader("🌴 Luxury Music AI")

    col1, col2 = st.columns(2)

    with col1:
        genre = st.selectbox("Genre", ["Deep House", "Chill House", "Lounge Music", "Summer Vibes"])
        durasi = st.selectbox("Durasi Video", ["1 Jam", "3 Jam"])
        suasana = st.text_area("Suasana Visual", value="luxury beach villa sunset, infinity pool, ocean view")

    with col2:
        target = st.success("Target: USA")
        mood = st.selectbox("Mood", ["Relaxing", "Luxury", "Sunset", "Focus", "Beach Party"])

    if st.button("🚀 Generate Luxury Music"):
        prompt = f"""
Buatkan paket konten YouTube music target US.

GENRE: {genre}
DURASI: {durasi}
SUASANA: {suasana}
MOOD: {mood}

Output wajib:
1. 10 JUDUL YOUTUBE BAHASA INGGRIS
2. DESKRIPSI YOUTUBE
3. PROMPT GAMBAR COVER 16:9
4. PROMPT VIDEO LOOP 16:9
5. PROMPT VIDEO LOOP 9:16
6. THUMBNAIL TEXT
7. HASHTAG
8. KEYWORD SEO
9. PROMPT SUNO / MUSIC AI

Gaya:
premium, relaxing, luxury villa, sunset, ocean, deep house, US audience.
"""
        hasil = generate_ai(prompt)
        output_box("🌴 Hasil Luxury Music", hasil, "luxury_result")
