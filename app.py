import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Content Factory AI",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.card {
    background: #1f2937;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #374151;
    margin-bottom: 18px;
}
.big-title {
    font-size: 38px;
    font-weight: 800;
}
.small-muted {
    color: #9ca3af;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

def ai_generate(prompt):
    if not st.session_state.api_key:
        st.error("Masukkan Gemini API Key dulu di menu Settings.")
        return ""

    try:
        genai.configure(api_key=st.session_state.api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        st.error("Gagal generate. Kemungkinan quota API limit atau API key bermasalah.")
        return ""

def result_card(title, content):
    st.markdown(f"<div class='card'><h3>{title}</h3></div>", unsafe_allow_html=True)
    st.text_area(title, content, height=250)
    st.code(content, language="text")

st.sidebar.title("🚀 Content Factory AI")
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

st.markdown("<div class='big-title'>🚀 Content Factory AI</div>", unsafe_allow_html=True)
st.markdown("<div class='small-muted'>AI Content Studio untuk Film, Affiliate, Dakwah, dan Luxury Music.</div>", unsafe_allow_html=True)
st.divider()

if menu == "🏠 Dashboard":
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='card'><h3>🎬 Film AI</h3><p>Buat storyboard, dialog, dan prompt video.</p></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h3>🛍️ Affiliate AI</h3><p>Prompt produk, model, hook, CTA, dan negative prompt.</p></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><h3>🕌 Dakwah AI</h3><p>Narasi dakwah, judul, thumbnail, dan prompt visual.</p></div>", unsafe_allow_html=True)

    with col4:
        st.markdown("<div class='card'><h3>🌴 Luxury Music</h3><p>Konten Deep House target US.</p></div>", unsafe_allow_html=True)

elif menu == "⚙️ Settings":
    st.subheader("⚙️ Settings")
    api_key = st.text_input("Masukkan Gemini API Key", type="password")

    if st.button("💾 Simpan API Key"):
        st.session_state.api_key = api_key
        st.success("API Key berhasil disimpan.")

    st.info("Jangan bagikan API Key ke orang lain.")

elif menu == "🎬 Film AI":
    st.subheader("🎬 Film AI - Referensi Karakter")

    col1, col2 = st.columns([1, 1])

    with col1:
        target = st.selectbox("Target Audience", ["Indonesia", "USA"])
        mesin = st.selectbox("Mesin Video", ["Opal", "Omni Flash", "Gemini"])
        jumlah_scene = st.selectbox("Jumlah Scene", [5, 10])
        ide = st.text_area("Ide Cerita", placeholder="Contoh: Aceng dan teman-teman membuat film komedi kampung")

    with col2:
        st.markdown("### 📷 Gambar Referensi Karakter")
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
Jumlah scene: {jumlah_scene}
Ide cerita: {ide}

User akan memakai gambar referensi karakter sendiri.

Output WAJIB:
1. Judul film
2. Sinopsis
3. Daftar karakter
4. Storyboard {jumlah_scene} scene
5. Prompt video per scene untuk {mesin}
6. Dialog per scene
7. Negative prompt super ketat

Aturan prompt:
- gunakan gambar referensi sebagai karakter utama
- wajah harus tetap sama
- pakaian harus tetap sama
- umur harus tetap sama
- bentuk tubuh harus tetap sama
- jangan mengganti identitas karakter
- jangan mengubah latar secara berlebihan
- jangan ada subtitle di video

Formatkan dengan heading yang rapi.
"""
        hasil = ai_generate(prompt)
        result_card("🎬 Hasil Film AI", hasil)

elif menu == "🛍️ Affiliate AI":
    st.subheader("🛍️ Affiliate AI")

    col1, col2 = st.columns([1, 1])

    with col1:
        mode = st.radio("Mode", ["Produk Saja", "Model + Produk"])
        target = st.selectbox("Target Audience", ["Indonesia", "USA"])
        mesin = st.selectbox("Mesin Video", ["Opal", "Omni Flash", "Gemini"])
        produk = st.text_input("Nama Produk", placeholder="Contoh: Tas sekolah anak SD")
        kategori = st.selectbox("Kategori Produk", ["Tas", "Baju", "Sepatu", "Sandal", "Jam", "Aksesoris", "Custom"])

        model_desc = ""
        if mode == "Model + Produk":
            model_desc = st.text_area("Deskripsi Model", placeholder="Contoh: anak perempuan SD umur 8 tahun memakai seragam sekolah")

    with col2:
        st.markdown("### 📷 Foto Produk Referensi")
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
Kategori: {kategori}
Deskripsi model: {model_desc}

User akan upload foto produk sebagai referensi utama.
Produk harus 100% sama seperti foto referensi.

Output WAJIB:
1. Judul konten
2. Hook 3 detik
3. Script video 15-30 detik
4. Storyboard 5 scene
5. Prompt image-to-video untuk {mesin}
6. CTA keranjang kuning
7. Hashtag
8. Negative prompt super ketat

Negative prompt wajib melarang:
- perubahan warna produk
- perubahan bentuk produk
- perubahan logo
- perubahan tulisan
- perubahan bahan
- perubahan ukuran
- tambahan aksesoris
- detail produk hilang
- produk berubah desain
- produk menjadi blur
- produk menjadi model lain
- produk terpotong
- produk dobel
- produk melayang

Formatkan dengan heading yang rapi.
"""
        hasil = ai_generate(prompt)
        result_card("🛍️ Hasil Affiliate AI", hasil)

elif menu == "🕌 Dakwah AI":
    st.subheader("🕌 Dakwah AI")

    col1, col2 = st.columns([1, 1])

    with col1:
        target = st.selectbox("Target Audience", ["Indonesia", "USA"])
        tema = st.text_input("Tema Dakwah", placeholder="Contoh: Tawakal dalam Islam")
        durasi = st.selectbox("Durasi", ["60 detik", "3 menit", "10 menit"])

    with col2:
        st.markdown("### 📷 Gambar Referensi Opsional")
        gambar_ref = st.file_uploader("Upload Gambar Referensi", type=["jpg", "jpeg", "png"])
        if gambar_ref:
            st.image(gambar_ref, caption="Gambar Referensi", width=260)

    if st.button("🚀 Generate Dakwah AI"):
        prompt = f"""
Buatkan paket konten dakwah.

Target audience: {target}
Tema: {tema}
Durasi: {durasi}

Output WAJIB:
1. 5 pilihan judul
2. Hook pembuka
3. Naskah narasi lengkap
4. Thumbnail text
5. Prompt gambar thumbnail
6. Prompt video islami
7. Deskripsi YouTube
8. Hashtag
9. Voice over script

Bahasa menyesuaikan target audience.
Gaya menyentuh, sopan, mudah dipahami, dan tidak berlebihan.
Formatkan dengan heading rapi.
"""
        hasil = ai_generate(prompt)
        result_card("🕌 Hasil Dakwah AI", hasil)

elif menu == "🌴 Luxury Music AI":
    st.subheader("🌴 Luxury Music AI")

    col1, col2 = st.columns([1, 1])

    with col1:
        genre = st.selectbox("Genre", ["Deep House", "Chill House", "Lounge Music"])
        durasi = st.selectbox("Durasi Video", ["1 Jam", "3 Jam"])
        suasana = st.text_area("Suasana Visual", placeholder="Contoh: luxury beach villa sunset, infinity pool, ocean view")

    with col2:
        st.markdown("### 🎯 Target")
        st.success("Target default: 🇺🇸 United States")
        st.info("Cocok untuk channel Deep House / Luxury Villa / Sunset Chill.")

    if st.button("🚀 Generate Luxury Music AI"):
        prompt = f"""
Buatkan paket konten YouTube music target US.

Genre: {genre}
Durasi: {durasi}
Suasana visual: {suasana}

Output WAJIB:
1. 10 judul YouTube bahasa Inggris
2. Deskripsi YouTube bahasa Inggris
3. Prompt gambar villa luxury sunset
4. Prompt video loop 16:9
5. Prompt video loop 9:16
6. Thumbnail text
7. Hashtag
8. Keyword SEO

Gaya: premium, relaxing, luxury villa, sunset, ocean, deep house, US audience.
Formatkan dengan heading rapi.
"""
        hasil = ai_generate(prompt)
        result_card("🌴 Hasil Luxury Music AI", hasil)
