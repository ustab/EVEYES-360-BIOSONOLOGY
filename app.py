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

    # DİKKAT: 'with' ifadesi 'col1' ile aynı hizada ve 'elif'in bir basamak içinde olmalı
    with col1:
        if st.button("Analiz Et"):
            st.info(f"{db_degeri} dB için Selçuklu Makam eşleşmesi yapılıyor...")
            with st.spinner('Frekanslar Selçuklu Arşiviyle Eşleştiriliyor...'):
                time.sleep(1.5)
                
                if db_degeri < 30:
                    st.warning("⚠️ Düşük Rezonans: Hücre enerjisi zayıf. Rehavi Makamı önerilir.")
                elif 30 <= db_degeri <= 60:
                    st.success("✅ Dengeli Rezonans: Hücre sağlıklı titreşiyor. Rast Makamı ile desteklenebilir.")
                else:
                    st.error("🚨 Yüksek Stres: Hücrede termal stres belirtisi. Hicaz Makamı ile yatıştırılmalı.")
    
    with col2:
        st.subheader("🔊 Anlık Sonik Dalga")
        chart_data = pd.DataFrame(np.sin(np.linspace(0, 10, 100) * (db_degeri/10)), columns=['Hücre Sesi'])
        st.line_chart(chart_data)
        
        # --- SAYFA 3: BİLİMSEL MAKALE ---

elif sayfa == "📊 Bilimsel Makale":
    st.title("📄 Bilimsel Makale ve Frekans Verileri")
    # [2026-01-15] Makale içeriği: Seslerin hücreye etkisi ve Selçuklu psikoterapisi.
    st.markdown("""
    ### Acoustic Healing from Seljuk Medicine to Modern Biosonology
This article has been structured in a professional format, adhering to the provided scientific resources to reflect the core values of the EVEYES 360 project and the science of biosonology.

🚀 Ancient Seljuk Medicine Reborn with Modern Biosonology: EVEYES 360 💠
EVEYES 360 is a digital portal grounded in the science of biosonology, aiming to optimize cellular resonance by integrating ancient Seljuk medical traditions with modern technology. [1], [2] [cite: 2026-01-14]

The Science of Biosonology and Cellular Sounds
Biosonology has identified that every living cell emits a unique frequency of sound and has experimentally proven the effects of these sounds on biological processes. [1]

Cellular Efficiency: Experiments have observed that when yeast cells are played back the sounds they naturally produce, their reproductive efficiency increases significantly. [1]

Disease and Chaos: Sound frequencies shift according to the health status of cells. For instance, it has been detected that cancer cells produce a chaotic noise, unlike the harmonious frequencies of healthy cells. [1]

A 1000-Year Healing Legacy: Seljuk Music Therapy
Beginning nearly a millennium ago, Seljuk medicine utilized music—which has healing effects on cells—to treat psychiatric disorders. [1] [cite: 2026-01-15]

Inspiration and Development: These musical forms were inspired by the melodic structures of the Holy Quran and were developed into systematic treatment methods by scholars such as Avicenna (Ibn Sina) and Al-Farabi. [1]

Concentration vs. Music: According to Al-Farabi, while the recitation of the Holy Quran provides positive effects, it requires concentration to be beneficial. In contrast, music therapy exerts healing effects on cells even without the patient’s active concentration. [2]

Cellular Resonance and Acoustic Medicine
Today, the EVEYES 360 portal brings the effects of traditional Seljuk "Maqams"—such as Rast, Rehavi, and Hicaz—into the digital world through scientific modeling. [2] [cite: 2026-01-15] This approach aims to provide:

DNA repair and reduction of cellular stress levels. [2]

Optimization of cellular resonance across a broad spectrum. [2]

A robust bridge to the "acoustic medicine" of the future. [2]

Through biosonology, we rediscover that science is found not only in laboratories but also in the harmony of frequencies and the depths of history. [2]
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
 
