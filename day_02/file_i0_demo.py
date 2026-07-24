# ============================================================
# file_io_demo.py
# Concept: reading and writing files — how data survives after
#          your program stops running
# ============================================================
log_entries = [
    "Day 2 started",
    "Functions section complete",
    "Comprehensions section complete",
]
# --- Writing to a file ---
# "w" mode means "write": creates the file if it doesn't exist, or
# OVERWRITES it if it does. Use "a" (append) to add without erasing.
with open("progress_log.txt", "w") as f:
    for entry in log_entries:
        f.write(entry + "\n")   # \n adds a line break after each entry
# 'with' automatically closes the file when this block ends, even if
# an error happens partway through — always prefer it over manually
# calling f.close().
# --- Reading the file back ---
with open("progress_log.txt", "r") as f:
    contents = f.read()
print("File contents:")
print(contents)