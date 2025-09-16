from pydub import AudioSegment
import os

# ===== Settings =====
# List your wav files in order
wav_files = [
    "part1.wav",
    "part2.wav",
    "part3.wav"
]

# ===== Build output filename from input names =====
names = [os.path.splitext(os.path.basename(w))[0] for w in wav_files]
output_file = "_".join(names) + ".wav"

# ===== Processing =====
combined = AudioSegment.empty()
pause = AudioSegment.silent(duration=250)  # 250 ms pause

for i, wav in enumerate(wav_files):
    if os.path.exists(wav):
        print(f"Adding {wav}...")
        sound = AudioSegment.from_wav(wav)
        combined += sound
        if i < len(wav_files) - 1:  # don't add pause after last file
            combined += pause
    else:
        print(f"⚠️ File not found: {wav}")

# Export the result
combined.export(output_file, format="wav")

print(f"✅ Merged file saved as {output_file}")
