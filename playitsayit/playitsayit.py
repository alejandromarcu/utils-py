from pydub import AudioSegment
from typing import List, Dict
from pathlib import Path
from random import shuffle

def find_files(paths: List[str], recursive=True) -> Dict[str, str]:
    def word_from_filename(fname: str) -> str:
        word = "".join([ch for ch in fname.lower() if ch.isalpha() or ch == '-'])
        # if it starts with -, probably it had a number before, so just remove it
        return word[1:] if word[0] == "-" else word 

    files = {}
    for path in paths:
        path_files = Path(path).glob("**/*.mp3") if recursive else Path(path).glob("*.mp3")
        files.update({word_from_filename(f.stem):str(f) for f in path_files})
   
    print("Read", len(files), "words")
    return files


def generate(files: List[str], out_fname: str, repetitions=3, silence_mult=1.1, silence_fix=400, start_fname=None, end_fname=None, tags=None):
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

    audio.export(out_fname, format="mp3", tags=tags)

root = "C:\\Users\\Ale\\OneDrive\\Cucu\\Etc\\English\\Rachel's English\\words"
min_pairs = "C:\\Users\\Ale\\OneDrive\\Cucu\\Etc\\English\\Rachel's English\\minimal pairs"
modules = "C:\\Users\\Ale\\OneDrive\\Cucu\\Etc\\English\\Rachel's English\\modules"
word_to_file = find_files([root, min_pairs, modules])

def render_module_with_slow(words, module_number, repetitions_slow=2, repetitions=6):
    print(words)
    all = []
    for word in words:
        all.extend([word + "-slow"] * repetitions_slow)
        all.extend([word] * repetitions)

    render_module(all, module_number, repetitions=1)

def render_module(words, module_number, repetitions=4):
    print(", ".join(words))

    files = map(lambda w: word_to_file[w.lower()], words)
    start_fname, end_fname = word_to_file["startbell"], word_to_file["endbell"]
    tags = {"title": f"My module {module_number} words", "album": "Rachel's English", "artist": "Rachel's English"}
    fname = f"module{module_number}.mp3"
    generate(files, fname, repetitions=repetitions, start_fname=start_fname, end_fname=end_fname, tags=tags)


def module6():
    uh = ["cut", "done", "gun", "cup", "enough", "function", "funny", "husband", "love", "money", "month", "other", "oven", "public", "structure", "thump", "under"]
    ah = ["gone", "cop", "block", "body", "bottle", "bottom", "comment", "constant", "contest", "document", "father", "holidays", "impossible", "job", "model", "module", "occupation", "october", "operate", "option", "product", "robot", "stock"]
    aw = [ "caught", "dawn", "also", "alternate", "boss", "login", "long", "often", "small", "thought"]
    words = list(uh)
    words.extend(ah)
    words.extend(aw)
    shuffle(words)

    render_module(words, 6)

def module8():
    words = ["action", "active", "actual", "after", "battery", "cash", "chapter", "exact", "fast", "graph", "hacker", "happen", "ration", "task", "track"] # aa 
    words.extend(["angle", "hang", "thanks", "exam", "man", "stand", "ban", "scam", "band", "ant", "jam", "stand"]) # aa + nasak
    words.extend(["address", "defend", "empty", "except", "excess", "invest", "preface", "present", "pressure", "pretend", "shelves", "special", "suggest", "unless", "weather", "wednesday", "yellow"]) # eh
    shuffle(words)

    render_module(words, 8)

def module9():
    words = ["beach","busy","cheese","degree","exceed","feel","field","happy","here","peer","repeat","see","sheet","sleep","speed","teacher","wheel"] # ee
    words.extend(["activity","begin","build","contribute","convince","decision","description","equipment","fill","finish","indicate","internet","limit","list","office","printer","system","window","women"])
    shuffle(words)

    render_module(words, 9)

def module10():
    words = ["alone", "cold", "code", "dont", "go", "home", "hotel", "load", "most", "okay", "only", "open", "over", "so", "total", "wont"]
    render_module_with_slow(words, 10)

def module19():
    N = 10
    words = ["notebook-stressed", "notebook-unstressed"] * N
    words += ["skateboard-stressed", "skateboard-unstressed"] * N
    words += ["backbone-stressed", "backbone-unstressed"] * N
    words += ["touchdown-stressed", "touchdown-unstressed"] * N
    words += ["weekend-stressed", "weekend-unstressed"] * N
    words += ["toothpaste-stressed", "toothpaste-unstressed"] * N
    words += ["download-stressed", "download-unstressed"] * N
    words += ["bookmark-stressed", "bookmark-unstressed"] * N
    words += ["lifetime-stressed", "lifetime-unstressed"] * N
    words += ["headquarters-stressed", "headquarters-unstressed"] * N

    render_module(words, 19, repetitions=1)

module19()