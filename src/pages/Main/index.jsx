import Header from './Header'
import ImageSearch from './ImageSearch'


export default function Main() {

    return(
        <>
        <Header />
        <ImageSearch />

        <div className="tag">
        <br id="how"/>
        <br/><br/><br/>
        <hr/>
            <div className="HOW">
                <h2><u>How to Use</u></h2>
                <h3>Langkah 1: Unggah Folder Dataset</h3>
                <p>- Klik pada tombol "Unggah Folder Dataset".</p>
                <p>- Pilih folder dataset yang berisi gambar-gambar yang ingin Anda gunakan untuk mencari gambar serupa.</p>
                <h3>Langkah 2: Pilih File Gambar</h3>
                <p>- Klik pada tombol "Unggah File Gambar".</p>
                <p>- Pilih satu file gambar yang akan menjadi dasar pencarian gambar serupa.</p>
                <p>- Pastikan file gambar yang dipilih sesuai dengan format yang didukung oleh website.</p>
                <h3>Langkah 3: Langkah 6: Tentukan Parameter Pencarian</h3>
                <p>- Terdapat 2 opsi parameter pencarian yaitu colors dan textures, sesuaikan parameter pencarian sesuai kebutuhan Anda.</p>
                <h3>Langkah 4: Mulai Pencarian</h3>
                <p>- Setelah mengunggah folder dataset dan memilih file gambar, klik tombol "Mulai Pencarian" atau opsi serupa.</p>
                <p>- Tunggu hingga proses pencarian selesai.</p>
                <h3>Langkah 5: Hasil Pencarian</h3>
                <p>- Setelah proses pencarian selesai, website akan menampilkan hasil yang mencakup gambar-gambar dari dataset yang mirip atau memiliki warna dan tekstur serupa dengan file gambar yang Anda unggah.</p>
            </div>
            <hr/>

            <div className="BASIC">
                <h2 id="concepts"><u>Basic Concepts</u></h2>
                <p>Platform ini mengadopsi aljabar vektor sebagai dasar untuk menggambarkan dan menganalisis data, terutama dalam konteks klasifikasi berbasis konten yang dikenal sebagai Content-Based Image Retrieval (CBIR). Fokus utama sistem ini adalah pada identifikasi gambar berdasarkan konten visual, seperti warna dan tekstur. Pengguna mengakses platform melalui peramban web, di mana antarmuka pengguna yang intuitif memungkinkan pengunggahan folder dataset yang berisi gambar-gambar referensi. Setiap gambar dalam dataset diinterpretasikan sebagai vektor dalam ruang fitur, dan analisis menggunakan aljabar vektor dilakukan untuk menganalisis karakteristik visual seperti warna dan tekstur. Pengguna dapat memilih satu gambar dari dataset sebagai referensi untuk memulai proses pencarian gambar serupa. Sistem menggunakan metode klasifikasi berbasis konten, yang melibatkan aljabar vektor, untuk mencocokkan gambar referensi dengan gambar lain dalam dataset. Hasil pencarian kemudian disajikan kepada pengguna. Dengan pendekatan ini, aljabar vektor menjadi fondasi yang kuat untuk menggambarkan dan menganalisis konten visual, memungkinkan sistem temu balik gambar mengidentifikasi gambar berdasarkan karakteristik warna dan tekstur dengan akurat.</p>
            </div>
            <hr/>

            <div className="ABOUT">
                <h2 id="about"><u>About Us</u></h2>
                <p>Platform ini dikembangkan oleh tim ALLENS yang terdiri dari 3 mahasiswi Teknik Informatika ITB angkatan 2022, yaitu:</p>
                <p>1. Thea Josephine H (13522012)</p>
                <p>2. Diana Tri Handayani (13522104)</p>
                <p>3. Chelvadinda (13522154)</p>
            </div>
            <hr />
        </div>
        </>
    )
}