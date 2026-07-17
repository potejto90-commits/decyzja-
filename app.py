import streamlit as st

st.set_page_config(page_title="Model Decyzyjny", layout="wide")
st.title("Model Decyzyjny: Miłość vs Ryzyko")

# --- SUWAKI ---
col1, col2, col3 = st.columns(3)
with col1:
    v_obecna = st.slider("Wartość: Zostaje z obecną", -100, 100, 40)
    v_samotnosc = st.slider("Wartość: Ręka w nocniku", -100, 100, -50)
with col2:
    p_chce = st.slider("Szansa: Nowa chce (0-100%)", 0, 100, 40) / 100
    p_lepsza = st.slider("Szansa: Nowa lepsza (0-100%)", 0, 100, 60) / 100
    v_nowa_L = st.slider("Wartość: Nowa jest LEPSZA", -100, 100, 90)
    v_nowa_G = st.slider("Wartość: Nowa jest GORSZA", -100, 100, 20)
with col3:
    p_dowie = st.slider("Szansa: Obecna się dowie (0-100%)", 0, 100, 70) / 100
    p_oleje = st.slider("Szansa: Po wpadce oleje (0-100%)", 0, 100, 50) / 100
    v_total_wtopa = st.slider("Wartość: Totalna wtopa", -100, 100, -100)
    v_powrot = st.slider("Wartość: Cichy powrót", -100, 100, 35)

# --- MATEMATYKA ---
ev_zostaje = v_obecna
ev_zrywa = p_chce * (p_lepsza * v_nowa_L + (1-p_lepsza) * v_nowa_G) + (1-p_chce) * v_samotnosc
ev_zagaduje = p_dowie * (p_oleje * v_total_wtopa + (1-p_oleje) * 0) + (1-p_dowie) * v_powrot 

# --- WYNIKI ---
k1, k2, k3 = st.columns(3)
k1.metric("EV: Zostaje", round(ev_zostaje, 1))
k2.metric("EV: Zerwij", round(ev_zrywa, 1))
k3.metric("EV: Po cichu", round(ev_zagaduje, 1))
