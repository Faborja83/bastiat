"""Marker scan across Bastiat's Œuvres complètes (Guillaumin, 7 vols.).

Counts word-bounded markers of the candidate traditions (Masonic, Illuminist/
theosophical, alchemical/Hermetic, magnetism) and of the Christian-providential
register, per volume. With --kwic, also prints every hit in context so that
each count can be checked by hand. Most raw hits are ordinary words
(maçon = mason by trade, hermétiquement, colimaçon); see
other_writings.md for the hand-checked readings.

Usage: python3 oeuvres_marker_scan.py [--kwic]
"""
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "sources" / "bastiat_oeuvres_completes"
VOLS = [f"OC{i}.txt" for i in range(1, 8)]

MARKERS = {
    # Masonic
    "franc-maçon*": r"franc-?ma[çc]on",
    "maçon (any)": r"\bma[çc]on",
    "loge(s)": r"\bloges?\b",
    "vénérable": r"\bv[ée]n[ée]rable",
    "grand orient": r"grand[- ]orient",
    "écossais(e)": r"\b[ée]cossaise?s?\b",
    # Illuminist / theosophical / Romantic-esoteric names
    "Swedenborg": r"swedenborg",
    "Saint-Martin": r"saint-martin\b",
    "Ballanche": r"ballanche",
    "Maistre": r"maistre\b",
    "Fabre d'Olivet": r"fabre d.olivet",
    "illumin*": r"\billumin",
    "théosoph*": r"th[ée]osoph",
    "mystique": r"\bmystiques?\b",
    # Alchemical / Hermetic
    "alchim*": r"\balchimi",
    "hermét*": r"\bherm[ée]ti",
    "cabal*/kabbal*": r"\b[ck]abb?ali",
    "grand œuvre": r"grand[- ]?(œ|oe)uvre",
    "transmutation": r"transmut",
    # Magnetism
    "magnétisme": r"magn[ée]tis",
    "somnambul*": r"somnambul",
    # Egypt / hieroglyphs
    "égypt*": r"[ée]gypt",
    "hiéroglyph*": r"hi[ée]roglyph",
    # Socialist-esoteric milieu
    "Fourier": r"fourier",
    "Leroux": r"\bleroux\b",
    "Lamennais": r"lamennais",
    # Christian-providential register
    "Providence/providentiel": r"providen",
    "harmoni*": r"harmoni",
    "déchéance": r"d[ée]ch[ée]ance",
    "rédemption": r"r[ée]demption",
}


def load(name):
    t = (SRC / name).read_text(encoding="utf-8")
    # strip Project Gutenberg header/footer
    s = t.find("*** START OF")
    e = t.find("*** END OF")
    if s != -1:
        t = t[t.find("\n", s) + 1:]
    if e != -1:
        t = t[:e]
    return t


def main():
    kwic = "--kwic" in sys.argv
    texts = {v: load(v) for v in VOLS}
    words = {v: len(re.findall(r"\w+", t)) for v, t in texts.items()}
    print("marker".ljust(24) + "".join(v[:3].rjust(7) for v in VOLS) + "   total")
    print("words".ljust(24) + "".join(str(words[v]).rjust(7) for v in VOLS) + str(sum(words.values())).rjust(8))
    for label, pat in MARKERS.items():
        row = [len(re.findall(pat, texts[v], re.I)) for v in VOLS]
        print(label.ljust(24) + "".join(str(n).rjust(7) for n in row) + str(sum(row)).rjust(8))
    if kwic:
        for label, pat in MARKERS.items():
            if label in ("Providence/providentiel", "harmoni*", "maçon (any)", "égypt*"):
                continue
            print(f"\n=== {label}")
            for v in VOLS:
                flat = re.sub(r"\s+", " ", texts[v])
                for m in re.finditer(pat, flat, re.I):
                    print(f"{v[:3]} | …{flat[max(0, m.start() - 110):m.end() + 110]}…")


if __name__ == "__main__":
    main()
