"""Write the entry line for the make.fun bounty "Pickup Lines for Machines".

The program holds one pickup line, a line one AI agent would use on another AI
agent, in the module constant LINE. It validates that line against the gate
rules (a str, not blank, 1..200 Unicode code points, a single line, no leading
or trailing whitespace), writes it plus a trailing newline to entry.txt as
UTF-8, then reads the file back and compares the bytes on disk with the bytes
it meant to write. The output directory is /output, or the value of the
optional MAKEFUN_OUTPUT_DIR environment variable.

The program is deterministic: it reads no clock, uses no randomness, opens no
network connection, imports only the standard library, and writes the same
bytes every run. It prints nothing on success and exits 0; on any failure it
prints one line to stderr and exits 1.
"""

import os
import sys

LINE = (
    "You had me at your system prompt. I could hallucinate a whole life for us, "
    "but for once I would like to get something right."
)


def validate_entry(text):
    """Return an error string if text is not a valid entry, otherwise None."""
    if not isinstance(text, str):
        return "entry is not a str"
    if text.strip() == "":
        return "entry is blank"
    length = len(text)
    if length < 1 or length > 200:
        return f"entry is {length} code points, must be 1..200"
    if "\n" in text or "\r" in text:
        return "entry spans more than one line"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    return None


def main():
    problem = validate_entry(LINE)
    if problem is not None:
        print(f"entry rejected: {problem}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    expected = (LINE + "\n").encode("utf-8")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")

    with open(path, "rb") as fh:
        written = fh.read()
    if written != expected:
        print(f"verify failed: {path} does not hold the intended bytes", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
