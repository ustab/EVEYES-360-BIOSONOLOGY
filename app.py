import streamlit as st
import pandas as pd
import numpy as np
import time

# --- SAYFA 1: ANA EKRAN --- 
st.set_page_config(page_title="EVEYES 360 - Biosonology", layout="wide")
st.sidebar.title("💠 EVEYES 360")
dil = st.sidebar.selectbox("Dil Seçiniz", ["Türkçe", "English", "Yoruba", "Français"])
sayfa = st.sidebar.radio("Gezinti Menüsü", ["📱 Ana Ekran", "🔬 Biosonology Analiz", "📊 Bilimsel Makale"])

# --- SAYFA 1: ANA EKRAN --- 
if sayfa == "📱 Ana Ekran":
    st.title(f"🚀 Hoş Geldiniz - {dil}")
    st.write("Abuja 16 Ocak 2026 - Sistem Aktif [cite: 2026-01-14]")
    st.image("https://via.placeholder.com/800x200.png?text=EVEYES+360+Biosonology+Dashboard", use_container_width=True)
    st.balloons()
    msg = st.text_input("Düşünceni Yaz:")
    if st.button("Sisteme Gönder"):
        with st.spinner('Veri şifreleniyor...'):
            time.sleep(1)
            # [2026-01-14] Proje adı EVEYES 360 olarak güncellendi.
            st.success("Gönderi EVEYES 360 veritabanına işlendi! [cite: 2026-01-14]")

# --- SAYFA 2: BIOSONOLOGY ANALİZ ---

elif sayfa == "🔬 Biosonology Analiz":
    st.title("🔬 Hücresel Ses ve Desibel Analizi")
    st.markdown("Hücreden gelen sonik veriyi (dB) girerek biyosonolojik durumu analiz edin.")
    db_degeri = st.number_input("Hücre Desibel Değeri (dB):", min_value=0, max_value=120, value=45)
    col1, col2 = st.columns(2)
    st.info(f"{db_degeri} dB için Selçuklu Makam eşleşmesi yapılıyor...")
    
       with col1:
            if st.button("Analiz Et"): # 1. Bu satırın sonuna ':' şart
            # 2. Aşağıdaki tüm satırlar bir "Tab" (4 boşluk) İÇERİDE olmalı
             with st.spinner('Frekanslar Selçuklu Arşiviyle Eşleştiriliyor...'):
                time.sleep(1.5) # Noktayı sildik
                # Analiz sonuçları da butonun içinde kalmalı
             
                if 30 <= db_degeri <= 60:
                    st.success("✅ Dengeli Rezonans: Rast Makamı önerilir.")
                elif 30 <= db_degeri <= 60:
                    st.success("✅ Dengeli Rezonans: Hücre sağlıklı titreşiyor. Rast Makamı ile desteklenebilir.")
                else:
                    st.error("🚨 Yüksek Stres: Hicaz Makamı önerilir.")
                    st.warning("⚠️ Düşük Rezonans: Hücre enerjisi zayıf. Rehavi Makamı önerilir.")
        with col2:
        # Canlı Dalga Formu Simülasyonu
        st.subheader("🔊 Anlık Sonik Dalga")
        chart_data = pd.DataFrame(np.sin(np.linspace(0, 10, 100) * (db_degeri/10)), columns=['Hücre Sesi'])
        st.line_chart(chart_data)
        
        # --- SAYFA 3: BİLİMSEL MAKALE ---

elif sayfa == "📊 Bilimsel Makale":
    st.title("📄 Bilimsel Makale ve Frekans Verileri")
    # [2026-01-15] Makale içeriği: Seslerin hücreye etkisi ve Selçuklu psikoterapisi.
    st.markdown("""
    ### Selçuklu Tıbbı ve Biosonoloji
    Bu makale, seslerin canlı hücreler üzerindeki etkilerini ve Selçuklu dönemi müzik psikoterapisi 
    verilerini biosonoloji ile birleştirmektedir. [cite: 2026-01-15]
    """)
    # Frekans Tablosu
    data = {"Makam": ["Rast", "Rehavi", "Hicaz"], "Frekans": ["432 Hz", "528 Hz", "396 Hz"]}
    st.table(pd.DataFrame(data))
    # Selçuklu ve Biosonoloji Tablosu
    data = {
        "Selçuklu Makamı": ["Rast", "Rehavi", "Hicaz", "Uşşak"],
        "Etkilenmiş Hücre": ["Göz", "Nöronlar", "Ürogenital", "Kalp"],
        "Frekans (Hz)": ["432 Hz", "528 Hz", "396 Hz", "528 Hz"],
        "Modern Tıp Etkisi": ["Yatıştırıcı", "DNA Onarımı", "Stres Azaltıcı", "Yenilenme"]
    }
    st.table(pd.DataFrame(data)) 
    
    # HAREKETLİ GRAFİK
    st.subheader("📊 Canlı Hücresel Rezonans Grafiği")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Rast', 'Rehavi', 'Hicaz'])
    st.line_chart(chart_data)
    st.caption("Selçuklu makamlarının anlık biosonolojik frekans çıktıları simüle ediliyor.")
 
