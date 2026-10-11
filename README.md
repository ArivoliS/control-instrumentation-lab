# EE3512 Control and Instrumentation Virtual Lab

Prepared for Dr. Arivoli S, Department of EEE, PSG iTech.

## GitHub → Streamlit deployment

1. Extract this ZIP. Upload the FILES INSIDE the extracted folder, not the ZIP.
2. Sign in to https://github.com and create a new public repository named `control-instrumentation-lab`. Use a new repository so your Engineering Skills Lab remains separate.
3. Choose Add file → Upload files. Drag app.py, requirements.txt, lab.html, both PDFs and this README into the repository root. Commit changes.
4. Open https://share.streamlit.io and sign in with GitHub. Authorize repository access if requested.
5. Choose Create app → deploy from GitHub. Select the new repository, branch main, main file path app.py. Select Python 3.12 in advanced settings if a version selector is shown.
6. Choose an available URL such as psg-control-instrumentation-lab, then click Deploy.
7. Wait until the app opens. Copy the actual URL returned by Streamlit, ending in .streamlit.app.
8. Check sharing/access settings and choose public access if needed. Test the link in a private/incognito window before giving it to students.

Repository root should contain app.py, requirements.txt, lab.html, Lab_Manual.pdf, Front_Pages.pdf, README.md.

## Run locally on Windows (optional)

Install Python 3.12 from python.org and enable Add Python to PATH. Open Command Prompt inside the extracted folder, then run:

    python -m pip install -r requirements.txt
    python -m streamlit run app.py

## Use

The Streamlit Python app embeds a self-contained HTML/JavaScript workbench. No external numerical server or MATLAB runtime is needed for browser simulations. MATLAB script downloads and Simulink builders are supplied for separate local use. All 13 manual experiment headings and two mini-project references are included. Default mathematical models are educational examples; consult the supplied manual for assigned values.

Notebook records use browser storage where supported; they are not collected centrally or sent to faculty. Export readable HTML or JSON and submit through your institution's chosen channel. Import previously exported JSON from the Notebook tab. Export before closing the app or changing devices.

MATLAB and Simulink scripts have not been executed in MATLAB in the authoring environment. Hardware and real-time models are reference simulations only. Root locus browser output shows poles for the selected gain; the downloaded MATLAB script produces the full root locus. Frequency response browser plot shows magnitude; CSV also contains phase. Discrete-domain Kalman tests are available in the MATLAB script.

## Troubleshooting

- ModuleNotFoundError: confirm requirements.txt is at repository root.
- Missing lab.html: upload lab.html next to app.py.
- App file not found: main file path must be app.py when uploaded at root.
- If the app is inside a folder, use folder-name/app.py as the main file path.
- Blank lab: enable JavaScript and check whether your browser blocks embedded frames. Try another browser.
- Download blocked: allow downloads for the app and click again.
- Export records regularly; iframe browser storage availability varies.

Official deployment guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
