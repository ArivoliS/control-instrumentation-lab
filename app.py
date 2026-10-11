"""EE3512 interactive lab, hosted with Streamlit; numerical models run in-browser."""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).resolve().parent
st.set_page_config(page_title="EE3512 Control and Instrumentation Lab", page_icon="📈", layout="wide")
st.title("EE3512 · Control and Instrumentation Virtual Lab")
st.caption("PSG Institute of Technology and Applied Research · Department of EEE · 2026–2027")
with st.expander("Manuals and help"):
    a, b = st.columns(2)
    for column, filename, label in [(a,"Lab_Manual.pdf","Download lab manual"),(b,"Front_Pages.pdf","Download front pages")]:
        file = BASE / filename
        if file.exists():
            column.download_button(label, data=file.read_bytes(), file_name=filename, mime="application/pdf")
    st.markdown("Select an experiment, adjust parameters and run the simulation. Use MATLAB & Simulink for script downloads. Use Notebook to save and export observations. Export records before leaving: browser storage may be restricted or cleared, especially in private browsing.")
    st.info("Browser numerical models are educational reference simulations. MATLAB/Simulink scripts require local software and appropriate toolboxes; actual real-time and hardware experiments need equipment. No student records are stored on the server.")
html_file = BASE / "lab.html"
if not html_file.exists():
    st.error("lab.html is missing. Upload all package files to the repository alongside app.py.")
    st.stop()
components.html(html_file.read_text(encoding="utf-8"), height=1650, scrolling=True)
