import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


# layang-layang
def luas_layang_layang(d1, d2):
    return 0.5 * d1 * d2


def keliling_layang_layang(sisi1, sisi2):
    return 2 * (sisi1 + sisi2)


# jajar genjang
def keliling_jajar_genjang(sisi_a, sisi_b):
    return 2 * (sisi_a + sisi_b)


# belah ketupat
def luas_belah_ketupat(d1, d2):
    return 0.5 * d1 * d2


def keliling_belah_ketupat(sisi):
    return 4 * sisi


# trapesium
def luas_trapesium(panjang_atas, panjang_bawah, tinggi):
    return 0.5 * (panjang_atas + panjang_bawah) * tinggi


def keliling_trapesium(sisi_a, sisi_b, sisi_c, sisi_d):
    return sisi_a + sisi_b + sisi_c + sisi_d


# lingkaran
def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari**2


def keliling_lingkaran(jari_jari):
    return 2 * 3.14 * jari_jari


# segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi


def tinggi_segitiga(luas, alas):
    return (2 * luas) / alas


def alas_segitiga(luas, tinggi):
    return (2 * luas) / tinggi


def keliling_segitiga(sisi_a, sisi_b, sisi_c):
    return sisi_a + sisi_b + sisi_c


def main():
    (
        col1,
        col2,
    ) = st.columns(2)

    # navigasi sidebar
    with st.sidebar:
        selected = option_menu(
            "Menu",
            [
                "Home",
                "Persegi",
                "Persegi Panjang",
                "Jajar Genjang",
                "Segitiga",
                "Belah Ketupat",
                "Layang-Layang",
                "Trapesium",
                "Lingkaran",
            ],
            icons=[
                "house",
            ],
            menu_icon="cast",
            default_index=0,
        )

    # halaman 1
    if selected == "Home":
        st.title("Selamat Datang di Aplikasi Bangun Datar")
        st.image("mtk.png")
        st.write(
            "Aplikasi bangun datar adalah alat yang sangat berguna dalam dunia geometri. Dengan menggunakan aplikasi ini, Anda dapat dengan cepat dan akurat menghitung berbagai parameter dari berbagai bentuk geometris, seperti persegi, segitiga, lingkaran, dan lain-lain. Dengan kemampuan untuk menghitung luas, keliling, dan beberapa parameter lainnya, aplikasi ini sangat membantu dalam menyelesaikan berbagai masalah matematika.''Untuk membuka kalkulatornya tekan slider bar bagian pojok kiri atas''."
        )
        st.write(
            "''Sebelum meraih bantuan dari aplikasi bangun datar kami, mari tantang diri Anda dengan meracik solusi permasalahan diri sendiri melalui rumus yang telah kami berikan di ''TOMBOL MULAI'' bagian bawah. Kemahiran Anda adalah kunci menuju pemahaman yang mendalam!''"
        )
        st.markdown(
            "Created by [arffrmnsh](https://www.instagram.com/ariffirmnsh/). | © 2023"
        )
        if st.button("Mulai"):
            selected = "Rumus"  # Mengganti halaman ke "Rumus"

    # halaman 2 (Rumus)
    if selected == "Rumus":
        st.image("rumus.png")
        
    if selected == "Persegi":
        with col1:
            st.title("Hitung luas")
            sisi = st.number_input("masukan nilai", 0)
            hitung = st.button("hitung luas")

            if hitung:
                luas = sisi * sisi
                st.write("luas persegi adalah = ", luas)
                st.success(f"luas persegi adalh = {luas}")
                st.balloons()

        with col2:
            st.title("Hitung keliling")
            sisi = st.number_input("masukan nilai sisi", 0)
            hitung = st.button("hitung keliling")

            if hitung:
                keliling = 4 * sisi
                st.write("keliling persegi adalah = ", keliling)
                st.success(f"keliling persegi adalah = {keliling}")
                st.balloons()

    # halaman 2
    elif selected == "Persegi Panjang":
        with col1:
            st.title("Hitung luas")
            panjang = st.number_input("masukan nilai panjang", 0)
            lebar = st.number_input("masukan nilai lebar", 0)
            hitung = st.button("hitung luas")

            if hitung:
                luas = panjang * lebar
                st.write("luas persegi panjang adalah = ", luas)
                st.success(f"luas persegi panjang adalah = {luas}")
                st.balloons()

        with col2:
            st.title("Hitung keliling")
            panjang_keliling = st.number_input("masukan nilai panjang persegi", 0)
            lebar_keliling = st.number_input("masukan nilai lebar persegi", 0)
            hitung = st.button("hitung keliling")

            if hitung:
                keliling = 2 * panjang_keliling + 2 * lebar_keliling
                st.write("keliling persegi panjang adalah = ", keliling)
                st.success(f"keliling persegi panjang adalah = {keliling}")
                st.balloons()

    # halaman 3
    elif selected == "Jajar Genjang":
        with col1:
            st.title("Hitung Luas")
            alas = st.number_input("Masukkan nilai alas:", step=0, min_value=0)
            tinggi = st.number_input("Masukkan nilai tinggi:", step=0, min_value=0)
            hitung_luas = st.button("Hitung Luas")

            if hitung_luas:
                luas = alas * tinggi
                st.write(f"Luas Jajar Genjang adalah: {luas}")
                st.success(f"luas Jajar Genjang adalah = {luas}")
                st.balloons()

        with col2:
            st.title("Hitung Keliling")
            sisi_a = st.number_input("Masukkan panjang sisi a:", step=0, min_value=0)
            sisi_b = st.number_input("Masukkan panjang sisi b:", step=0, min_value=0)
            hitung_keliling = st.button("Hitung Keliling")

            if hitung_keliling:
                keliling = keliling_jajar_genjang(sisi_a, sisi_b)
                st.write(f"Keliling Jajar Genjang adalah: {keliling}")
                st.success(f"Keliling Jajar Genjang adalah = {keliling}")
                st.balloons()

    # halaman 4 (Segitiga)
    if selected == "Segitiga":
        with col1:
            st.title("Hitung Luas")
            alas = st.number_input("Masukkan nilai alas:", step=0, key="alas")
            tinggi = st.number_input("Masukkan nilai tinggi:", step=0, key="tinggi")
            hitung_luas = st.button("Hitung Luas")

            if hitung_luas:
                luas = luas_segitiga(alas, tinggi)
                st.write(f"Luas Segitiga adalah: {luas}")
                st.success(f"luas segitiga adalah = {luas}")
                st.balloons()

        with col2:
            st.title("Hitung Keliling")
            sisi_a = st.number_input("Masukkan panjang sisi A:", step=0, key="sisi_a")
            sisi_b = st.number_input("Masukkan panjang sisi B:", step=0, key="sisi_b")
            sisi_c = st.number_input("Masukkan panjang sisi C:", step=0, key="sisi_c")
            hitung_keliling = st.button("Hitung Keliling")

            if hitung_keliling:
                keliling = keliling_segitiga(sisi_a, sisi_b, sisi_c)
                st.write(f"Keliling Segitiga adalah: {keliling}")
                st.success(f"keliling segitiga adalah = {keliling}")
                st.balloons()

        with col1:
            st.title("Hitung Tinggi")
            luas_segitiga_tinggi = st.number_input(
                "Masukkan nilai luas:", step=0, key="luas_segitiga_tinggi"
            )
            alas_segitiga_tinggi = st.number_input(
                "Masukkan nilai alas:", step=0, key="alas_segitiga_tinggi"
            )
            hitung_tinggi = st.button("Hitung Tinggi")

            if hitung_tinggi:
                tinggi = tinggi_segitiga(luas_segitiga_tinggi, alas_segitiga_tinggi)
                st.write(f"Tinggi Segitiga adalah: {tinggi}")
                st.success(f"tinggi segitiga adalah = {tinggi}")
                st.balloons()

        with col2:
            st.title("Hitung Alas")
            luas_segitiga_alas = st.number_input(
                "Masukkan nilai luas:", step=0, key="luas_segitiga_alas"
            )
            tinggi_segitiga_alas = st.number_input(
                "Masukkan nilai tinggi:", step=0, key="tinggi_segitiga_alas"
            )
            hitung_alas = st.button("Hitung Alas")

            if hitung_alas:
                alas = alas_segitiga(luas_segitiga_alas, tinggi_segitiga_alas)
                st.write(f"Alas Segitiga adalah: {alas}")
                st.success(f"alas segitiga adalah = {alas}")
                st.balloons()

    # halaman 5 (Belah Ketuapat)
    if selected == "Belah Ketupat":
        with col1:
            st.title("Hitung Luas")
            d1 = st.number_input("Masukkan panjang diagonal 1:", step=0, min_value=0)
            d2 = st.number_input("Masukkan panjang diagonal 2:", step=0, min_value=0)
            hitung = st.button("Hitung Luas")

            if hitung:
                luas = luas_belah_ketupat(d1, d2)
                st.write(f"Luas Belah Ketupat adalah: {luas}")
                st.success(f"luas belah ketupat adalah = {luas}")
                st.balloons()

        with col2:
            st.title("Hitung Keliling")
            sisi = st.number_input("Masukkan panjang sisi:", step=0, min_value=0)
            hitung = st.button("Hitung Keliling")

            if hitung:
                keliling = keliling_belah_ketupat(sisi)
                st.write(f"Keliling Belah Ketupat adalah: {keliling}")
                st.success(f"keliling belah ketupat adalah = {keliling}")
                st.balloons()

    # halaman 6 (Layang-Layang)
    if selected == "Layang-Layang":
        with col1:
            st.title("Hitung Luas")
            d1 = st.number_input("Masukkan panjang diagonal 1:", step=0, min_value=0)
            d2 = st.number_input("Masukkan panjang diagonal 2:", step=0, min_value=0)
            hitung = st.button("Hitung Luas")

            if hitung:
                luas = luas_layang_layang(d1, d2)
                st.write(f"Luas Layang-Layang adalah: {luas}")
                st.success(f"luas layang-layang adalah = {luas}")
                st.balloons()

        with col2:
            st.title("HitungKeliling")
            sisi1 = st.number_input("Masukkan panjang sisi 1:", step=0, min_value=0)
            sisi2 = st.number_input("Masukkan panjang sisi 2:", step=0, min_value=0)
            hitung_keliling = st.button("Hitung Keliling")

            if hitung_keliling:
                keliling = keliling_layang_layang(sisi1, sisi2)
                st.write(f"Keliling Layang-Layang adalah: {keliling}")
                st.success(f"keliling layang-layang adalah = {keliling}")
                st.balloons()

    # halaman 7 (Trapesium)
    if selected == "Trapesium":
        with col1:
            st.title("Hitung Luas")
            panjang_atas = st.number_input(
                "Masukkan panjang atas:", step=0, key="panjang_atas_trap"
            )
            panjang_bawah = st.number_input(
                "Masukkan panjang bawah:", step=0, key="panjang_bawah_trap"
            )
            tinggi = st.number_input("Masukkan tinggi:", step=0, key="tinggi_trap")
            hitung_luas = st.button("Hitung Luas")

            if hitung_luas:
                luas = luas_trapesium(panjang_atas, panjang_bawah, tinggi)
                st.write(f"Luas Trapesium adalah: {luas}")
                st.success(f"luas trapesium adalah = {luas}")
                st.balloons()

        with col2:
            st.title("Hitung Keliling")
            sisi_a = st.number_input(
                "Masukkan panjang sisi A:", step=0, key="sisi_a_trap"
            )
            sisi_b = st.number_input(
                "Masukkan panjang sisi B:", step=0, key="sisi_b_trap"
            )
            sisi_c = st.number_input(
                "Masukkan panjang sisi C:", step=0, key="sisi_c_trap"
            )
            sisi_d = st.number_input(
                "Masukkan panjang sisi D:", step=0, key="sisi_d_trap"
            )
            hitung_keliling = st.button("Hitung Keliling")

            if hitung_keliling:
                keliling = keliling_trapesium(sisi_a, sisi_b, sisi_c, sisi_d)
                st.write(f"Keliling Trapesium adalah: {keliling}")
                st.success(f"keliling trapesium adalah = {keliling}")
                st.balloons()

    # halaman 8 (Lingkaran)
    if selected == "Lingkaran":
        with col1:
            st.title("Hitung Luas")
            jari_jari = st.number_input(
                "Masukkan jari-jari lingkaran:", step=0, key="jari_jari_lingkaran"
            )

            hitung_luas = st.button("Hitung Luas")

            if hitung_luas:
                luas = luas_lingkaran(jari_jari)
                st.write(f"Luas Lingkaran adalah: {luas}")
                st.success(f"luas lingkaran adalah = {luas}")
                st.balloons()

        with col2:
            st.title("Hitung Keliling")
            jari_jari_keliling = st.number_input(
                "Masukkan jari-jari lingkaran:",
                step=0,
                key="jari_jari_lingkaran_keliling",
            )
            hitung_keliling = st.button("Hitung Keliling")

            if hitung_keliling:
                keliling = keliling_lingkaran(jari_jari_keliling)
                st.write(f"Keliling Lingkaran adalah: {keliling}")
                st.success(f"keliling lingkaran adalah = {keliling}")
                st.balloons()


if __name__ == "__main__":
    main()
