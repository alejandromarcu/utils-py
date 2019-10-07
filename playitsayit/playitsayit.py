from pydub import AudioSegment
from typing import List, Dict
from pathlib import Path
from random import shuffle

def find_files(paths: List[str], recursive=True) -> Dict[str, str]:
    def word_from_filename(fname: str) -> str:
        return "".join([ch for ch in fname.lower() if ch.isalpha()])

    files = {}
    for path in paths:
        path_files = Path(path).glob("**/*.mp3") if recursive else Path(path).glob("*.mp3")
        files.update({word_from_filename(f.stem):str(f) for f in path_files})
   
    return files


def generate(files: List[str], out_fname: str, repetitions=3, silence_mult=1.2, silence_fix=300):
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
min_pairs = "C:\\Users\\Ale\\OneDrive\\Cucu\\Etc\\English\\Rachel's English\\minimal pairs"
word_to_file = find_files([root, min_pairs])

#words = ["sure", "tatter", "Admire"]
#files = map(lambda w: word_to_file[w.lower()], words)
#generate(files, "test.mp3")

def module6():
    uh = ["cut", "done", "gun", "cup", "enough", "function", "funny", "husband", "love", "money", "month", "other", "oven", "public", "structure", "thump", "under"]
    ah = ["gone", "cop", "block", "body", "bottle", "bottom", "comment", "constant", "contest", "document", "father", "holidays", "impossible", "job", "model", "module", "occupation", "october", "operate", "option", "product", "robot", "stock"]
    aw = [ "caught", "dawn", "also", "alternate", "boss", "login", "long", "often", "small", "thought"]
    words = list(uh)
    words.extend(ah)
    words.extend(aw)
    shuffle(words)

    files = map(lambda w: word_to_file[w.lower()], words)
    generate(files, "module6.mp3", repetitions=4)

module6()

