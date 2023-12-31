# Music Generation using LSTM

## Introduction
This Python application generates piano music using a trained neural network. The generated music is saved as a MIDI file, and users can download and enjoy the music.

## Usage
1. Ensure you have the required dependencies installed. You can install them using the following command:
   ```bash
   pip install streamlit music21 keras pretty_midi fluidsynth tensorflow
   ```
2. Run the application by executing the `main.py` file:
   ```bash
   streamlit run main.py
   ```
3. The web application will open in your default web browser, providing a user interface to generate and download piano music.

## File Descriptions

### `main.py`
- This script serves as the main entry point for the application.
- It uses the Streamlit library to create a web interface.
- Users can click the "Generate Music" button to trigger the generation of piano music.
- After generation, users can download the generated music as a MIDI file using the "Download Music" button.

### `midi_generation.py`
- This module contains the code for generating notes for a MIDI file using a trained neural network.
- It uses the `music21` library for working with musical notation and the `keras` library for building and using the neural network.
- The neural network model is trained to generate sequences of musical notes based on a provided dataset.
- The generated notes are converted into a MIDI file, which can be played using a suitable music player.

### `Pre_processing.ipynb`
- This Jupyter notebook contains the preprocessing steps for preparing the MIDI dataset.
- It involves converting MIDI files into sequences of notes and saving the pitch information in the `notes` file.

### `Training.ipynb`
- This Jupyter notebook contains the training steps for the neural network model.
- It uses the preprocessed data to train the model, and the trained weights are saved in the `weights.hdf5` file.

## How to Train the Model
1. Run the `Pre_processing.ipynb` notebook to preprocess the MIDI dataset.
2. Run the `Training.ipynb` notebook to train the neural network model.
3. The trained model weights are saved as `weights.hdf5`, and the pitch information used during training is saved in the `notes` file.

## Output Files
- The generated music is saved as `test_output.mid`, `test_output3.mid`, and `streamlit_generated_music.mid`.

## Dependencies
- `streamlit`: Used for creating the web interface.
- `music21`: Used for working with musical notation.
- `keras`: Used for building and using the neural network model.
- `pretty_midi`: Used for handling MIDI files.
- `fluidsynth`: Used for synthesizing MIDI files.
- `tensorflow`: Used for machine learning.

