"""
Modul Pohon Keputusan (Binary Decision Tree) untuk Klasifikasi Gaya Belajar Mahasiswa.
Dibuat untuk keperluan representasi struktur data pohon dan penelusuran (traversal).
"""

from typing import Optional, Dict, Any, Tuple, List


class TreeNode:
    """
    Representasi Node pada Binary Tree.
    - Jika bukan daun (internal node), memiliki 'feature' untuk pengujian logika.
    - Jika daun (leaf node), memiliki 'value' yang merupakan hasil klasifikasi.
    """
    def __init__(
        self,
        feature: Optional[str] = None,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None,
        value: Optional[str] = None
    ):
        self.feature = feature  # Pertanyaan / Fitur pemisah
        self.left = left        # Cabang Kiri (Jika kondisi bernilai True / Pilihan A)
        self.right = right      # Cabang Kanan (Jika kondisi bernilai False / Pilihan B)
        self.value = value      # Label hasil klasifikasi (hanya untuk leaf node)

    def is_leaf(self) -> bool:
        """Memeriksa apakah node saat ini merupakan daun (ujung pohon)."""
        return self.value is not None


# Daftar pertanyaan kuis beserta pemetaan opsinya
QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": 1,
        "key": "Suka belajar mandiri",
        "question": "Kamu lebih suka belajar seperti apa?",
        "options": ["Sendiri", "Bareng temen"],
        "true_option": "Sendiri"
    },
    {
        "id": 2,
        "key": "Suka belajar pagi-siang",
        "question": "Waktu belajar paling efektif menurutmu kapan?",
        "options": ["Pagi-Siang", "Malam"],
        "true_option": "Pagi-Siang"
    },
    {
        "id": 3,
        "key": "Langsung dikerjain setelah dikasih",
        "question": "Kalau ada tugas kuliah, kapan kamu mulai mengerjakan?",
        "options": [
            "Langsung dikerjain setelah dikasih",
            "H-1 bahkan tinggal beberapa jam lagi gas terus!"
        ],
        "true_option": "Langsung dikerjain setelah dikasih"
    },
    {
        "id": 4,
        "key": "Suka memakai tools plan belajar",
        "question": "Kamu biasanya pakai tools belajar (Notion, Google Calendar, To-Do List)?",
        "options": [
            "Iya dong, hidupku terjadwal banget",
            "Enggak sih, ngikut alur dan mood aja"
        ],
        "true_option": "Iya dong, hidupku terjadwal banget"
    },
    {
        "id": 5,
        "key": "Evaluasi",
        "question": "Apakah kamu rutin evaluasi diri setelah ujian atau pengumpulan tugas?",
        "options": [
            "Iya aku catat apa yang harus diperbaiki",
            "Nggak remidi aja dah syukur"
        ],
        "true_option": "Iya aku catat apa yang harus diperbaiki"
    }
]


def build_decision_tree() -> TreeNode:
    """
    Membangun struktur Binary Decision Tree 5-level (kedalaman d = 5).
    Struktur mencerminkan 32 kemungkinan cabang jawaban mahasiswa.
    """
    return TreeNode(
        feature="Suka belajar mandiri",  # Level 1
        left=TreeNode(
            feature="Suka belajar pagi-siang",  # Level 2 (Mandiri = True)
            left=TreeNode(
                feature="Langsung dikerjain setelah dikasih",  # Level 3
                left=TreeNode(
                    feature="Suka memakai tools plan belajar",  # Level 4
                    left=TreeNode(
                        feature="Evaluasi",  # Level 5
                        left=TreeNode(value="Si Paling Ambis"),   # AAAAA
                        right=TreeNode(value="Si Paling Ambis")   # AAAAB
                    ),
                    right=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Ambis"),   # AAABA
                        right=TreeNode(value="Si Paling Santuy")  # AAABB
                    )
                ),
                right=TreeNode(
                    feature="Suka memakai tools plan belajar",
                    left=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling SKS"),     # AABAA
                        right=TreeNode(value="Si Paling SKS")     # AABAB
                    ),
                    right=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Santuy"),  # AABBA
                        right=TreeNode(value="Si Paling Santuy")  # AABBB
                    )
                )
            ),
            right=TreeNode(
                feature="Langsung dikerjain setelah dikasih",  # Level 3 (Pagi-Siang = False / Malam)
                left=TreeNode(
                    feature="Suka memakai tools plan belajar",
                    left=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Ambis"),   # ABAAA
                        right=TreeNode(value="Si Paling Ambis")   # ABAAB
                    ),
                    right=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Santuy"),  # ABABA
                        right=TreeNode(value="Si Paling Santuy")  # ABABB
                    )
                ),
                right=TreeNode(
                    feature="Suka memakai tools plan belajar",
                    left=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling SKS"),     # ABBAA
                        right=TreeNode(value="Si Paling SKS")     # ABBAB
                    ),
                    right=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Santuy"),  # ABBBA
                        right=TreeNode(value="Si Paling Rame-rame")# ABBBB
                    )
                )
            )
        ),
        right=TreeNode(
            feature="Suka belajar pagi-siang",  # Level 2 (Mandiri = False / Bareng Teman)
            left=TreeNode(
                feature="Langsung dikerjain setelah dikasih",  # Level 3
                left=TreeNode(
                    feature="Suka memakai tools plan belajar",
                    left=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Rame-rame"),  # BAAAA
                        right=TreeNode(value="Si Paling Rame-rame")  # BAAAB
                    ),
                    right=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Santuy"),     # BAABA
                        right=TreeNode(value="Si Paling SKS")        # BAABB
                    )
                ),
                right=TreeNode(
                    feature="Suka memakai tools plan belajar",
                    left=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling SKS"),        # BABAA
                        right=TreeNode(value="Si Paling Santuy")     # BABAB
                    ),
                    right=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Santuy"),     # BABBA
                        right=TreeNode(value="Si Paling Santuy")     # BABBB
                    )
                )
            ),
            right=TreeNode(
                feature="Langsung dikerjain setelah dikasih",  # Level 3 (Pagi-Siang = False / Malam)
                left=TreeNode(
                    feature="Suka memakai tools plan belajar",
                    left=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Rame-rame"),  # BBAAA
                        right=TreeNode(value="Si Paling Rame-rame")  # BBAAB
                    ),
                    right=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Santuy"),     # BBABA
                        right=TreeNode(value="Si Paling Santuy")     # BBABB
                    )
                ),
                right=TreeNode(
                    feature="Suka memakai tools plan belajar",
                    left=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling SKS"),        # BBBAA
                        right=TreeNode(value="Si Paling SKS")        # BBBAB
                    ),
                    right=TreeNode(
                        feature="Evaluasi",
                        left=TreeNode(value="Si Paling Rame-rame"),  # BBBBA
                        right=TreeNode(value="Si Paling Santuy")     # BBBBB
                    )
                )
            )
        )
    )


# Instansiasi pohon tunggal (Singleton Tree)
STUDENT_DECISION_TREE = build_decision_tree()


def classify_student(
    answers: Dict[str, str],
    tree: TreeNode = STUDENT_DECISION_TREE
) -> Tuple[str, List[Dict[str, Any]]]:
    """
    Melakukan traversal (penelusuran) pada pohon keputusan berdasarkan jawaban user.

    Kompleksitas Waktu: O(d), di mana d adalah kedalaman pohon (5 langkah).
    Kompleksitas Ruang: O(1) iteratif.

    Returns:
        tuple: (tipe_mahasiswa, path_riwayat_traversal)
    """
    # Mapping jawaban ke nilai Boolean (True = Left, False = Right)
    answer_mapping = {
        q["key"]: answers.get(q["key"]) == q["true_option"]
        for q in QUESTIONS
    }

    current_node = tree
    decision_path: List[Dict[str, Any]] = []

    while not current_node.is_leaf():
        feature = current_node.feature
        decision = answer_mapping.get(feature, False)
        direction = "LEFT (Ya/Pilihan 1)" if decision else "RIGHT (Tidak/Pilihan 2)"

        decision_path.append({
            "feature": feature,
            "decision": decision,
            "direction": direction
        })

        if decision:
            current_node = current_node.left
        else:
            current_node = current_node.right

    return current_node.value, decision_path

