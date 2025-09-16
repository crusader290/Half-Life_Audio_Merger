# Half-Life Voice Line Merger

This project is a small Python utility that allows you to merge multiple Half-Life `.wav` voice line files into a single output file, mimicking the **in-game sentence forming system** used by the HEV suit and NPCs.

In the original Half-Life, sentences like:

```
Power level is at 30 percent
```

were constructed by dynamically chaining together short audio clips (`power.wav`, `level.wav`, `is.wav`, `at.wav`, `30.wav`, `percent.wav`), with a short pause in between.

This script re-creates that behavior offline, letting you build complete sentences or announcements and save them as standalone `.wav` files.

---

## Features

- Merge multiple `.wav` files into one continuous file.
- Automatically inserts a **250 ms pause** between clips to match the pacing of the Half-Life HEV suit.
- Output file is named after the input clips, joined by underscores.  
  Example:  

  ```
  Input:  ["power.wav", "level.wav", "30.wav", "percent.wav"]
  Output: power_level_30_percent.wav
  ```

- Saves all merged results into a dedicated `output/` subfolder so they don’t clutter your source audio files.

---

## Requirements

- **Python 3.8+**
- [pydub](https://pypi.org/project/pydub/)
- [ffmpeg](https://ffmpeg.org/) (must be installed and in your system PATH)

Install dependencies with:

```bash
pip install pydub
```

---

## Usage

1. Place your Half-Life `.wav` voice lines in a folder.  
2. Edit the script:
   - Set `wav_dir` to the folder containing your `.wav` files.
   - List the filenames (in order) in the `wav_files` list.  
3. Run the script:

```bash
python merge_vox.py
```

4. The merged file will appear in the `output/` subfolder.

---

## Example

Suppose your working directory contains:

```
C:\hl_vox\
    power.wav
    level.wav
    is.wav
    at.wav
    30.wav
    percent.wav
```

With this script configuration:

```python
wav_dir = r"C:\hl_vox"
wav_files = ["power.wav", "level.wav", "is.wav", "at.wav", "30.wav", "percent.wav"]
```

The output will be:

```
C:\hl_vox\output\power_level_is_at_30_percent.wav
```

---

## Notes

- You can experiment with the pause duration if you want to replicate different pacing than the default 250 ms.  
- Works with any `.wav` files, but intended for Half-Life’s `vox/` lines.

---

## License

This project is provided as-is for educational and fan purposes.  
Half-Life and HEV suit voice assets are © Valve Software.
