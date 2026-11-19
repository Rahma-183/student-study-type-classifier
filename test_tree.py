"""
Unit Testing untuk Memvalidasi Struktur Data dan Algoritma Penelusuran Pohon Keputusan.
Dijalankan menggunakan Python Built-in unittest.
"""

import unittest
from tree_model import TreeNode, build_decision_tree, classify_student, STUDENT_DECISION_TREE


class TestStudentDecisionTree(unittest.TestCase):
    """Pengujian Unit untuk Pohon Keputusan Klasifikasi Mahasiswa."""

    def setUp(self):
        """Menyiapkan instance pohon sebelum setiap tes."""
        self.tree = STUDENT_DECISION_TREE

    def test_root_node_initialization(self):
        """Memverifikasi bahwa root node terinisialisasi dengan benar dan bukan merupakan leaf."""
        self.assertIsNotNone(self.tree)
        self.assertFalse(self.tree.is_leaf())
        self.assertEqual(self.tree.feature, "Suka belajar mandiri")
        self.assertIsNotNone(self.tree.left)
        self.assertIsNotNone(self.tree.right)

    def test_classification_si_paling_ambis(self):
        """Menguji kombinasi jawaban AAAAA harus menghasilkan 'Si Paling Ambis'."""
        answers = {
            "Suka belajar mandiri": "Sendiri",
            "Suka belajar pagi-siang": "Pagi-Siang",
            "Langsung dikerjain setelah dikasih": "Langsung dikerjain setelah dikasih",
            "Suka memakai tools plan belajar": "Iya dong, hidupku terjadwal banget",
            "Evaluasi": "Iya aku catat apa yang harus diperbaiki"
        }
        result, path = classify_student(answers, self.tree)
        self.assertEqual(result, "Si Paling Ambis")
        self.assertEqual(len(path), 5)
        # Semua keputusan harus True (ke arah Kiri)
        for step in path:
            self.assertTrue(step["decision"])

    def test_classification_si_paling_santuy(self):
        """Menguji kombinasi jawaban BBBBB harus menghasilkan 'Si Paling Santuy'."""
        answers = {
            "Suka belajar mandiri": "Bareng temen",
            "Suka belajar pagi-siang": "Malam",
            "Langsung dikerjain setelah dikasih": "H-1 bahkan tinggal beberapa jam lagi gas terus!",
            "Suka memakai tools plan belajar": "Enggak sih, ngikut alur dan mood aja",
            "Evaluasi": "Nggak remidi aja dah syukur"
        }
        result, path = classify_student(answers, self.tree)
        self.assertEqual(result, "Si Paling Santuy")
        self.assertEqual(len(path), 5)
        # Semua keputusan harus False (ke arah Kanan)
        for step in path:
            self.assertFalse(step["decision"])

    def test_classification_si_paling_sks(self):
        """Menguji kombinasi jawaban AABAA harus menghasilkan 'Si Paling SKS'."""
        answers = {
            "Suka belajar mandiri": "Sendiri",
            "Suka belajar pagi-siang": "Pagi-Siang",
            "Langsung dikerjain setelah dikasih": "H-1 bahkan tinggal beberapa jam lagi gas terus!",
            "Suka memakai tools plan belajar": "Iya dong, hidupku terjadwal banget",
            "Evaluasi": "Iya aku catat apa yang harus diperbaiki"
        }
        result, path = classify_student(answers, self.tree)
        self.assertEqual(result, "Si Paling SKS")
        self.assertEqual(len(path), 5)

    def test_classification_si_paling_rame_rame(self):
        """Menguji kombinasi jawaban BAAAA harus menghasilkan 'Si Paling Rame-rame'."""
        answers = {
            "Suka belajar mandiri": "Bareng temen",
            "Suka belajar pagi-siang": "Pagi-Siang",
            "Langsung dikerjain setelah dikasih": "Langsung dikerjain setelah dikasih",
            "Suka memakai tools plan belajar": "Iya dong, hidupku terjadwal banget",
            "Evaluasi": "Iya aku catat apa yang harus diperbaiki"
        }
        result, path = classify_student(answers, self.tree)
        self.assertEqual(result, "Si Paling Rame-rame")
        self.assertEqual(len(path), 5)

    def test_tree_depth_and_path_length(self):
        """Memastikan setiap penelusuran selalu berhenti di kedalaman tepat 5 tingkat."""
        test_cases = [
            {"Suka belajar mandiri": "Sendiri", "Suka belajar pagi-siang": "Malam", "Langsung dikerjain setelah dikasih": "Langsung dikerjain setelah dikasih", "Suka memakai tools plan belajar": "Enggak sih, ngikut alur dan mood aja", "Evaluasi": "Iya aku catat apa yang harus diperbaiki"},
            {"Suka belajar mandiri": "Bareng temen", "Suka belajar pagi-siang": "Malam", "Langsung dikerjain setelah dikasih": "H-1 bahkan tinggal beberapa jam lagi gas terus!", "Suka memakai tools plan belajar": "Iya dong, hidupku terjadwal banget", "Evaluasi": "Nggak remidi aja dah syukur"}
        ]
        valid_labels = {"Si Paling Ambis", "Si Paling Santuy", "Si Paling SKS", "Si Paling Rame-rame"}
        for case in test_cases:
            result, path = classify_student(case, self.tree)
            self.assertEqual(len(path), 5)
            self.assertIn(result, valid_labels)


if __name__ == "__main__":
    unittest.main()

