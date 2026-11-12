# Pre-registrations

The decision rules below were written into the project plan before the corresponding experiments were run.
They are reproduced verbatim from that plan, in the original Indonesian, with only approval notes removed.
The dates in the headings are the dates of writing. They were not deposited with a third-party registry at that time,
so the first public timestamp of this file is the commit that added it.

| Block | Covers |
|---|---|
| 2026-11-03, hypotheses H1–H3 | Pilot study on G1 (step-size coalitions, in-model removal, MambaLRP) |
| 2026-11-03, benchmark v2 protocol | Tasks, models, 14 methods, metrics, statistics of the main benchmark |
| 2026-11-04, v2.1 | Masker-dependence replication on held-out datasets (M1–M3) |
| 2026-11-08, v2.2 | Kernel SHAP budget and longer horizons |
| 2026-11-11, Option A | Replication on the official S-Mamba and TimeMachine code (HA1–HA3) |

### 2026-11-03 — Pra-registrasi uji hipotesis berikutnya (ditulis sebelum eksperimen dijalankan)
**Pertanyaan riset XAI:** apakah informasi internal Mamba menghasilkan penjelasan forecasting yang lebih tepat dan lebih faithful daripada metode model-agnostic? Informasi internal bisa masuk lewat tiga jalur:
- **H1 Koalisi** (siapa pemainnya): Δ atau hidden attention menentukan segmen. Status: lemah.
- **H2 Penghapusan** (bagaimana pemain dihapus): Δ = 0 (state melompati langkah yang dihapus) ditambah masked training, analog SHAPformer untuk Mamba.
- **H3 Propagasi** (bagaimana relevansi mengalir): MambaLRP.

Ketiganya dinilai dengan GT sintetis yang sama, sehingga apa pun hasilnya tetap mengisi benchmark (a).

**Kriteria (tidak diubah setelah hasil keluar):**
- **H1, Exp A** (head last, seed 1–2 ditambah seed 0 = 120 window):
  - *Terbukti bersyarat* bila AP Δ-mass − Uniform > 0 di M=4 **dan** M=8, Wilcoxon berpasangan p < 0,05 atas 120 window, dengan tanda yang sama pada rata-rata tiap seed.
  - *Terbukti kuat* (internal model > statistik data) bila Δ-mass juga > MMD dengan kriteria yang sama.
  - Bila gagal: H1 ditutup dan dilaporkan sebagai temuan negatif. Tidak ada varian segmentasi baru.
- **H2, Exp B** (head flatten konfigurasi F1):
  - *Pelatihan:* 50% sampel tanpa masking. Sisanya q ~ U(0,1), dan tiap segmen waktu dihapus dengan peluang 1 − q (M acak dari {4, 8, 16}), sehingga semua ukuran koalisi terlihat saat training.
  - *Model:* **F-skip** = token terhapus diganti mask token yang dipelajari, ditambah Δ = 0 (khusus Mamba). **F-token** = hanya mask token (pembanding generik ala Covert dkk. / SHAPformer).
  - *Evaluasi:* Shapley eksak atas 8 segmen waktu (256 koalisi), AP level waktu, 40 window.
  - *Gerbang seed 0:* AP(F-skip) − max(AP F1-mean, AP F1-interp) ≥ 0,03. Bila tidak, H2 ditutup tanpa seed tambahan.
  - *Terbukti* bila dengan 3 seed (120 window) selisihnya ≥ 0,05 dengan Wilcoxon p < 0,05 **dan** MSE test F-skip ≤ 1,05 × F1.
  - *Khusus Mamba* hanya bila F-skip juga > F-token dengan kriteria yang sama. Bila tidak, dilaporkan sebagai manfaat masked training yang generik.
- **H3, Exp C** (MambaLRP pada model yang sudah ada: flatten seed 0–2, last seed 0–2):
  - *Terbukti* bila AP MambaLRP > IG dengan Wilcoxon p < 0,05 (window digabung per jenis head) **dan** deletion AOPC tidak lebih buruk.
  - Bila gagal: dilaporkan sebagai temuan benchmark (keunggulan di NLP/vision tidak menular ke forecasting).

**Aturan umum:** hipotesis yang gagal ditutup, dan tidak diselamatkan dengan varian baru kecuali ada bukti independen (literatur, atau bug yang terdiagnosis).


### 2026-11-03 — Protokol benchmark v2 (B8 = pilihan A; ditulis sebelum eksperimen)

**Klaim paper yang dituju:** benchmark XAI untuk forecaster Mamba. Pertanyaannya: apakah informasi internal Mamba memberi penjelasan yang lebih baik, dan faktor apa yang benar-benar menentukan kualitas penjelasan? Hasil v1 (tiga jalur ditutup) menjadi hipotesis yang diuji ulang secara lebih luas, bukan klaim yang dipertahankan.

**Pertanyaan riset**
- **RQ1:** Apakah XAI khusus Mamba (MambaLRP; segmen Δ untuk model yang men-scan waktu) lebih baik daripada metode umum (IG, Grad×Input, SHAP segmen, GS-SHAP resmi), lintas arsitektur dan data?
- **RQ2:** Seberapa besar peringkat metode bergantung pada masker evaluasi (temuan 2–3)?
- **RQ3:** Apakah *sumbu scan* Mamba mengubah jawaban RQ1? Sumbunya bisa waktu, patch, variabel, atau dimensi embedding.
- **RQ4:** Resolusi pemain vs estimator (temuan 1).

**Fakta struktural** (dari kode resmi, dicek 2026-11-03): S-Mamba men-scan *antar-variabel*. TimeMachine men-scan *antar-channel* (mode mixing) atau *dimensi embedding* (mode CI). Keduanya tidak men-scan langkah waktu, sehingga XAI berbasis Δ-waktu tidak terdefinisi untuk mereka. MambaLRP tetap berlaku untuk semua.

**Model** (semua memakai `PurePyTorchMamba` yang sama, satu protokol training v1)

| Kode | Model | Sumbu scan | Sumber |
|---|---|---|---|
| M-T | PlainMamba (head flatten) | langkah waktu | `src/models/plain_mamba.py` (v1) |
| M-V | S-Mamba (bidirectional) | variabel | implementasi ulang dari paper dan kode resmi (repo tanpa lisensi; kode tidak disalin) |
| M-E | TimeMachine, mode channel-mixing (`ch_ind=0`) | channel (satu arah) | port kode resmi (Apache-2.0, atribusi dicantumkan) |
| C-V | iTransformer | variabel (attention) | kembaran non-Mamba dari S-Mamba, untuk menguji apakah suatu temuan khas Mamba |

**Implementasi:** semua di `src/models/zoo.py` (test `tests/test_zoo.py`).
- **Konservasi MambaLRP** (Σ R = f(x) tanpa bias) lulus untuk ketiga model Mamba.
- **iTransformer** terbukti ekuivarian terhadap permutasi variabel. S-Mamba tidak, karena urutan scan berpengaruh.
- **Deviasi** dari konfigurasi resmi, berlaku sama untuk semua model: d_state 16, normalisasi instance dimatikan pada data sintetis yang stasioner.
- **Urutan channel:** target diletakkan di channel *terakhir*, karena TimeMachine men-scan channel satu arah.

**Perubahan protokol sebelum ada hasil (2026-11-03):** M-P (PatchMamba channel-independent) dikeluarkan.
- **Alasan:** model CI tidak dapat melihat channel pemicu, sedangkan semua task GT menuntut informasi lintas channel, sehingga model ini pasti gagal gerbang kualitas.
- **Kenapa tidak diganti varian patch channel-mixing:** varian itu bukan model yang dipublikasikan.

HyMamba-X masuk setelah B2/B3 diputuskan (opsional untuk benchmark).

**Data dengan GT**

| Kode | Data | Jenis GT | Catatan |
|---|---|---|---|
| G1 | Generator kita (lag × regime, event, distraktor) | sel kausal biner | v1 |
| G2 | Setting A/B/C GroupSegment-SHAP (`synthetic_recovery_experiment.py` resmi) | blok grup × segmen biner | Proses X sama persis dengan aslinya. Label ±1 dijadikan target regresi, karena benchmark ini forecasting. Adaptasi ini dilaporkan |
| G3 | Data sintetis SHAPformer (file resmi `data.zip`, KIT) | nilai SHAP per fitur per langkah ramalan (kontinu) | Memerlukan kovariat masa depan. Format: jendela masa lalu + masa depan, beban masa depan dinolkan |

**Data publik (fase 2, faithfulness saja):** ETTh1 dan Weather.

**Metode XAI:**
- **Umum:** IG (baseline 0 = mean), Grad×Input, SHAP segmen seragam (exact/Kernel, M = 4/8/16), SHAP segmen MMD, GS-SHAP resmi (`external/GroupSegment-SHAP`, commit `8ed7e2a`), acak.
- **Khusus Mamba:** MambaLRP (semua M-*), segmen Δ-mass (M-T dan M-P saja).

**Metrik:**
- **G1/G2:** AP, P@k, mass-in-GT. G2 juga memakai IoU pemain dan top-1 hit, seperti paper GS-SHAP.
- **G3:** korelasi Spearman/Pearson antara atribusi per fitur dan GT, serta AP fitur relevan vs noise.
- **Semua data:** deletion/insertion AOPC dengan dua masker (mean, interp), sanity parameter-randomization, dan jumlah evaluasi model per penjelasan.

**Statistik (dikunci sekarang):**
- Unit analisis = jendela, digabung lintas 3 seed.
- Metode A dinyatakan "lebih baik" dari B dalam satu sel (data × model) hanya bila **Wilcoxon berpasangan p < 0,05 setelah koreksi Holm** atas semua perbandingan di sel itu **dan** tanda selisihnya sama di ketiga seed.
- Lintas sel: peringkat rata-rata + uji Friedman (diagram critical difference).

**Gerbang kualitas model:** MSE test dilaporkan bersama pembanding trivial (forecast rata-rata) dan, bila ada, oracle. Model yang tidak mengalahkan forecast rata-rata dikeluarkan dari analisis XAI, dengan pencatatan.

**Aturan anti-terjebak:**
- Benchmark melaporkan semua sel apa adanya.
- Tidak ada metode, varian, atau metrik baru setelah melihat hasil. Analisis tambahan ditulis terpisah sebagai *post-hoc/eksploratif*.
- Bila RQ1 di v2 ternyata positif untuk sebagian sel, itu dilaporkan sebagai kondisi batas, bukan diangkat menjadi klaim metode.

**Status eksekusi (2026-11-03):**
- **Kode:**
  - `src/models/zoo.py`;
  - `src/bench/tasks.py` (g1, g2a/b/c, g3, etth1, weather);
  - `scripts/bench_train.py`, `scripts/bench_explain.py`, `scripts/bench_analyze.py`, `scripts/prepare_shapformer.py`;
  - test: `tests/test_zoo.py`, `tests/test_bench_tasks.py`.
- **Antrean:** `bash results/bench/queue.sh "<tasks>" "<models>" "<seeds>"` (train → explain, langkah yang sudah selesai dilewati). Log ada di `results/bench/queue_*.log`, hasil di `results/bench/<task>/<model>_s<seed>/`.
- **GS-SHAP resmi:** di-clone ke `external/GroupSegment-SHAP` (commit `8ed7e2a`, tanpa lisensi, tidak didistribusikan ulang). Dipanggil persis seperti `evaluate_method_on_sample` di skrip sintetisnya: grup HSIC dari data train, MMD maks. 10 segmen, panjang minimal L/10, anggaran 1.500 evaluasi.
- **Data SHAPformer:** diunduh dari share KIT ke `dataset/external/shapformer/` lewat range request (zip Deflate64). Additivity dicek: y ≈ base[168:] + Σ φ, sisa rata-rata 0,0115 (noise).
- **Data publik (fase 2):** metrik utama deletion AOPC; sebuah klaim harus konsisten di kedua masker.
- **Perubahan data pra-hasil (Weather, 2026-11-03):**
  - `weather.csv` berisi nilai penanda rusak −9999 di 80 baris, semuanya di bagian train: 50 di OT, 30 di `max. PAR`, 1 di `wv`.
  - Akibatnya simpangan baku train OT melonjak dari 18 menjadi 384. Target uji terjepit ke skala ±0,04, dan loss training didominasi titik rusak (uji smoke: train 1,02 vs val 0,003).
  - Penanda (≤ −9990) diganti interpolasi linear sebelum standardisasi. Hasil uji smoke setelahnya: train 0,34, val 0,49, skill uji 0,66.
  - Keputusan ini diambil sebelum ada hasil publik apa pun. Konsekuensinya, MSE Weather kita **tidak sebanding** dengan angka Weather di literatur, yang membiarkan penanda ini. Benchmark ini memang tidak mengklaim akurasi ramalan.
  - ETTh1 tidak punya penanda.

**Urutan kerja:**
1. Model M-V/M-E/C-V + test.
2. Adapter G2 dan G3.
3. Training (3 seed per model × data).
4. Evaluasi XAI.
5. Fase 2: data publik.


### 2026-11-04 — Pra-registrasi replikasi v2.1: ketergantungan masker (ditulis sebelum eksperimen)

**Alasan:**
- Temuan RQ2 (masker membalik kesimpulan) dan dua tafsiran mekanismenya ditemukan di data yang sama (ETTh1, Weather), jadi masih berstatus post-hoc.
- Untuk menjadikannya klaim konfirmatori, ketiganya diuji ulang di data publik **baru** dengan kriteria yang dikunci di sini.

**Data baru** (dipilih dan dicek sebelum ada hasil; tidak ada penanda rusak atau NaN):

| Data | Channel | Resolusi | Split |
|---|---|---|---|
| ETTh2 | 7 | per jam | 12/4/4 bulan |
| ETTm1 | 7 | 15 menit | 12/4/4 bulan |
| Exchange Rate | 8 | harian | 70/10/20 |

- ETTm2 tidak dipakai karena statistiknya hampir identik dengan ETTh2.
- Electricity dan Traffic tidak dipakai karena jumlah channelnya (321 dan 862) terlalu besar untuk KernelSHAP dan GS-SHAP.

**Yang tidak berubah:** protokol v2 apa adanya, termasuk model, L = H = 96, 3 seed, 50 jendela, metode, metrik, masker, statistik, dan gerbang kualitas. Hasilnya **12 sel baru** (3 data × 4 model).

**Hipotesis konfirmatori.** Dihitung dari rata-rata sel (jendela digabung lintas seed); Random dikeluarkan; peringkat 1 = AOPC tertinggi.

| | Hipotesis | Kriteria lulus (12 sel baru) | Temuan asal (ETTh1 + Weather, 8 sel) |
|---|---|---|---|
| M1 | Peringkat metode tidak stabil antar masker | Median τ(del-mean, del-interp) < 0,5 **dan** metode terbaik berbeda di ≥ 6/12 sel | median τ ≈ 0,03; terbaik berbeda 8/8 |
| M2 | Deletion-interp menguntungkan atribusi kasar | Peringkat SHAP-C lebih baik (angka lebih kecil) di del-interp daripada di del-mean pada ≥ 10/12 sel (uji tanda satu sisi p < 0,05; seri = gagal) | SHAP-C terbaik menurut interp di 4/4 sel Weather |
| M3 | Deletion-mean menguntungkan SHAP bermasker mean (penilaian berputar) | AOPC rata-rata SHAP-U8 > IG-U8 di del-mean pada ≥ 10/12 sel **dan** di del-interp pada ≤ 6/12 sel | verdik A di del-mean 8/8; di del-interp 3/2/3 |

**Sekunder (deskriptif):** MambaLRP vs IG, dihitung sebagai jumlah sel "A di kedua masker" dengan aturan terkunci. Temuan asalnya 2/6.

**Pelaksanaan:**
- Skrip `scripts/bench_replication.py` ditulis sebelum run dan menghasilkan `results/bench/replication.md`.
- Hipotesis yang gagal dilaporkan apa adanya dan tidak diselamatkan dengan varian baru.


### 2026-11-08 — Pra-registrasi tambahan v2.2 (ditulis sebelum eksperimen)


**A. Contoh peta penjelasan (deskriptif, tanpa uji).**
- **Model:** PlainMamba seed 0, satu-satunya model tempat semua metode terdefinisi.
- **Aturan pemilihan jendela** (dikunci agar tidak memilih contoh yang "cantik"):
  - G1: jendela pertama dalam urutan jendela yang dijelaskan yang punya ≥ 1 sel GT;
  - G2a: jendela pertama.
- **Panel:** GT, IG, MambaLRP, SHAP-U8, SHAP-Δ8, GS-SHAP. AP setiap panel ditulis di gambar.

**B. Anggaran estimator: apakah KernelSHAP kalah karena kurang sampel?**
- **Cakupan:** G1 dan G2a–c, 4 model, 3 seed, jendela yang sama dengan v2. Totalnya 16 sel.
- **Anggaran dinaikkan:**
  - KernelSHAP 4× sampel (8.192, bukan 2.048) untuk SHAP-U4/U8/U16;
  - Integrated Gradients 128 langkah (bukan 32) untuk IG dan IG-U4/U8/U16.
- **Hipotesis B1 (kekalahan SHAP bukan karena kurang sampel):** dengan 4× sampel, SHAP-U8 tidak lebih baik dari IG-U8 (32 langkah, hasil v2) menurut aturan terkunci (AP) di ≥ 14 dari 16 sel.
- **Deskriptif:**
  - perubahan AP rata-rata per metode akibat anggaran;
  - korelasi Spearman antara peta default dan peta beranggaran besar (konvergensi);
  - IG-U8 128 langkah vs 32 langkah.
- **Rincian pelaksanaan, ditambahkan 2026-11-08 sebelum hasil B ada:** benchmark hanya menyimpan metrik per jendela, bukan peta atribusi. Karena itu korelasi peta (konvergensi) dihitung ulang pada subset: seed 0, 10 jendela pertama yang dijelaskan per sel, untuk SHAP-U8 dan IG-U8. Uji B1 sendiri memakai semua jendela dan semua seed.

**C. Ketahanan horizon: apakah temuan masker berlaku untuk horizon lain?**
- **Cakupan:** ETTh1 dan Weather, H ∈ {192, 336, 720}, L = 96, 4 model × 3 seed = 72 run. Pengaturan lain tidak berubah, termasuk gerbang kualitas; persistence dilaporkan secara deskriptif.
- **Hipotesis per horizon** (8 sel per horizon):
  - **M1-H:** median τ(mean, interp) < 0,5 **dan** metode terbaik berbeda di ≥ 4/8 sel.
  - **M2-H:** SHAP-C berperingkat lebih baik di interp daripada di mean pada ≥ 7/8 sel (uji tanda satu sisi p = 0,035).
- **Lulus keseluruhan** bila M1-H dan M2-H lulus di ketiga horizon. Hasil dilaporkan per horizon.
- **M3 tidak diuji ulang** karena sudah ditutup.
- **Sekunder (deskriptif):** MambaLRP vs IG di kedua masker.

**Aturan umum:**
- Hasil yang gagal dilaporkan apa adanya.
- Sel-sel ini tidak dimasukkan ke peringkat utama 28 sel.
- Skrip: `scripts/bench_budget.py` (B), `scripts/bench_replication.py --set horizon` (C), `scripts/paper_examples.py` (A).


### 2026-11-11 — Pra-registrasi Opsi A: replikasi RQ1 dan RQ2 pada kode resmi (ditulis sebelum ada run)

**Tujuan.** Menguji apakah dua temuan utama bertahan pada forecaster Mamba resmi berukuran penuh, dengan kernel `mamba_ssm`, keluaran multivariat dan resep pelatihan penulisnya. Ini pelengkap §7.4 naskah, bukan pengganti benchmark zoo (Tabel 4–7).

**Model dan pelatihan (persis skrip resmi, H = 96).**
- S-Mamba, `third_party/official/S-D-Mamba` commit `e7e8bf0` (tanpa lisensi: dijalankan, tidak disalin). ETTh1: `scripts/multivariate_forecasting/ETT/S_Mamba_ETTh1.sh` blok 96_96 (d_model 256, d_ff 256, 2 lapis, d_state 2, lr 7e-5, batch 32, 10 epoch, patience 3). Weather: `Weather/S_Mamba.sh` blok 96_96 (d_model 512, d_ff 512, 3 lapis, d_state 2, lr 5e-5, 5 epoch). Satu-satunya perubahan pada klon: baris `fix_seed = 2023` di `run.py` membaca variabel lingkungan `SEED` (nilai asli tetap default).
- TimeMachine, `third_party/official/TimeMachine` commit `5bf17a7` (Apache-2.0). ETTh1: `scripts/TimeMachine/etth1.sh` cabang pred_len 96 (n1 512, n2 32, dropout 0,7, revin 1, **ch_ind 1**, residual 1, d_state 256, dconv 2, e_fact 1, batch 512, lr 1e-3, 100 epoch, lradj type3). Weather: `weather.sh` cabang 96 (n1 128, n2 16, dropout 0,1, lradj constant, pct_start 0,2, selebihnya sama).
- Seed 0, 1, 2 untuk kedua model. Checkpoint di `results/opsA/ckpt/<model>_<data>_s<seed>/`. Data: `dataset/ETT-small/ETTh1.csv`, `dataset/weather/weather.csv` lewat loader resmi masing-masing (scaler train, border standar; Weather **tanpa** interpolasi sentinel −9999, berbeda dari zoo).
- **Inklusi:** MSE test multivariat (metrik resmi, ruang terstandar) ≤ 1,10 × nilai yang dilaporkan paper masing-masing pada H 96: S-Mamba ETTh1 0,386 dan Weather 0,165 [wang2025smamba, Tabel 2]; TimeMachine ETTh1 0,364 [ahamed2024, Tabel 2]; TimeMachine Weather 0,164 [ahamed2024, Tabel 2; dibaca 2026-11-11 sebelum ada hasil penjelasan]. Model yang tidak lolos tetap dijelaskan, tetapi selnya ditandai dan dikeluarkan dari uji konfirmatori.

**Penjelasan (sama dengan v2 kecuali yang disebut).**
- 50 window test (linspace atas indeks dataset test resmi), kuantitas yang dijelaskan = rata-rata ramalan OT (kolom terakhir) atas 96 langkah horizon. Fitur waktu (x_mark, S-Mamba) dianggap konteks tetap dan tidak diatribusikan.
- 13 metode: Random, GxI, IG (32 langkah), IG-U4/8/16, SHAP-C, SHAP-U4/8/16 (Kernel SHAP 2.048 sampel, masker mean), SHAP-MMD8, GS-SHAP (anggaran 1.500 panggilan, grup HSIC dari data train resmi), MambaLRP lewat jalur referensi murni-PyTorch dari modul `mamba_ssm.Mamba` dengan aturan detach yang sama (`src/xai/official_adapter.py`). SHAP-Δ8 tidak berlaku (tidak ada scan waktu).
- Faithfulness: deletion dan insertion AOPC, fraksi 2/5/10/20/30 %, masker mean (= 0, rata-rata train) dan interp. Sanity: korelasi Spearman dengan model acak pada 8 window.
- **Prasyarat teknis yang harus lulus sebelum penjelasan** (`scripts/opsA_equivalence.py`): (i) forward referensi = forward `mamba_ssm` (selisih maks < 1e-4, nilai dan gradien terhadap input); (ii) `PurePyTorchMamba` dengan bobot disalin = `mamba_ssm` (selisih maks < 1e-4), sebagai jawaban atas kritik "scan PyTorch sendiri"; (iii) mode LRP tidak mengubah nilai forward. Kegagalan di sini adalah bug kode yang diperbaiki, bukan alasan mengubah hipotesis.

**Hipotesis konfirmatori** (4 sel = {ETTh1, Weather} × {S-Mamba, TimeMachine}; n = 150 window per sel, 3 seed digabung; Wilcoxon berpasangan, Holm atas semua uji HA1 di 4 sel, tanda sama di 3 seed):
- **HA1 (RQ1 di model resmi):** MambaLRP − IG pada deletion AOPC masker mean > 0 di ≥ 3/4 sel (zoo: 4/4; selisih +0,028, +0,055, +0,016, +0,064). Sekunder, deskriptif: masker interp (zoo: 2/4 "A better").
- **HA2 (M1 di model resmi):** metode terbaik berbeda antara masker mean dan interp di ≥ 3/4 sel dan median τ Kendall < 0,5 (zoo: 4/4 berbeda; τ −0,18, −0,42, +0,27, +0,27).
- **HA3 (M2 di model resmi):** SHAP-C berperingkat lebih baik di bawah interp daripada mean di 4/4 sel (ambang n = 4 mengikuti aturan ⌈10n/12⌉ dari v2.1; zoo 4/4).
- Tidak ada gerbang seed 0 pada hasil: ke-12 run dijalankan semua karena murah. Satu-satunya alasan berhenti adalah kegagalan teknis.

**Operasionalisasi (ditambahkan 2026-11-11 sebelum ada hasil penjelasan; `scripts/opsA_analyze.py`).** Run-seed yang gagal inklusi dibuang; sel tetap konfirmatori bila ≥ 2 seed tersisa, selain itu deskriptif. HA1: Holm atas uji masker mean di sel konfirmatori; interp keluarga Holm sendiri, deskriptif. HA2: rata-rata metode per sel atas window gabungan, τ Kendall. HA3: peringkat SHAP-C (1 = terbaik) per masker. Penyimpangan teknis yang dicatat: (a) `np.Inf` → `np.inf` di `utils/tools.py` kedua repo (NumPy 2, tanpa efek perilaku); (b) seed `run.py` S-Mamba dari variabel lingkungan; (c) wrapper S-Mamba menulis ulang `forecast` tanpa pembagian in-place (pembagian in-place aslinya memutus gradien terhadap input), nilainya identik (uji (iii), selisih 0).

**Pelaporan.** Apa pun hasilnya: Supplementary S9 (tabel per sel, MSE vs paper, τ, peringkat) dan satu paragraf di §6 plus revisi kalimat §7.4. Hipotesis yang gagal dilaporkan sebagai batas validitas temuan zoo. Tidak ada varian metode baru.
