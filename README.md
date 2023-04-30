# Ted-Talk_Scraper

## Setup Environment
This is to create the SpeechToTextVenv folder in this repo if you don't have it already. You must delete the old folder before running this.

```bash
$ setup_venv.bat
```

## Run Model (Not Complete)
This is to run the sr_script.py file which lets you feed in audio for the model to predict text. Currently this doesn't work in real time since we have trouble setting up our environment to grab audio input device without using anaconda or a virtual machine (Ubuntu)

```bash
$ run_script.bat
```

## Testing the Model
Running this python script and passing in a wav file will print the transcription that the model output. All our wav files are in the output_files folder. Change the 

Run this with the current working directory in the github repository.
```bash
$ SpeechToTextVenv\Scripts\activate
$ python .\sr_script.py "output_files\2007-david-gallo-006-5000k\output_0.wav"
```
