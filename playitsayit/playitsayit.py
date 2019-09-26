from pydub import AudioSegment
from typing import List, Dict
from pathlib import Path

def find_files(paths: List[str], recursive=True) -> Dict[str, str]:
    files = {}
    for path in paths:
        path_files = Path(path).glob("**/*.mp3") if recursive else Path(path).glob("*.mp3")
        files.update({f.stem.lower():str(f) for f in path_files})
   
    return files


def generate(files: List[str], out_fname: str, repetitions=3, silence_mult=1.1, silence_fix=200):
    audio = AudioSegment.empty()
    for file in files:
        orig = AudioSegment.from_file(file)
        silence_duration = len(orig) * silence_mult + silence_fix
        silence_audio = AudioSegment.silent(duration=silence_duration)

        for _ in range(repetitions):
            audio += orig
            audio += silence_audio

    audio.export(out_fname, format="mp3")

root = "C:\\Users\\Ale\\OneDrive\\Cucu\\Etc\\English\\Rachel's English\\words"
word_to_file = find_files([root])

words = ["sure", "tatter", "Admire"]

files = map(lambda w: word_to_file[w.lower()], words)

generate(files, "test.mp3")

