"""
Modul Rekomendasi Studi Personal untuk Setiap Karakter Gaya Belajar Mahasiswa.
Menyediakan tips actionable, kekuatan, mitigasi kelemahan, dan rekomendasi tools.
"""

from typing import Dict, Any

STUDENT_PROFILES: Dict[str, Dict[str, Any]] = {
    "Si Paling Ambis": {
        "mascot": "Semut",
        "emoji": "🐜",
        "tagline": "Disiplin, Terstruktur, dan Selalu Satu Langkah di Depan",
        "description": (
            "Kamu memiliki komitmen dan disiplin tinggi dalam belajar. "
            "Rencana belajarmu rapi, selalu evaluasi diri, dan tidak mudah puas dengan hasil standar. "
            "Kamu adalah tipe pembelajar mandiri yang visioner."
        ),
        "strengths": [
            "Manajemen waktu luar biasa dan jarang menunda tugas",
            "Konsisten dalam mencatat progres dan hasil belajar",
            "Mampu belajar secara mandiri dalam durasi panjang tanpa terdistraksi"
        ],
        "challenges": [
            "Rentan mengalami academic burnout jika memaksakan diri tanpa istirahat",
            "Kecenderungan perfeksionisme berlebih yang memicu stres berulang"
        ],
        "study_techniques": [
            {
                "name": "Active Recall & Spaced Repetition",
                "desc": "Uji ingatan secara aktif menggunakan flashcard berkala daripada sekadar membaca ulang catatan."
            },
            {
                "name": "Feynman Technique",
                "desc": "Jelaskan konsep rumit dengan bahasa sesederhana mungkin seolah mengajari anak SD."
            }
        ],
        "recommended_tools": [
            {"name": "Notion", "use": "Manajemen materi & database tugas perkuliahan"},
            {"name": "Anki", "use": "Flashcards berbasis algoritma Spaced Repetition"},
            {"name": "Google Calendar", "use": "Time blocking jadwal harian"}
        ],
        "motto": "Disiplin adalah jembatan antara tujuan dan pencapaian nyata."
    },

    "Si Paling Santuy": {
        "mascot": "Koala",
        "emoji": "🐨",
        "tagline": "Tenang, Fleksibel, dan Minim Beban Pikiran",
        "description": (
            "Kamu adalah pembelajar yang santai namun tetap bertanggung jawab menyelesaikan tugas. "
            "Kamu tidak mudah panik menghadapi deadline dan fleksibel menghadapi perubahan situasi perkuliahan."
        ),
        "strengths": [
            "Tingkat stres rendah dan kemampuan menjaga kesehatan mental yang baik",
            "Fleksibel dan mampu beradaptasi cepat dalam berbagai kondisi belajar",
            "Tidak mudah panik saat menghadapi ujian mendadak"
        ],
        "challenges": [
            "Terkadang terlalu santai hingga menunda pekerjaan penting",
            "Kurangnya catatan terstruktur yang menyulitkan saat revisi akhir"
        ],
        "study_techniques": [
            {
                "name": "Rule of 2 Minutes (Aturan 2 Menit)",
                "desc": "Jika suatu tugas bisa dimulai dalam waktu kurang dari 2 menit, lakukan sekarang juga untuk mencegah penundaan."
            },
            {
                "name": "Micro-Habits Learning",
                "desc": "Belajar sedikit tapi rutin setiap hari (15-20 menit) daripada marathon sekaligus."
            }
        ],
        "recommended_tools": [
            {"name": "Google Keep", "use": "Catatan kilat ide dan to-do list sederhana"},
            {"name": "Forest App", "use": "Gamifikasi fokus belajar dengan menanam pohon virtual"},
            {"name": "Spotify Focus Playlists", "use": "Musik lofi / ambient untuk menjaga mood belajar"}
        ],
        "motto": "Pelan tapi pasti, ketenangan adalah kunci ketahanan jangka panjang."
    },

    "Si Paling SKS": {
        "mascot": "Burung Hantu",
        "emoji": "🦉",
        "tagline": "Pakar Tekanan Tinggi & Penakluk Sistem Kebut Semalam",
        "description": (
            "Adrenalin deadline adalah bahan bakar terbesarmu! Kamu memiliki fokus tajam saat situasi kepepet "
            "dan mampu menyerap informasi dalam waktu singkat di bawah tekanan tinggi."
        ),
        "strengths": [
            "Fokus dan konsentrasi hiper-intensif saat mendekati tenggat waktu",
            "Mental tangguh menghadapi situasi darurat dan tekanan akademis",
            "Kemampuan problem solving cepat dan berpikir pragmatis"
        ],
        "challenges": [
            "Retensi memori jangka panjang cenderung rendah karena materi masuk mendadak",
            "Pola tidur terganggu yang berisiko menurunkan stamina fisik dan kesehatan"
        ],
        "study_techniques": [
            {
                "name": "Teknik Pomodoro Modifikasi (50/10)",
                "desc": "50 menit fokus total tanpa notifikasi gawai, diselingi 10 menit istirahat regang."
            },
            {
                "name": "Eisenhower Matrix (Matriks Kuadran Prioritas)",
                "desc": "Pilah tugas menjadi: Mendesak-Penting, Tidak Mendesak-Penting, agar tidak semua menjadi krisis semalam."
            }
        ],
        "recommended_tools": [
            {"name": "Pomofocus / Marinara Timer", "use": "Timer Pomodoro minimalis di browser"},
            {"name": "Todoist", "use": "Pengingat deadline bertahap sebelum H-1"},
            {"name": "Cold Turkey / Freedom", "use": "Memblokir media sosial saat fase darurat tugas"}
        ],
        "motto": "Tekanan melahirkan berlian, tapi manajemen waktu melahirkan ketenangan."
    },

    "Si Paling Rame-rame": {
        "mascot": "Lumba-Lumba",
        "emoji": "🐬",
        "tagline": "Pembelajar Sosial, Kolaboratif, dan Energik",
        "description": (
            "Kamu menyerap ilmu terbaik saat berinteraksi, berdiskusi, dan bertukar pikiran dengan teman. "
            "Bagimu, ruang belajar adalah ruang diskusi bersama di mana kerja tim melipatgandakan pemahaman."
        ),
        "strengths": [
            "Kemampuan komunikasi, negosiasi, dan kerja sama tim yang sangat baik",
            "Mampu mencairkan suasana belajar kelompok agar tidak membosankan",
            "Mudah memahami materi jika diiringi perdebatan ide dan tanya jawab langsung"
        ],
        "challenges": [
            "Sesi belajar kelompok berisiko berubah menjadi nongkrong atau ngobrol ngalor-ngidul",
            "Kesulitan fokus jika terpaksa harus belajar sendirian dalam ruang hening"
        ],
        "study_techniques": [
            {
                "name": "Peer Teaching / Jigsaw Method",
                "desc": "Bagi materi ke masing-masing anggota kelompok, lalu saling mengajarkan satu sama lain."
            },
            {
                "name": "Virtual Co-Working / Study With Me",
                "desc": "Gunakan sesi Discord atau Google Meet dengan kamera menyala untuk menjaga akuntabilitas belajar bersama."
            }
        ],
        "recommended_tools": [
            {"name": "Discord Study Server", "use": "Ruang belajar suara dan berbagi layar dengan teman"},
            {"name": "Miro / FigJam", "use": "Papan tulis virtual kolaboratif untuk brainstorming bersama"},
            {"name": "Google Docs / Workspace", "use": "Kolaborasi penulisan laporan secara real-time"}
        ],
        "motto": "Jika ingin berjalan cepat berjalanlah sendiri, jika ingin berjalan jauh berjalanlah bersama."
    }
}

