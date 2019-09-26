from pydub import AudioSegment
from typing import List

def generate(files: List[str], out_fname: str, repetitions=3, silence_mult=1.1, silence_fix=200):
    audio = AudioSegment.empty()
    for file in files:
        orig = AudioSegment.from_file(file)
        silence_duration = len(orig) * silence_mult + silence_fix
        silence_audio = AudioSegment.silent(duration=silence_duration)

        audio += orig
        for _ in range(repetitions - 1):
            audio += silence_audio
            audio += orig

    audio.export(out_fname, format="mp3")

generate(["C:\\Cucu\\tmp\\2.mp3", "C:\\Cucu\\tmp\\4.mp3"], "C:\\Cucu\\tmp\\hey.mp3", repetitions=2)