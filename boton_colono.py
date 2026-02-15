"""
📱 BOTÓN PLUMA - PARA EL CEL DEL COLONO
Versión conectada a Cloudflare Tunnel
"""

import streamlit as st
import requests
import time

st.set_page_config(
    page_title="🚗 Abrir Pluma",
    page_icon="🚗",
    layout="centered"
)

# ================================
# URL DEL SERVIDOR (GUARDIA)
# ================================
URL_SERVIDOR = "https://powerpoint-holiday-payday-anymore.trycloudflare.com/abrir"

# ================================
# PARAMETROS PERSONALIZADOS
# ================================
params = st.query_params
nombre = params.get('name', 'Colono')
qr = params.get('qr', 'QR001')

if 'abriendo' not in st.session_state:
    st.session_state.abriendo = False

# ================================
# CSS BOTÓN GRANDE
# ================================
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        height: 300px;
        font-size: 60px !important;
        border-radius: 30px;
        background: linear-gradient(145deg, #27ae60, #2ecc71);
        color: white;
        border: none;
        box-shadow: 0 15px 40px rgba(39, 174, 96, 0.4);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 20px 50px rgba(39, 174, 96, 0.5);
    }
    .header {
        text-align: center;
        padding: 25px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
    }
    .success-box {
        text-align: center;
        padding: 60px;
        background: linear-gradient(145deg, #f39c12, #e67e22);
        border-radius: 30px;
        color: white;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ================================
# HEADER
# ================================
st.markdown(f"""
<div class="header">
    <h1>🏠 PORTÓN GIRASOLES</h1>
    <h2>👤 {nombre}</h2>
</div>
""", unsafe_allow_html=True)

# ================================
# BOTÓN
# ================================
if st.session_state.abriendo:

    st.markdown("""
    <div class="success-box">
        <h1 style="font-size: 100px;">🚗 ✅</h1>
        <h2>¡PLUMA ABIERTA!</h2>
        <p>Pase por favor...</p>
    </div>
    """, unsafe_allow_html=True)

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.session_state.abriendo = False
    st.rerun()

else:

    if st.button("🚗\nABRIR\nPLUMA"):

        try:
            response = requests.post(
                URL_SERVIDOR,
                json={
                    "name": nombre,
                    "qr": qr
                },
                timeout=5
            )

            if response.status_code == 200:
                st.session_state.abriendo = True
                st.rerun()
            else:
                st.error(f"❌ Error del servidor: {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("❌ No se pudo conectar con el servidor del guardia")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
