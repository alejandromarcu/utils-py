from pydub import AudioSegment
from typing import List, Dict
from pathlib import Path
from random import shuffle

def find_files(paths: List[str], recursive=True) -> Dict[str, str]:
    def word_from_filename(fname: str) -> str:
        return "".join([ch for ch in fname.lower() if ch.isalpha() or ch == '-'])

    files = {}
    for path in paths:
        path_files = Path(path).glob("**/*.mp3") if recursive else Path(path).glob("*.mp3")
        files.update({word_from_filename(f.stem):str(f) for f in path_files})
   
    print("Read", len(files), "words")
    return files


def generate(files: List[str], out_fname: str, repetitions=3, silence_mult=1.1, silence_fix=400, start_fname=None, end_fname=None):
    audio = AudioSegment.empty()
    if start_fname:
        audio += AudioSegment.from_file(start_fname)

    for file in files:
        orig = AudioSegment.from_file(file)
        silence_duration = len(orig) * silence_mult + silence_fix
        silence_audio = AudioSegment.silent(duration=silence_duration)

        for _ in range(repetitions):
            audio += orig
            audio += silence_audio

    if end_fname:
        audio += AudioSegment.from_file(end_fname)

    audio.export(out_fname, format="mp3")

root = "C:\\Users\\Ale\\OneDrive\\Cucu\\Etc\\English\\Rachel's English\\words"
min_pairs = "C:\\Users\\Ale\\OneDrive\\Cucu\\Etc\\English\\Rachel's English\\minimal pairs"
word_to_file = find_files([root, min_pairs])

def render_module_with_slow(words, fname, repetitions_slow=2, repetitions=6):
    print(words)
    all = []
    for word in words:
        all.extend([word + "-slow"] * repetitions_slow)
        all.extend([word] * repetitions)

    render_module(all, fname, repetitions=1)

def render_module(words, fname, repetitions=4):
    print(", ".join(words))

    files = map(lambda w: word_to_file[w.lower()], words)
    start_fname, end_fname = word_to_file["startbell"], word_to_file["endbell"]
    generate(files, fname, repetitions=repetitions, start_fname=start_fname, end_fname=end_fname)


def module6():
    uh = ["cut", "done", "gun", "cup", "enough", "function", "funny", "husband", "love", "money", "month", "other", "oven", "public", "structure", "thump", "under"]
    ah = ["gone", "cop", "block", "body", "bottle", "bottom", "comment", "constant", "contest", "document", "father", "holidays", "impossible", "job", "model", "module", "occupation", "october", "operate", "option", "product", "robot", "stock"]
    aw = [ "caught", "dawn", "also", "alternate", "boss", "login", "long", "often", "small", "thought"]
    words = list(uh)
    words.extend(ah)
    words.extend(aw)
    shuffle(words)

    render_module(words, "module6.mp3")

def module8():
    words = ["action", "active", "actual", "after", "battery", "cash", "chapter", "exact", "fast", "graph", "hacker", "happen", "ration", "task", "track"] # aa 
    words.extend(["angle", "hang", "thanks", "exam", "man", "stand", "ban", "scam", "band", "ant", "jam", "stand"]) # aa + nasak
    words.extend(["address", "defend", "empty", "except", "excess", "invest", "preface", "present", "pressure", "pretend", "shelves", "special", "suggest", "unless", "weather", "wednesday", "yellow"]) # eh
    shuffle(words)

    render_module(words, "module8.mp3")

def module9():
    words = ["beach","busy","cheese","degree","exceed","feel","field","happy","here","peer","repeat","see","sheet","sleep","speed","teacher","wheel"] # ee
    words.extend(["activity","begin","build","contribute","convince","decision","description","equipment","fill","finish","indicate","internet","limit","list","office","printer","system","window","women"])
    shuffle(words)

    render_module(words, "module9.mp3")

def module10():
    words = ["alone", "cold", "code", "dont", "go", "home", "hotel", "load", "most", "okay", "only", "open", "over", "so", "total", "wont"]
    render_module_with_slow(words, "module10.mp3")

module10()