Soal No 1

Di hari pertama pendaftaran, panitia menemukan beberapa kejadian :
- Ada peserta yang panik karena halaman sempat loading lama, lalu menekan tombol Daftar berkali-kali yang mengakibatkan data masuk lebih dari sekali. (3)
- Ada yang mengisi asal: nama “.”, email “aaa”, atau bahkan mengosongkan form mengakibatkan data berantakan. (1)
- Di akhir hari, beberapa kelas yang kuotanya 25 orang ternyata terisi 30+ karena sistem tetap menerima pendaftaran. (4)
- Saat panitia mau rekap, muncul pertanyaan: “Kalau data dobel dan data tidak valid begini, mana yang dianggap resmi?” (2)

Perbaikan :
1. Saya ingin memperbaiki di kasus no 2 dikarenakan tidak adanya validasi pada form pendaftaran tersebut sehingga yang harus dilakukan untuk update form versi berikutnya yaitu memvalidasi nama sebanyak minimal 3 karakter, format emailnya harus valid (dengan mengandung karakter @) dan opsi pilihan kelasnya tidak boleh kosong agar peserta yang mengisi pendaftaran di form tersebut wajib mengisi fieldnya supaya data diri dari peserta yang mendaftar tidak boleh kosong.
2. Saya sarankan untuk update berikutnya, harus ada validasi data terhadap peserta yang mendaftar baik itu nama, email dan pemilihan kelasnya untuk memastikan keabsahan datanya agar bisa membedakan dari segi format nama, email dan pilihan kelasnya untuk bisa menentukan mana data yang bersifat resmi atau data palsu.
3. Saya sarankan untuk update berikutnya, ketika peserta selesai melakukan pendaftaran dan menekan tombol "Submit", maka yang harus dilakukan yaitu dengan memunculkan loading sebanyak (0 ms) dengan delay kecil sebanyak (800-1000 ms) untuk menghindari spam klik yang mengakibatkan data peserta yang masuk ke form dashboard panitianya muncul secara dobel (duplikat) dan melakukan proses pengiriman data pendaftarannya secara bergantian (queueing) agar tidak terjadi overload
4. Saya sarankan untuk update berikutnya, harus menambahkan status pendaftaran pesertanya baik itu "diterima", "pending" maupun "ditolak" agar ketika peserta menekan submit, maka sistem akan mempending terlebih dahulu sebelum periode pendaftaran tersebut berakhir agar sistem bisa menyeleksi dengan cara mengecek kuota pendaftarannya untuk memastikan kelengkapan data diri peserta pendaftar tersebut harus valid dan terisi dengan baik agar bisa menentukan penerimaan terhadap peserta yang mendaftar.
