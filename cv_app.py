import streamlit as st
from PIL import Image

st.set_page_config(page_title="CV - Rodrigo Huamán", page_icon="📄", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    try:
        image = Image.open("IMG_3422.JPG")
        st.image(image, width=180)
    except FileNotFoundError:
        st.warning("⚠️ No se encontró la imagen de perfil 'IMG_3422.JPG'.")

    st.markdown("## ✨ Rodrigo Huamán")
    st.markdown("""
📍 **Lima, Perú**  
📧 [huamanmaitarodrigoalonso@gmail.com](mailto:huamanmaitarodrigoalonso@gmail.com)  
📱 +51 960 678 127    
💻 [GitHub](https://github.com/rodrigo)  
📸 [Instagram](https://instagram.com/rdrigo_ah)
    """)
    st.markdown("---")
    st.markdown("🎯 *Apasionado por el cine, la cultura visual y el desarrollo digital(?).*")

# --- TÍTULO ---
st.title("📄 Curriculum Vitae – Rodrigo Huamán")

# --- TABS ---
tabs = st.tabs(["👤 Perfil", "🎓 Educación", "💼 Experiencia", "🛠️ Habilidades", "🚀 Proyectos", "📬 Contacto"])

# --- PERFIL ---
with tabs[0]:
    st.header("👤 Perfil Profesional")
    st.info("""
Soy un comunicador audiovisual con experiencia en análisis cinematográfico, estudios culturales, edición multimedia y fotografía. Me interesa expresar mi visión del mundo y sentir a través de distintos recursos audiovisuales.
""")

# --- EDUCACIÓN ---
with tabs[1]:
    st.header("🎓 Educación")
    st.markdown("""
**Pontificia Universidad Católica del Perú**  
📅 *2023 – Actualidad*  
🎥 *Licenciatura en Comunicación Audiovisual*
""")

# --- EXPERIENCIA ---
with tabs[2]:
    st.header("💼 Experiencia Profesional")
    st.markdown("""
### 🛰️ Covisan.S.A – Ejecutivo de Ventas  
📍 Lima | 🗓️ 2023 – 2024  
- Asesoría personalizada y venta de productos (internet, telefonía fija y TV).  
- Comunicación efectiva y resolución de necesidades del cliente.

### 🎥 Festival de cine AL ESTE – Asistente de Producción y Fotografía  
📍 Lima | 🗓️ 2025  
- Apoyo en preproducción, rodaje y postproducción.  
- Coordinación de equipo técnico y artístico en durante el festival.
""")

# --- HABILIDADES ---
with tabs[3]:
    st.header("🛠️ Habilidades")
    cols = st.columns(3)
    skills = [
        "🎞️ Edición de video (Premiere, Final Cut)",
        "🧠 Pensamiento crítico y análisis cultural",
        "🐍 Python y Streamlit",
        "🎨 Adobe Photoshop / Illustrator / Lightroom",
        "📊 Visualización de datos",
        "✍️ Redacción académica y ensayos"
    ]
    for i, skill in enumerate(skills):
        cols[i % 3].markdown(f"- {skill}")

# --- PROYECTOS ---
with tabs[4]:
    st.header("🚀 Proyectos Destacados")

    st.markdown("""
📽️ **Análisis de 'La boca del lobo'**  
Estudio crítico desde los Estudios Culturales sobre representación de la violencia en el cine peruano.

📊 **Análisis de Películas con Python**  
Sistema interactivo (Streamlit + Rotten Tomatoes) para analizar géneros, puntuaciones y tendencias globales.

📚 **Investigación sobre Cine Soviético**  
Proyecto académico sobre propaganda visual y construcción ideológica en el cine de Eisenstein y Vertov.

📸 **Proyectos en Instagram**  
Creación y divulgación de contenidos sobre cine.  
🔗 [Ver perfil completo en Instagram](https://www.instagram.com/funcioncineoficial/?hl=es-la#)

🖼️ **Post destacado:**  
""")

    # Imagen del post
    post_image = "IMG_3422.JPG"  # Reemplázala por otra si prefieres una diferente
    post_url = "https://www.instagram.com/p/DJ0gE6GtZSw/?hl=es-la&img_index=1"

    try:
        st.image(post_image, caption="Cultura visual y espacio urbano", use_container_width=True)
    except FileNotFoundError:
        st.warning("⚠️ No se encontró la imagen del post 'IMG_3422.JPG'.")

    st.markdown(f"<a href='{post_url}' target='_blank'>🔗 Ver este post en Instagram</a>", unsafe_allow_html=True)

# --- CONTACTO ---
with tabs[5]:
    st.header("📬 ¿Te interesa colaborar?")
    st.success("¡Contáctame! Estoy abierto a proyectos creativos, culturales o tecnológicos.")
    st.markdown("""
📧 [Envíame un correo](mailto:huamanmaitarodrigoalonso@gmail.com)    
📸 [Instagram](https://instagram.com/rdrigo_ah)
""")