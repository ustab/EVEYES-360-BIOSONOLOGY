import streamlit as st
import pandas as pd
import numpy as np
import time

# --- SAYFA 1: ANA EKRAN ---


# --- SAYFA 1: ANA EKRAN ---
# EVEYES 360 Ayarları [cite: 2026-01-14]

if sayfa == "Ana Ekran":
    st.title(f"🚀 Hoş Geldiniz - {dil}")
    st.write("Abuja 16 Ocak 2026 - Sistem Aktif")
    st.image("https://via.placeholder.com/800x200.png?text=EVEYES+360+Biosonology+Dashboard", use_container_width=True)
    st.set_page_config(page_title="EVEYES 360 - Biosonology", layout="wide")
    st.sidebar.title("💠 EVEYES 360-BIOSONOLOGY")
    dil = st.sidebar.selectbox("Dil Seçiniz", ["Türkçe", "English", "Français"])
    sayfa = st.sidebar.radio("Menü", ["Ana Ekran", "Bilimsel Makale & Frekans", "🔬 Biosonology Analiz", "📊 Bilimsel Veriler"])
    st.balloons()
    msg = st.text_input("Düşünceni Yaz:")
    if st.button("Sisteme Gönder"):
        with st.spinner('Veri şifreleniyor...'):
            time.sleep(1)
            st.success("Gönderi EVEYES-360-BIOSONOLOY veritabanına işlendi!")

elif sayfa == "📊 Bilimsel Analiz (Makale)":
    st.title("📄 Bilimsel Makale ve Frekans Verileri")
    st.markdown("### Selçuklu Tıbbı ve Biosonoloji")

    # Canlı Grafik Fonksiyonu
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Rast Makamı', 'Rehavi Makamı'])
    st.line_chart(chart_data)

    # Selçuklu ve Biosonoloji Tablosu
    data = {
        "Makam": ["Rast", "Rehavi", "Hicaz"],
        "Etki Alanı": ["Göz/Kemik", "Sinir Sistemi", "Kalp/Kan"],
        "Frekans (Hz)": ["432 Hz", "528 Hz", "396 Hz"]
    }
    st.table(pd.DataFrame(data)) 

# --- SAYFA 2: BIOSONOLOGY ANALİZ (DESİBEL GİRİŞİ) ---
elif sayfa == "🔬 Biosonology Analiz":
    st.title("🔬 Hücresel Ses ve Desibel Analizi")
    st.markdown("Hücreden gelen sonik veriyi (dB) girerek biyosonolojik durumu analiz edin.")

    col1, col2 = st.columns(2)
    
    with col1:
        # Kullanıcıdan Desibel Girişi Alıyoruz
        db_degeri = st.number_input("Hücre Desibel Değeri (dB):", min_value=0, max_value=120, value=45)
        
        if st.button("Analiz Et"):
            with st.spinner('Frekanslar Selçuklu Arşiviyle Eşleştiriliyor...'):
                time.sleep(1.5)
                
                if db_degeri < 30:
                    st.warning("⚠️ Düşük Rezonans: Hücre enerjisi zayıf. Rehavi Makamı önerilir.")
                elif 30 <= db_degeri <= 60:
                    st.success("✅ Dengeli Rezonans: Hücre sağlıklı titreşiyor. Rast Makamı ile desteklenebilir.")
                else:
                    st.error("🚨 Yüksek Stres: Hücrede termal stres belirtisi. Hicaz Makamı ile yatıştırılmalı.")

    with col2:
        # Canlı Dalga Formu Simülasyonu
        st.subheader("🔊 Anlık Sonik Dalga")
        chart_data = pd.DataFrame(np.sin(np.linspace(0, 10, 100) * (db_degeri/10)), columns=['Hücre Sesi'])
        st.line_chart(chart_data)

# --- SAYFA 3: BİLİMSEL VERİLER (MAKALE) ---

"""# 3. app.py dosyasını BİLİMSEL TABLO VE HAREKETLİ GRAFİKLE yeniden yazalım
with open('app.py', 'w', encoding='utf-8') as f:
    f.write("""
import streamlit as st
import pandas as pd
import numpy as np
import time
st.set_page_config(page_title="EVEYES 360 - Canlı Portal", layout="wide")

if sayfa == "Bilimsel Makale & Frekans":
   st.title("📄 Selçuklu Tıbbı & Biosonoloji Makale Verileri")
   st.markdown("""
    **Özet:** Seslerin canlı hücreler üzerindeki etkileri, biosonoloji verileri ve Selçuklu dönemi müzik 
    psikoterapisi arasındaki bağlar programın temelini oluşturur. [cite: 2026-01-15]
    """)

    # Bilimsel Tablo 
data = {
        "Selçuklu Makamı": ["Rast", "Rehavi", "Hicaz", "Uşşak"],
        "Etkilenmiş Hücre": ["Göz", "Nöronlar", "Ürogenital", "Kalp"],
        "Frekans (Hz)": ["432 Hz", "528 Hz", "396 Hz", "528 Hz"],
        "Modern Tıp Etkisi": ["Yatıştırıcı", "DNA Onarımı", "Stres Azaltıcı", "Yenilenme"]
    }
st.table(pd.DataFrame(data)) # Profesyonel tablo görünümü

    # HAREKET BURADA: Canlı Frekans Grafiği
st.subheader("📊 Canlı Hücresel Rezonans Grafiği")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Rast', 'Rehavi', 'Hicaz'])
st.line_chart(chart_data)
st.caption("Selçuklu makamlarının anlık biosonolojik frekans çıktıları simüle ediliyor.")

#!streamlit run app.py & npx localtunnel --port 8501

with open('app.py', 'w', encoding='utf-8') as f:
    f.write("""
import streamlit as st
import pandas as pd
import numpy as np""")

# EVEYES 360 Ayarları
st.set_page_config(page_title="EVEYES 360 Portal", layout="wide")

# 4. IP Adresini Göster ve Başlat
print("\n" + "="*50)
print("SİTE ŞİFRESİ (ENDPOINT IP):")
#curl ipv4.icanhazip.com
print("="*50 + "\n")

# Uygulamayı Başlat
#streamlit run app.py & npx localtunnel --port 8501
