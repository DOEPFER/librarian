from pathlib import Path

description_file = Path(__file__).parent / "summarizer_description.md"
DESCRIPTION = description_file.read_text(encoding="utf-8")

instructions_file = Path(__file__).parent / "summarizer_instructions.md"
INSTRUCTIONS = instructions_file.read_text(encoding="utf-8")
