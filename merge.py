import os
from pydub import AudioSegment
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# ===== Settings =====
wav_dir = r"D:\Sounds\HEV"

# Scan directory for wav files
all_wavs = [f for f in os.listdir(wav_dir) if f.lower().endswith(".wav")]
if not all_wavs:
    raise FileNotFoundError(f"No .wav files found in {wav_dir}")

# Strip extensions for cleaner autocomplete
all_basenames = [os.path.splitext(f)[0] for f in all_wavs]

# Setup autocomplete
wav_completer = WordCompleter(all_basenames, ignore_case=True)

print("🎙️ Half-Life Voice Line Merger")
print(f"Found {len(all_basenames)} wav files in {wav_dir}:")
print(", ".join(all_basenames))
print("\nType filenames in order (press ENTER after each).")
print("Press ENTER on an empty line when you're finished.\n")

wav_files = []
while True:
    basename = prompt("Add file: ", completer=wav_completer).strip()
    if basename == "":
        break
    if basename in all_basenames:
        wav_files.append(basename + ".wav")
    else:
        print(f"⚠️ {basename} not found in directory.")

if not wav_files:
    raise ValueError("No files selected!")

# ===== Create output subfolder =====
output_dir = os.path.join(wav_dir, "output")
os.makedirs(output_dir, exist_ok=True)

# ===== Build output filename =====
names = [os.path.splitext(f)[0] for f in wav_files]
output_file = "_".join(names) + ".wav"
output_path = os.path.join(output_dir, output_file)

# ===== Merge processing =====
combined = AudioSegment.empty()
pause = AudioSegment.silent(duration=250)  # 250 ms pause

for i, wav in enumerate(wav_files):
    wav_path = os.path.join(wav_dir, wav)
    print(f"Adding {wav}...")
    sound = AudioSegment.from_wav(wav_path)
    combined += sound
    if i < len(wav_files) - 1:
        combined += pause

combined.export(output_path, format="wav")

print(f"\n✅ Merged file saved as {output_path}")
