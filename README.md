# Final Project Intern ID/X Partners: Credit Risk Prediction

## Deskripsi
Tujuan dari proyek ini adalah untuk membangun model machine learning yang dapat memprediksi risiko kredit calon peminjam dengan akurat menggunakan dataset yang disediakan oleh perusahaan.

## Dataset
Dataset yang digunakan dalam proyek ini adalah "Data Pinjaman 2007-2014", yang dapat diunduh dari [link ini](https://drive.google.com/file/d/1JVG3_QQx8is4xWfPUrkMxbWev6c3VC-e/view?usp=sharing).
Dataset ini berisi informasi tentang pinjaman yang dikeluarkan antara tahun 2007 dan 2014.  Informasi yang terdapat di dalamnya meliputi jumlah pinjaman, suku bunga, jangka waktu, grade, lama kerja, kepemilikan rumah, pendapatan tahunan, tujuan pinjaman, dan status pinjaman. Dataset ini memiliki sekitar 466.285 baris dan 75 kolom.

**Fitur Utama:**
| Fitur          | Tipe Data    | Deskripsi                                                                                                                               | Contoh Nilai            |
| --------------- | ---------    | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `loan_amnt`    | Numerik     | Jumlah pinjaman yang diajukan.                                                                                                            | 10000                  |
| `int_rate`     | Numerik     | Suku bunga pinjaman.                                                                                                                   | 10.65                   |
| `term`         | Kategorikal | Jangka waktu pinjaman (dalam bulan).                                                                                                       |  36 bulan             |
| `grade`        | Kategorikal | Tingkat risiko pinjaman (A, B, C, D, E, F, G).                                                                                              | B                       |
| `emp_length`   | Kategorikal | Lama kerja peminjam (dalam tahun).                                                                                                      | 10+ tahun              |
| `home_ownership` | Kategorikal | Status kepemilikan rumah peminjam (RENT, OWN, MORTGAGE, OTHER).                                                                              | RENT                    |
| `annual_inc`   | Numerik     | Pendapatan tahunan peminjam.                                                                                                              | 50000                   |
| `purpose`      | Kategorikal | Tujuan pinjaman (debt_consolidation, credit_card, home_improvement, etc.).                                                                 | debt_consolidation      |
| `loan_status`  | Kategorikal | Status pinjaman saat ini (Fully Paid, Charged Off, Current, etc.).                                                                        | Fully Paid              |

## Tujuan Proyek
*   Membangun model prediksi risiko kredit yang akurat menggunakan teknik machine learning.
*   Mengevaluasi kinerja model menggunakan metrik yang sesuai.
*   Mengembangkan visualisasi yang jelas dan informatif untuk mempresentasikan solusi kepada klien secara end to end.


