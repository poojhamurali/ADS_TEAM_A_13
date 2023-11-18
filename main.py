import streamlit as st
from midi_generation import generate  # Assuming the MIDI generation code is in a module named midi_generator
import base64

# Function to generate MIDI file and save it
def generate_midi():
    generate()

def main():
    st.markdown(
        """
        <style>
            body {
                background-color: #f2f2f2;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .center {
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h1 class='center' style='color: #004080; font-size: 48px;'>🎵 Piano Music Generator 🎵</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='center'>",
        unsafe_allow_html=True,
    )

    if st.button("Generate Music", key="generate_button"):
        with st.spinner("Generating Music... Please wait."):
            generate_midi()
        st.balloons()  # Display balloons after generating music
        st.success("Music file generated successfully!")

    midi_file_path = 'test_output.mid'  # Update with your actual file path
    if st.button("Download Music"):
        st.text("Enjoy the music by clicking the below link ")

        st.markdown(
            f"<a href='data:application/octet-stream;base64,{base64.b64encode(open(midi_file_path, 'rb').read()).decode()}' download='output.mid'>Download Music</a>",
            unsafe_allow_html=True
        )

        st.success("Download complete!")

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p class='center' style='font-size: 28px; color: #006699;'>🎶 Enjoy the magical tunes! 🎶</p>",
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
