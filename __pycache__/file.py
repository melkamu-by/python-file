tx=open("firstfile.txt","w")
tx.write("""File handling refers to how a program creates, reads, writes, updates, and deletes files stored on a computer's disk.
 It's a core concept in programming used any time your code needs to work with data that lives outside the program itself — like 
           -text files
           -logs
           - configuration files
           -images, or CSVs.

**Core operations:**

1. **Opening a file** -> establishing a connection between your program and a file on disk, usually specifying a mode (read, write, append, etc.)
2. **Reading** -> pulling data from a file into your program
3. **Writing** ->sending data from your program into a file (this can overwrite existing content or add to it)
4. **Appending** -> adding new data to the end of a file without erasing what's already there
5. **Closing** -> releasing the file so other programs (or parts of your own program) can use it, and making sure all data is properly saved

**Common file modes** (these show up in most languages):
- `r` -> read only
- `w` -> write (overwrites existing content)
- `a` -> append (adds to the end)
- `r+` / `w+` -> read and write combined
- `b` -> binary mode (for non-text files like images)

**Example in Python:**
```python
# Writing to a file
with open("notes.txt", "w") as f:
    f.write("Hello, world!")

# Reading from a file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
```

The `with` statement here automatically closes the file when you're done, which is good practice — it prevents "file left open" bugs and data corruption.

**Why it matters:**
- Persisting data between program runs (a program's variables disappear when it stops, but files stick around)
- Processing large datasets that can't fit fully in memory
- Logging and debugging
- Configuration management (like `.env` or `.json` config files)
- Exchanging data between programs or systems

**Things to watch out for:**
- **File not found errors** ->trying to read a file that doesn't exist
- **Permission errors** -> lacking rights to read/write a file
- **Encoding issues** -> especially with text containing special characters (UTF-8 vs. ASCII, etc.)
- **Leaving files open** -> can lock resources or lose unsaved data if the program crashes
""")
tx.close()
tx=open("firstfile.txt","r")
file=tx.read
print(file)
tx.close()