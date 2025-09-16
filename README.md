# Half-Life Sentence Builder

This project is a Python utility that allows you to interactively merge multiple Half-Life `.wav` voice line files into a single output file, mimicking the **in-game sentence forming system** used by the HEV suit and NPCs.

In the original Half-Life, sentences like:

```
Power level is at 30 percent
```

were constructed by dynamically chaining together short audio clips (`power.wav`, `level.wav`, `is.wav`, `at.wav`, `30.wav`, `percent.wav`), with a short pause in between.

This tool re-creates that behavior offline with an **interactive prompt** that lets you select and order the clips you want. The resulting sentence is then exported as a standalone `.wav` file.

---

## Features

- Interactive prompt with **autocomplete** for available voice lines.
- Scans your chosen directory for `.wav` files automatically.
- Lets you type filenames without extensions (e.g. `power` instead of `power.wav`).
- Automatically inserts a **250 ms pause** between clips, matching Half-Life’s HEV suit pacing.
- Output file is named after the chosen clips, joined by underscores.  
  Example:  

  ```
  Input:  power, level, 30, percent
  Output: power_level_30_percent.wav
  ```

- Saves merged results into a dedicated `output/` subfolder so they don’t clutter your original audio files.

---

## Requirements

- **Python 3.8–3.12** (⚠️ `pydub` is not fully compatible with Python 3.13+ yet)
- [pydub](https://pypi.org/project/pydub/)
- [prompt_toolkit](https://pypi.org/project/prompt-toolkit/) (for autocomplete)
- [ffmpeg](https://ffmpeg.org/) (must be installed and in your system PATH)

Install dependencies with:

```bash
pip install pydub prompt_toolkit
```

---

## Usage

1. Place your Half-Life `.wav` voice lines in a folder.  
2. Open `sentence_builder.py` in a text editor and set:

   ```python
   wav_dir = r"C:\path\to\your\vox\folder"
   ```

   Replace with the path to your `vox` folder or any folder containing `.wav` clips.  

3. Run the script from a real console (cmd.exe, PowerShell, or Windows Terminal):

   ```bash
   python sentence_builder.py
   ```

4. Start typing filenames. Autocomplete will suggest available clips.  
   - Example: typing `po` then pressing **TAB** will complete to `power`.  
   - Press **ENTER** after each clip.  
   - Press **ENTER** on an empty line when you're finished.

5. The merged file will appear in the `output/` subfolder of your working directory.

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

When you run the script:

```
🎙️ Half-Life Voice Line Merger
Found wav files in C:\hl_vox:
power, level, is, at, 30, percent

Type filenames in order (press ENTER after each).
Press ENTER on an empty line when you're finished.

Add file: power
Add file: level
Add file: is
Add file: at
Add file: 30
Add file: percent
Add file:
```

The output file will be saved as:

```
C:\hl_vox\output\power_level_is_at_30_percent.wav
```

---

## Notes

- You can experiment with the pause duration if you want to replicate different pacing than the default 250 ms.  
- Works with any `.wav` files, but designed for Half-Life’s `vox/` voice system.  
- If autocomplete doesn’t work in your IDE (e.g. PyCharm), run the script from a **real console** (`cmd.exe` or PowerShell).  

---

## License

This project is provided as-is for educational and fan purposes.  
Half-Life and HEV suit voice assets are © Valve Software.
