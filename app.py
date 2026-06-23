
import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Content Factory AI",
    page_icon="🚀",
    layout="wide"
)

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

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

def ai_generate(prompt):
    if not st.session_state.api_key:
        st.error("Masukkan Gemini API Key dulu di menu Settings.")
        return ""

    genai.configure(api_key=st.session_state.api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

st.title("🚀 Content Factory AI")

if menu == "🏠 Dashboard":
    st.subheader("Selamat datang kang 👋")
    st.write("Aplikasi untuk membuat ide konten, naskah, prompt gambar, prompt video, dan hashtag.")
    st.info("Pilih menu di sidebar untuk mulai membuat konten.")

elif menu == "⚙️ Settings":
    st.subheader("⚙️ Settings")
    api_key = st.text_input("Masukkan Gemini API Key", type="password")
    if st.button("Simpan API Key"):
        st.session_state.api_key = api_key
        st.success("API Key berhasil disimpan.")

elif menu == "🎬 Film AI":
    st.subheader("🎬 Film Pendek AI")

    target = st.selectbox("Target Audience", ["Indonesia", "USA"])
    mesin = st.selectbox("Mesin Video", ["Opal", "Omni Flash", "Gemini"])
    ide = st.text_area("Ide Cerita", placeholder="Contoh: Amoy ditipu Ruslan soal gorengan")
    scene = st.selectbox("Jumlah Scene", [5, 10])

    if st.button("Generate Film AI"):
        prompt = f"""
Buatkan konsep film pendek AI.

Target audience: {target}
Mesin video: {mesin}
Ide cerita: {ide}
Jumlah scene: {scene}

Output wajib:
1. Judul
2. Sinopsis singkat
3. Storyboard per scene
4. Prompt video untuk setiap scene
5. Dialog bahasa sesuai target audience
6. Negative prompt agar karakter, wajah, pakaian, dan lokasi tetap konsisten

Gunakan format rapi dan mudah dicopy.
"""
        hasil = ai_generate(prompt)
        st.markdown(hasil)

elif menu == "🛍️ Affiliate AI":
    st.subheader("🛍️ Affiliate AI")

    mode = st.radio("Pilih Mode", ["Produk Saja", "Model + Produk"])
    target = st.selectbox("Target Audience", ["Indonesia", "USA"])
    produk = st.text_input("Nama Produk", placeholder="Contoh: Tas sekolah anak SD")

    if mode == "Model + Produk":
        model_desc = st.text_area("Deskripsi Model", placeholder="Contoh: Anak perempuan SD umur 8 tahun memakai seragam sekolah")
    else:
        model_desc = ""

    if st.button("Generate Affiliate AI"):
        prompt = f"""
Buatkan konten TikTok Affiliate.

Mode: {mode}
Target audience: {target}
Produk: {produk}
Deskripsi model: {model_desc}

Output wajib:
1. Hook 3 detik
2. Script video pendek
3. Storyboard 5 scene
4. Prompt image-to-video
5. CTA keranjang kuning
6. Hashtag
7. Negative prompt super ketat agar produk tidak berubah

Negative prompt harus melarang:
- perubahan warna produk
- perubahan bentuk produk
- perubahan logo
- perubahan tulisan
- perubahan bahan
- perubahan ukuran
- tambahan aksesoris
- detail produk hilang
- produk berubah desain

Gunakan format rapi dan siap copy.
"""
        hasil = ai_generate(prompt)
        st.markdown(hasil)

elif menu == "🕌 Dakwah AI":
    st.subheader("🕌 Dakwah AI")

    target = st.selectbox("Target Audience", ["Indonesia", "USA"])
    tema = st.text_input("Tema Dakwah", placeholder="Contoh: Sabar dalam menghadapi ujian")
    durasi = st.selectbox("Durasi", ["60 detik", "3 menit", "10 menit"])

    if st.button("Generate Dakwah AI"):
        prompt = f"""
Buatkan konten dakwah.

Target audience: {target}
Tema: {tema}
Durasi: {durasi}

Output wajib:
1. Judul YouTube
2. Naskah narasi
3. Thumbnail text
4. Prompt gambar Islami
5. Prompt video Islami
6. Deskripsi YouTube
7. Hashtag

Bahasa menyesuaikan target audience.
Gunakan gaya menyentuh, sopan, dan mudah dipahami.
"""
        hasil = ai_generate(prompt)
        st.markdown(hasil)

elif menu == "🌴 Luxury Music AI":
    st.subheader("🌴 Luxury Music AI")

    genre = st.selectbox("Genre", ["Deep House", "Chill House", "Lounge Music"])
    durasi = st.selectbox("Durasi Video", ["1 Jam", "3 Jam"])
    suasana = st.text_area("Suasana Visual", placeholder="Contoh: luxury beach villa sunset, infinity pool, ocean view")

    if st.button("Generate Luxury Music AI"):
        prompt = f"""
Buatkan paket konten YouTube music target US.

Genre: {genre}
Durasi: {durasi}
Suasana visual: {suasana}

Output wajib:
1. Judul YouTube bahasa Inggris
2. Deskripsi YouTube bahasa Inggris
3. Prompt gambar villa luxury sunset
4. Prompt video loop 9:16 dan 16:9
5. Thumbnail text
6. Hashtag
7. Keyword SEO

Gaya konten: premium, relaxing, luxury villa, sunset, deep house, US audience.
"""
        hasil = ai_generate(prompt)
        st.markdown(hasil)
