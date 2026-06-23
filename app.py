import streamlit as st
import google.generativeai as genai
from datetime import datetime

st.set_page_config(page_title="Content Factory AI V4", page_icon="🚀", layout="wide")

st.markdown("""
<style>
.card {
    background:#1f2937;
    padding:20px;
    border-radius:16px;
    border:1px solid #374151;
    margin-bottom:18px;
}
.big-title {
    font-size:40px;
    font-weight:900;
}
.muted {
    color:#9ca3af;
}
</style>
""", unsafe_allow_html=True)

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

def generate_ai(prompt):
    if not st.session_state.api_key:
        return """
HASIL DEMO CONTENT FACTORY AI

JUDUL:
Contoh Judul Konten AI

HOOK:
Ini adalah contoh hasil demo tanpa API.

NARASI:
Aplikasi tetap bisa dicoba meskipun API belum aktif.

PROMPT VIDEO:
Gunakan gambar referensi utama. Pertahankan wajah, pakaian, warna, bentuk, dan detail tetap sama. Gerakan natural, cinematic, realistis.

NEGATIVE PROMPT:
no face change, no clothes change, no product changes, no blur, no watermark, no deformation

HASHTAG:
#AIContent #VideoAI #ContentFactoryAI
"""

    try:
        genai.configure(api_key=st.session_state.api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        return """
API ERROR - MODE DEMO AKTIF

Gemini API masih error atau quota limit.

Aplikasi tetap berjalan dalam mode demo.
"""

def result_section(title, content, key):
    st.markdown(f"### {title}")
    st.text_area("Klik CTRL+A lalu CTRL+C untuk copy", content, height=280, key=key)
    st.download_button(
        label=f"⬇️ Download {title}",
        data=content,
        file_name=f"{title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain"
    )

st.sidebar.title("🚀 Content Factory AI V4")
menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "🏠 Dashboard",
        "🎬 Film AI",
        "🛍️ Affiliate AI",
        "🕌 Dakwah AI",
        "🌴 Luxury Music AI",
        "⚙️ Settings"
    ]
)

st.markdown("<div class='big-title'>🚀 Content Factory AI V4</div>", unsafe_allow_html=True)
st.markdown("<div class='muted'>AI Content Studio untuk Film, Affiliate, Dakwah, dan Luxury Music.</div>", unsafe_allow_html=True)
st.divider()

if menu == "🏠 Dashboard":
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='card'><h3>🎬 Film AI</h3><p>Storyboard, dialog, prompt video, dan negative prompt karakter.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'><h3>🛍️ Affiliate AI</h3><p>Produk saja atau model + produk dengan negative prompt ketat.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='card'><h3>🕌 Dakwah AI</h3><p>Narasi, judul, thumbnail text, prompt gambar, hashtag.</p></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='card'><h3>🌴 Luxury Music</h3><p>Deep House, Chill, Lounge target US.</p></div>", unsafe_allow_html=True)

elif menu == "⚙️ Settings":
    st.subheader("⚙️ Settings")
    api_key = st.text_input("Gemini API Key", type="password")

    if st.button("💾 Simpan API Key"):
        st.session_state.api_key = api_key
        st.success("API Key berhasil disimpan.")

    st.warning("Jangan tampilkan API Key di screenshot atau dibagikan ke siapa pun.")

elif menu == "🎬 Film AI":
    st.subheader("🎬 Film AI")

    col1, col2 = st.columns(2)

    with col1:
        target = st.selectbox("Target Audience", ["Indonesia", "USA"])
        mesin = st.selectbox("Mesin Video", ["Opal", "Omni Flash", "Gemini"])
        scene = st.selectbox("Jumlah Scene", [5, 10])
        ide = st.text_area("Ide Cerita", placeholder="Contoh: Aceng dan teman-teman membuat film komedi kampung")

    with col2:
        st.markdown("### 📷 Referensi Karakter")
        ref1 = st.file_uploader("Karakter Utama", type=["jpg", "jpeg", "png"])
        ref2 = st.file_uploader("Teman / Lawan Main", type=["jpg", "jpeg", "png"])
        ref3 = st.file_uploader("Karakter Tambahan", type=["jpg", "jpeg", "png"])

        if ref1:
            st.image(ref1, caption="Karakter Utama", width=180)
        if ref2:
            st.image(ref2, caption="Teman / Lawan Main", width=180)
        if ref3:
            st.image(ref3, caption="Karakter Tambahan", width=180)

    if st.button("🚀 Generate Film AI"):
        prompt = f"""
Buatkan paket film pendek AI profesional.

Target audience: {target}
Mesin video: {mesin}
Jumlah scene: {scene}
Ide cerita: {ide}

Output harus dipisah dengan jelas:
1. JUDUL FILM
2. SINOPSIS
3. DAFTAR KARAKTER
4. STORYBOARD {scene} SCENE
5. PROMPT VIDEO PER SCENE UNTUK {mesin}
6. DIALOG PER SCENE
7. NEGATIVE PROMPT SUPER KETAT
8. CATATAN TEKNIS

Aturan:
- gunakan gambar referensi sebagai karakter utama
- wajah harus tetap sama
- pakaian harus tetap sama
- umur harus tetap sama
- bentuk tubuh harus tetap sama
- jangan mengganti identitas karakter
- jangan ada subtitle
- jangan ubah pakaian antar scene
- jangan ubah lokasi kecuali diminta
"""
        hasil = generate_ai(prompt)
        if hasil:
            result_section("🎬 Hasil Film AI", hasil, "film_result")

elif menu == "🛍️ Affiliate AI":
    st.subheader("🛍️ Affiliate AI")

    col1, col2 = st.columns(2)

    with col1:
        mode = st.radio("Mode Affiliate", ["Produk Saja", "Model + Produk"])
        target = st.selectbox("Target Audience", ["Indonesia", "USA"])
        mesin = st.selectbox("Mesin Video", ["Opal", "Omni Flash", "Gemini"])
        produk = st.text_input("Nama Produk", placeholder="Contoh: Tas sekolah anak SD")
        kategori = st.selectbox("Kategori Produk", ["Tas", "Baju", "Sepatu", "Sandal", "Jam", "Aksesoris", "Custom"])

        model_desc = ""
        if mode == "Model + Produk":
            model_desc = st.text_area("Deskripsi Model", placeholder="Contoh: anak perempuan SD umur 8 tahun memakai seragam sekolah")

    with col2:
        st.markdown("### 📷 Foto Produk")
        foto_produk = st.file_uploader("Upload Foto Produk", type=["jpg", "jpeg", "png"])
        if foto_produk:
            st.image(foto_produk, caption="Foto Produk Referensi", width=260)

    if st.button("🚀 Generate Affiliate AI"):
        prompt = f"""
Buatkan konten TikTok Affiliate profesional.

Mode: {mode}
Target audience: {target}
Mesin video: {mesin}
Produk: {produk}
Kategori produk: {kategori}
Deskripsi model: {model_desc}

Output harus dipisah:
1. JUDUL KONTEN
2. HOOK 3 DETIK
3. SCRIPT VIDEO 15-30 DETIK
4. STORYBOARD 5 SCENE
5. PROMPT IMAGE TO VIDEO UNTUK {mesin}
6. CTA KERANJANG KUNING
7. HASHTAG
8. NEGATIVE PROMPT SUPER KETAT

Aturan produk:
- produk harus 100% sama dengan foto referensi
- jangan ubah warna
- jangan ubah bentuk
- jangan ubah logo
- jangan ubah tulisan
- jangan ubah bahan
- jangan ubah ukuran
- jangan tambah aksesoris
- jangan hilangkan detail
- jangan ubah desain
- jangan buat produk blur
- jangan buat produk dobel
- jangan potong produk
"""
        hasil = generate_ai(prompt)
        if hasil:
            result_section("🛍️ Hasil Affiliate AI", hasil, "affiliate_result")

elif menu == "🕌 Dakwah AI":
    st.subheader("🕌 Dakwah AI")

    col1, col2 = st.columns(2)

    with col1:
        target = st.selectbox("Target Audience", ["Indonesia", "USA"])
        tema = st.text_input("Tema Dakwah", placeholder="Contoh: Tawakal dalam Islam")
        durasi = st.selectbox("Durasi", ["60 detik", "3 menit", "10 menit"])

    with col2:
        st.markdown("### 📷 Gambar Referensi")
        gambar_ref = st.file_uploader("Upload Gambar Referensi Opsional", type=["jpg", "jpeg", "png"])
        if gambar_ref:
            st.image(gambar_ref, caption="Gambar Referensi", width=260)

    if st.button("🚀 Generate Dakwah AI"):
        prompt = f"""
Buatkan paket konten dakwah.

Target audience: {target}
Tema: {tema}
Durasi: {durasi}

Output harus dipisah:
1. 10 PILIHAN JUDUL
2. HOOK PEMBUKA
3. NASKAH NARASI
4. THUMBNAIL TEXT
5. PROMPT GAMBAR THUMBNAIL
6. PROMPT VIDEO ISLAMI
7. DESKRIPSI YOUTUBE
8. HASHTAG
9. VOICE OVER SCRIPT

Gaya:
- menyentuh
- sopan
- mudah dipahami
- tidak berlebihan
- bahasa sesuai target audience
"""
        hasil = generate_ai(prompt)
        if hasil:
            result_section("🕌 Hasil Dakwah AI", hasil, "dakwah_result")

elif menu == "🌴 Luxury Music AI":
    st.subheader("🌴 Luxury Music AI")

    col1, col2 = st.columns(2)

    with col1:
        genre = st.selectbox("Genre", ["Deep House", "Chill House", "Lounge Music"])
        durasi = st.selectbox("Durasi Video", ["1 Jam", "3 Jam"])
        suasana = st.text_area("Suasana Visual", placeholder="Contoh: luxury beach villa sunset, infinity pool, ocean view")

    with col2:
        st.markdown("### 🎯 Target")
        st.success("Target default: USA")
        st.info("Cocok untuk channel Deep House / Luxury Villa / Sunset Chill.")

    if st.button("🚀 Generate Luxury Music AI"):
        prompt = f"""
Buatkan paket konten YouTube music target US.

Genre: {genre}
Durasi: {durasi}
Suasana visual: {suasana}

Output harus dipisah:
1. 10 JUDUL YOUTUBE BAHASA INGGRIS
2. DESKRIPSI YOUTUBE
3. PROMPT GAMBAR VILLA LUXURY SUNSET
4. PROMPT VIDEO LOOP 16:9
5. PROMPT VIDEO LOOP 9:16
6. THUMBNAIL TEXT
7. HASHTAG
8. KEYWORD SEO

Gaya:
- premium
- relaxing
- luxury villa
- sunset
- ocean
- deep house
- US audience
"""
        hasil = generate_ai(prompt)
        if hasil:
            result_section("🌴 Hasil Luxury Music AI", hasil, "luxury_result")
