"""Lexical profile of the 1850 first edition of Harmonies économiques.

Counts technical vocabularies associated with candidate traditions
(alchemical/Pernety, Masonic ritual, Christian theology, Newtonian science,
harmony, evil, gratuity). Word-bounded regexes avoid false hits
such as 'logement' for 'loge' or 'usages' for 'sages'.
Usage: python3 analysis/lexical_profile.py
"""
import re
from pathlib import Path

TEXT = Path(__file__).with_name("harmonies_1850_reflowed.txt").read_text(encoding="utf8")
T = TEXT.lower().replace("’", "'")

GROUPS = {
    "A. Alchemical terms of art (Pernety 1758)": [
        r"alchim", r"transmut", r"grand[ -]œuvre", r"magistère", r"élixir", r"philosophale",
        r"putréf", r"calcin", r"coagul", r"\bmercure\b", r"\bsoufre\b", r"teinture", r"régénér",
        r"\bvolatil", r"quintessence", r"hermès", r"hermétique", r"athanor", r"alambic", r"creuset",
        r"\bsels?\b", r"rosée", r"matières? premières?", r"\badeptes?\b",
    ],
    "B. Masonic ritual / initiatic": [
        r"\bloges?\b", r"franc-maç", r"\bmaçons?\b", r"\batelier", r"\btemples?\b", r"architecte",
        r"\bniveau", r"nivel", r"équerre", r"\bcompas\b", r"\bcolonnes?\b", r"pierres? angulaires?",
        r"pierre d'attente", r"\borient\b", r"vénérable", r"\bhiram\b", r"acacia", r"\bgrades?\b",
        r"initia", r"fraternité", r"\bfrères?\b", r"divin ouvrier", r"grand mécanicien",
    ],
    "C. Christian theology": [
        r"providen", r"\bdieu\b", r"créateur", r"rédemption", r"rachète", r"déchéance", r"infirmité native",
        r"sueur de (?:ton|son) front", r"genèse", r"moïse", r"\bchrist", r"calice", r"royaume de dieu",
        r"\bbéni[rt]\b", r"martyr", r"dogme", r"digitus dei", r"psalmiste", r"\bimpie", r"sacrilège", r"miracle",
    ],
    "D. Newtonian / Enlightenment science": [
        r"newton", r"k[ée]pl", r"laplace", r"gravitation", r"attraction", r"centrifuge", r"centripète",
        r"mécanique", r"mécanisme", r"observation", r"astronom", r"physiolog", r"molécule", r"élasticité",
        r"électricité", r"magnétisme", r"affinité",
    ],
    "E. Harmony / music": [r"harmoni", r"dissonan", r"discordan", r"vibration"],
    "F. Evil / pain": [r"\ble mal\b", r"\bdu mal\b", r"\bmaux\b", r"douleur", r"souffrance", r"châtiment", r"\bmission"],
    "G. Gratuity / community": [r"gratuit", r"communauté", r"dons? de dieu", r"libéralité", r"par-dessus le marché", r"anéanti"],
}

if __name__ == "__main__":
    print(f"Words: {len(T.split())}")
    for group, pats in GROUPS.items():
        print(f"\n{group}")
        print("  " + " | ".join(f"{p}: {len(re.findall(p, T))}" for p in pats))
