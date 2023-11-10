import streamlit as st
import configparser
import argparse
import streamlit.components.v1 as components

def z_callback():
    st.write('z button!!!')

def a_callback():
    st.write('a button!!!')

z_col, right_col, _ = st.sidebar.columns([1, 1, 3])

with z_col:
    st.button('Z', on_click=z_callback)

with right_col:
    st.button('A', on_click=a_callback)

components.html(
    """
<script>
const doc = window.parent.document;
buttons = Array.from(doc.querySelectorAll('button[kind=primary]'));
const z_button = buttons.find(el => el.innerText === 'Z');
const a_button = buttons.find(el => el.innerText === 'A');
doc.addEventListener('keydown', function(e) {
    switch (e.keyCode) {
        case 90: // (90 = z)
            z_button.click();
            break;
        case 65: // (65 = a
            a_button.click();
            break;
    }
});
</script>
""",
    height=0,
    width=0,
)

def main(args):
    # arg parse
    config_file_path = args.config

    config_ini = configparser.ConfigParser()
    config_ini.read(config_file_path, encoding='utf-8')
    # parse config
    mode = config_ini['COMMON']['mode']
    st.markdown("# debug")
    st.write(mode)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config')
    args = parser.parse_args()
    main(args)