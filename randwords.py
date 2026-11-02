#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Choose unique random French words from the bundled dictionary."""
import argparse
from pathlib import Path
import secrets

DEFAULT_DICTIONARY = Path(__file__).resolve().parent / "listfr.txt"

def choose_words(path: Path, count: int = 4) -> list[str]:
    if isinstance(count, bool) or not isinstance(count, int) or count < 1:
        raise ValueError("Count must be a positive integer")
    words = list(dict.fromkeys(word.strip() for word in path.read_text(encoding="utf-8-sig").splitlines() if word.strip()))
    if len(words) < count:
        raise ValueError(f"Dictionary has {len(words)} distinct words; {count} requested")
    return secrets.SystemRandom().sample(words, count)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", help="Name to greet; prompts if omitted")
    parser.add_argument("--count", type=int, default=4)
    parser.add_argument("--dictionary", type=Path, default=DEFAULT_DICTIONARY)
    args = parser.parse_args()
    name = args.name if args.name is not None else input("Entrez votre nom ici : ")
    try:
        words = choose_words(args.dictionary, args.count)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))
    print(f"{name}, tes mots sont :\n" + "\n".join(words))

if __name__ == "__main__":
    main()
