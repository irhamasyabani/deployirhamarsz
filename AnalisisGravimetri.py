import streamlit as st

import numpy as np

from streamlit_option_menu import option_menu

#welcome
with st.sidebar :
    
    from PIL import Image
    
    image = Image.open("MASBRO.jpg")
    
    st.image(image, caption="")
    
    selected = option_menu("Aplikasi Analisis Kuantitatif Gravimetri",
    ["Identitas Kelompok",
     "Analisis Gravimetri",
     "Perhitungan Kadar Unsur atau Senyawa Sampel",
     "Kalkulator Faktor Gravimetri",
     "Perhitungan Kadar Air Sampel",
     "Perhitungan Kadar Abu Sampel"],
    default_index=0)
    

    
if (selected == "Identitas Kelompok") :
    st.title("Identitas Anggota Kelompok")
    st.write ('''Daftar Anggota'')
    st.write ('' Diyana Iffah (2219065)'')
    st.write (''Alma Lubna Kamilia (2219032)'')
    st.write (''Lathifah Hasna (2219096)'')
    st.write (''Luthfi Muhammad Fikri (2219101)'')
    st.write (''Muh. Irham Asya'bani (2219110)'')
    
if (selected == "Analisis Gravimetri") :
    st.title("Analisis Gravimetri")
    st.write("ANALISIS GRAVIMETRI adalah salah satu metode analisis kuantitatif dalam penetapan suatu zat kimia berdasarkan beratnya. Prinsip dasar analisis gravimetri yaitu unsur atau senyawa target diendapkan dengan suatu pereaksi pengendap. Beberapa macam jenis metode dalam analisa gravimetri, yaitu metode penguapan, pengendapan, elektrolisis.")
    st.write("KADAR AIR adalah kuantitas air yang terdapat pada suatu bahan atau zat, diukur dalam satuan persentase atau fraksi dari massa atau volume zat tersebut. Kadar air dapat mempengaruhi kualitas dan stabilitas bahan, seperti makanan, obat-obatan, bahan bangunan, dan produk-produk lainnya. Kadar air yang terlalu tinggi atau rendah dapat menyebabkan kerusakan atau deteriorasi pada bahan tersebut.")
    st.write("KADAR ABU dalam analisis kimia adalah jumlah total senyawa anorganik yang tersisa setelah bahan organik terbakar pada suhu yang tinggi. Kadar abu dapat dihitung dengan mengukur berat sampel dan mengurangi berat abu dari berat awal sampel. Kadar abu biasanya digunakan sebagai indikator untuk mengukur kebersihan dan kualitas bahan organik, seperti makanan atau bahan bakar biomassa. Tingkat abu yang tinggi dapat mengindikasikan kontaminasi atau kualitas rendah dari sampel tersebut.")
    st.write("FAKTOR GRAVIMETRI adalah rasio antara massa substansi yang diendapkan dan jumlah zat di dalam sampel yang diukur. Faktor gravimetri digunakan dalam analisis gravimetri, sebuah metode analisis kimia di mana berat suatu zat dipakai untuk menentukan jumlah atau konsentrasi zat tersebut.")
    st.write("Nilai kadar ini dapat dihitung dengan menggunakan berbagai metode analisis gravimetri seperti metode penimbangan langsung, metode perbandingan, dan metode pemisahan gravimetri")
    
            
        
if (selected == "Perhitungan Kadar Unsur atau Senyawa Sampel") :
    st.title("Perhitungan Kadar Unsur atau Senyawa Sampel")
    st.write("Kadar % = berat endapan (g) x faktor gravimetri x 100 % / berat sampel (g)")

    # Membuat tiga kolom untuk input
    col1, col2, col3 = st.columns(3)

    # Input berat endapan (g)
    with col1:
        berat_endapan = st.number_input("Berat Endapan (g)")

    # Input faktor gravimetri
    with col2:
        faktor_gravimetri = st.number_input("Faktor Gravimetri")

    # Input berat sampel (g)
    with col3:
        berat_sampel = st.number_input("Berat Sampel (g)")
        
    if st.button ('Hitung') :
        Perhitungan_Kadar_Unsur_atau_Senyawa_Sampel = berat_endapan* faktor_gravimetri* 100 / berat_sampel
        st.success(f'Hasil Perhitungan Kadar Unsur atau Senyawa Sampel adalah  {Perhitungan_Kadar_Unsur_atau_Senyawa_Sampel}')
        st.balloons()
        

    
if (selected == "Kalkulator Faktor Gravimetri") :
    st.title("Kalkulator Faktor Gravimetri")
    st.write("Berat Molekul Unsur atau Senyawa / Berat Molekul Endapan")

    Berat_Molekul_Unsur_atau_Senyawa = st.number_input('Masukkan Berat Molekul Unsur atau Senyawa (dalam g/mol)')
    Berat_Molekul_Endapan = st.number_input('Masukkan Berat Molekul Endapan (dalam g/mol)')

    if st.button ('Hitung') :
        faktor_gravimetri = Berat_Molekul_Unsur_atau_Senyawa / Berat_Molekul_Endapan
        st.success(f'Hasil Faktor Gravimetri adalah {faktor_gravimetri}')
        st.balloons()
        
if (selected == "Perhitungan Kadar Air Sampel") :
    st.title("Perhitungan mencari Kadar Air Sampel")

    st.write("Perhitungan Kadar Air Sampel") 
    st.write("(massa sebelum - massa setelah) / (massa sampel * 100)")

    massa_sebelum = st.number_input('Masukkan massa bahan sebelum dioven (g) :', format='%.4f')
    massa_setelah = st.number_input('Masukkan massa bahan setelah dioven (g) :', format='%.4f')
    massa_sampel = st.number_input('Masukkan massa sampel (g) :', format='%.4f')

    if st.button('Hitung') :
        kadar_air = (massa_sebelum - massa_setelah) / (massa_sampel * 100)
        st.success(f'Hasil kadar air adalah {kadar_air}%')
        st.balloons()
        
            

if (selected == "Perhitungan Kadar Abu Sampel") :
    st.title ("Aplikasi Menghitung Kadar Abu Sampel")
    
    st.write("Perhitungan Kadar Abu Sampel")
    st.write("(massa sebelum - massa setelah) / (massa sampel* 100)")

    massa_sebelum = st.number_input('Masukkan massa bahan sebelum dibakar (g) :', format='%.4f')
    massa_setelah = st.number_input('Masukkan massa abu setelah dibakar (g) :', format='%.4f')
    massa_sampel  = st.number_input ('Masukkan massa sampel (g) :',format='%.4f') 
                                     
    if st.button('Hitung') :
        kadar_abu = (massa_sebelum - massa_setelah) / (massa_sampel * 100)
        st.success(f'Hasil kadar abu adalah {kadar_abu}')
