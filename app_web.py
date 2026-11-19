"""
Aplikasi Web Interaktif: Klasifikasi Tipe Mahasiswa Berdasarkan Kebiasaan Belajar.
Dibangun menggunakan Streamlit dan modul struktur data Binary Decision Tree.
"""

import streamlit as st
from tree_model import QUESTIONS, classify_student
from recommendations import STUDENT_PROFILES

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Student Study Type Classifier",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS: Futuristic Deep-Space Violet & Cyber-Glow Theme
st.markdown("""
<style>
    /* Latar belakang utama dengan ambient cyber-glow */
    .stApp {
        background:
            radial-gradient(circle at 18% 15%, rgba(124, 58, 237, 0.28) 0%, transparent 45%),
            radial-gradient(circle at 85% 25%, rgba(217, 70, 239, 0.22) 0%, transparent 42%),
            radial-gradient(circle at 50% 88%, rgba(56, 189, 248, 0.15) 0%, transparent 50%),
            linear-gradient(165deg, #090617 0%, #140f36 52%, #1d1142 100%);
        color: #f8fafc;
    }

    /* Sidebar dark glass */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0e0a24 0%, #191240 100%);
        border-right: 1px solid rgba(168, 85, 247, 0.25);
    }

    /* Hero Header */
    .hero-container {
        text-align: center;
        padding: 1.8rem 1.5rem;
        border-radius: 20px;
        background: rgba(26, 20, 64, 0.55);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(168, 85, 247, 0.32);
        box-shadow: 0 10px 35px rgba(8, 5, 25, 0.55);
        margin-bottom: 1.8rem;
    }
    .hero-badge {
        display: inline-block;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        background: linear-gradient(90deg, rgba(124, 58, 237, 0.35), rgba(217, 70, 239, 0.35));
        border: 1px solid rgba(217, 70, 239, 0.45);
        color: #f0abfc;
        margin-bottom: 0.8rem;
    }
    .main-title {
        font-size: 2.1rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ffffff 0%, #e9d5ff 55%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.2rem 0 0.5rem 0;
    }
    .sub-title {
        color: #cbd5e1;
        font-size: 1rem;
        margin: 0;
    }

    /* Glassmorphic Form Container */
    div[data-testid="stForm"] {
        background: rgba(22, 17, 56, 0.68);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(168, 85, 247, 0.32);
        border-radius: 18px;
        padding: 1.6rem 1.5rem;
        box-shadow: 0 12px 36px rgba(7, 4, 22, 0.6);
    }

    /* Radio option cards */
    div[role="radiogroup"] > label {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(168, 85, 247, 0.22);
        border-radius: 12px;
        padding: 10px 14px;
        margin-bottom: 6px;
        transition: all 0.2s ease;
    }
    div[role="radiogroup"] > label:hover {
        background: rgba(168, 85, 247, 0.14);
        border-color: rgba(217, 70, 239, 0.55);
    }

    /* Primary Gradient Buttons */
    div.stFormSubmitButton > button,
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #7c3aed 0%, #d946ef 100%);
        color: #ffffff;
        border: none;
        border-radius: 12px;
        font-weight: 700;
        padding: 0.65rem 1.4rem;
        box-shadow: 0 4px 20px rgba(168, 85, 247, 0.45);
        transition: all 0.25s ease;
    }
    div.stFormSubmitButton > button:hover,
    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
        box-shadow: 0 6px 28px rgba(217, 70, 239, 0.65);
        transform: translateY(-1px);
        color: #ffffff;
    }

    /* Kartu Hasil Utama */
    .result-badge {
        padding: 1.8rem 1.5rem;
        border-radius: 20px;
        background: linear-gradient(145deg, rgba(46, 28, 99, 0.82), rgba(22, 17, 56, 0.88));
        border: 1px solid rgba(217, 70, 239, 0.45);
        box-shadow: 0 0 35px rgba(168, 85, 247, 0.25);
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .result-title {
        margin: 0.4rem 0;
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ffffff, #f0abfc, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .result-tagline {
        font-weight: 600;
        color: #38bdf8;
        font-size: 1.05rem;
        margin: 0;
    }

    /* Glassmorphic Info Cards */
    .glass-card {
        padding: 1.25rem;
        border-radius: 14px;
        background: rgba(26, 20, 64, 0.62);
        border: 1px solid rgba(168, 85, 247, 0.28);
        margin-bottom: 1rem;
    }

    /* Quote Box */
    .quote-box {
        font-style: italic;
        padding: 1.1rem 1.25rem;
        background: linear-gradient(90deg, rgba(124, 58, 237, 0.22), rgba(56, 189, 248, 0.12));
        border-left: 4px solid #d946ef;
        border-radius: 10px;
        color: #e2e8f0;
        margin-top: 1.5rem;
    }

    /* Question divider */
    .q-header {
        color: #c084fc;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Hero Header
st.markdown("""
<div class="hero-container">
    <span class="hero-badge">Binary Decision Tree • Python</span>
    <h1 class="main-title">🎓 Student Study Type Classifier</h1>
    <p class="sub-title">Identifikasi gaya dan kebiasaan belajarmu melalui penelusuran struktur data <b>Decision Tree</b></p>
</div>
""", unsafe_allow_html=True)

# Sidebar Informasi Proyek
with st.sidebar:
    st.header("📌 Tentang Proyek")
    st.write(
        "Aplikasi ini mengimplementasikan struktur data **Binary Decision Tree** "
        "untuk mengklasifikasikan gaya belajar mahasiswa berdasarkan 5 dimensi kebiasaan."
    )
    st.markdown("---")
    st.markdown("**Struktur Data:** Binary Tree")
    st.markdown("**Kompleksitas Traversal:** $O(d)$ dengan $d = 5$")
    st.markdown("**Kapasitas Daun:** $2^5 = 32$ kombinasi")
    st.markdown("---")
    st.caption("Mata Kuliah: Struktur Data dan Algoritma")

# Inisialisasi session state
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "result_type" not in st.session_state:
    st.session_state.result_type = None
if "decision_path" not in st.session_state:
    st.session_state.decision_path = []

# Tampilan Form Kuis
if not st.session_state.quiz_submitted:
    st.info("Jawab 5 pertanyaan singkat di bawah ini sesuai kebiasaan belajarmu yang sebenarnya:")

    with st.form(key="quiz_form"):
        user_answers = {}
        for idx, q in enumerate(QUESTIONS, 1):
            st.markdown(f"<div class='q-header'>Pertanyaan {idx} dari {len(QUESTIONS)}</div>", unsafe_allow_html=True)
            answer = st.radio(
                label=q["question"],
                options=q["options"],
                key=f"q_{idx}",
                index=0
            )
            user_answers[q["key"]] = answer
            if idx < len(QUESTIONS):
                st.markdown("<hr style='border-color: rgba(168,85,247,0.18); margin: 0.8rem 0;'>", unsafe_allow_html=True)

        st.write("")
        submitted = st.form_submit_button("🔍 Analisis Gaya Belajarku", use_container_width=True, type="primary")

        if submitted:
            result, path = classify_student(user_answers)
            st.session_state.quiz_submitted = True
            st.session_state.result_type = result
            st.session_state.decision_path = path
            st.rerun()

else:
    # Tampilan Hasil Klasifikasi
    result_type = st.session_state.result_type
    profile = STUDENT_PROFILES.get(result_type, {})

    st.balloons()

    # Kartu Hasil Utama
    st.markdown(f"""
    <div class='result-badge'>
        <div style='font-size: 3.4rem; line-height: 1.1;'>{profile.get('emoji', '🎓')}</div>
        <div class='result-title'>{result_type}</div>
        <p class='result-tagline'>{profile.get('tagline', '')}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='glass-card'>
        <strong style='color: #e9d5ff;'>Tentang Karakter Ini:</strong><br>
        <span style='color: #e2e8f0;'>{profile.get('description', '')}</span>
    </div>
    """, unsafe_allow_html=True)

    # Tab Navigasi Hasil
    tab1, tab2, tab3 = st.tabs(["💡 Rekomendasi Belajar", "🌲 Analisis Decision Tree", "🔄 Coba Lagi"])

    # Tab 1: Rekomendasi Studi & Tools
    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("💪 Kekuatan Utama")
            for strength in profile.get("strengths", []):
                st.markdown(f"- ✅ {strength}")

        with col2:
            st.subheader("⚠️ Titik Perhatian")
            for challenge in profile.get("challenges", []):
                st.markdown(f"- ⚠️ {challenge}")

        st.markdown("---")
        st.subheader("📚 Teknik Belajar yang Direkomendasikan")
        for tech in profile.get("study_techniques", []):
            st.markdown(f"**{tech['name']}**")
            st.caption(tech["desc"])

        st.markdown("---")
        st.subheader("🛠️ Tools Produktivitas Pilihan")
        for tool in profile.get("recommended_tools", []):
            st.markdown(f"- **{tool['name']}**: {tool['use']}")

        st.markdown(f"""
        <div class='quote-box'>
            "{profile.get('motto', '')}"
        </div>
        """, unsafe_allow_html=True)

    # Tab 2: Penjelasan Alur Traversal Decision Tree
    with tab2:
        st.subheader("🌲 Logika Penelusuran Pohon (Tree Traversal)")
        st.write(
            "Berikut adalah bagaimana algoritma menelusuri simpul demi simpul "
            "dari akar (*root node*) menuju daun (*leaf node*):"
        )

        for step_idx, step in enumerate(st.session_state.decision_path, 1):
            is_true = step["decision"]
            icon = "🟣" if is_true else "🔵"
            with st.expander(f"Langkah {step_idx}: {step['feature']}", expanded=True):
                st.write(f"{icon} **Arah Cabang:** `{step['direction']}`")
                st.caption(f"Evaluasi kondisi cabang: **{'Benar (Kiri)' if is_true else 'Salah (Kanan)'}**")

        st.success(f"🎯 **Hasil Akhir Capaian Daun (Leaf Node):** `{result_type}`")

        st.markdown("""
        > **Catatan Struktur Data**:
        > Pohon ini merupakan *Full Binary Tree* dengan kedalaman $d = 5$.
        > Karena setiap pertanyaan memiliki 2 cabang (kiri/kanan), algoritma hanya membutuhkan
        > tepat **5 kali perbandingan** untuk menentukan kelas, menghasilkan kompleksitas waktu $\\mathcal{O}(d)$.
        """)

    # Tab 3: Reset Kuis
    with tab3:
        st.write("Ingin mengulang kuis dengan variasi jawaban lain?")
        if st.button("🔄 Reset dan Ulangi Kuis", type="primary", use_container_width=True):
            st.session_state.quiz_submitted = False
            st.session_state.result_type = None
            st.session_state.decision_path = []
            st.rerun()
