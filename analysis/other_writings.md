# Bastiat's other writings: what they add to the esotericism question

**Corpus.** The Guillaumin *Œuvres complètes* (2nd ed., ed. Paillottet), in 7 volumes and about 1.23 million words, in proofread Project Gutenberg transcriptions. Texts are in `sources/bastiat_oeuvres_completes/` and described in the README there. I also consulted the Institut Coppet edition of the *Correspondance avec la famille Cheuvreux* (not committed). References are to volume (OC1–OC7) and, for letters, to date.

**Method.**
1. A marker scan across all seven volumes (`oeuvres_marker_scan.py`, output in `oeuvres_marker_scan_output.txt`). Every hit was checked in context with `--kwic`.
2. A close reading of the texts that bear on formation and religion:
   - the Calmètes letters (1819–46) and Coudroy letters (1824–50), which cover the years of the reported lodge membership;
   - Fontenay's biographical *Notice* (OC1);
   - the 1845–47 letters on the genesis of the *Harmonies*;
   - the OC7 *ébauches*: *Projet de préface pour les Harmonies*, *Individualisme et Fraternité*, *Lettre à un ecclésiastique*, the fragments on religion and on the separation of temporal and spiritual power, the fragment on unity;
   - *Physiologie de la spoliation* (*Sophismes*, 2nd series, ch. I).

---

## 1. Marker scan: the esoteric lexicon is absent from the whole œuvre, not just from the *Harmonies*

| Marker | Hits (7 vols.) | What the hits actually are |
|---|---|---|
| Swedenborg, Ballanche, Fabre d'Olivet, théosoph-, somnambul-, transmutation, Grand Orient | **0** | — |
| franc-maçon- | 2 | Both use **Freemasonry as the antitype of publicity** (§2) |
| loge(s) | 3 | Theatre boxes; pig-sties; the verb *loger* |
| maçon | 22 | Masons by trade in lists of workers; *colimaçon* |
| vénérable | 7 | "femmes vénérables", "l'antiquité vénérable de nos institutions", the bishop of Langres, a meeting chairman |
| écossais(e) | 4 | The Scottish free-traders; one "secte écossaise" (1830; §3) |
| Saint-Martin | 4 | A Landes commune; a Paris street |
| Maistre | 3 | Fontenay's *Notice* only (§4) |
| illumin- | 9 | Light and gas lighting; pejorative: "celui qui vous parle **n'est pas un illuminé**" (OC2), Proudhon's "intuitions, **illuminations**, révélations" (OC5), "apocalypses de nos **illuminés** modernes" (OC7) |
| alchim- | 3 | Socialism "comme l'astrologie et l'alchimie" (OC6); "une moderne alchimie des votes du Parlement" (OC7); a joke about a pharmacist-"alchimiste" (Cheuvreux) |
| hermét- | 2 | *hermétiquement fermé* (a frontier; Proudhon's intelligence) |
| cabal- | 1 | "une opération cabalistique" (i.e. magic) as something that does *not* feed armies (OC3) |
| grand œuvre | 1 | A translated Boston protectionist tract: "le grand oeuvre de la RESTAURATION [du tarif]" (OC7) |
| magnétisme | 4 | The compass and natural forces only; **never animal magnetism** |
| hiéroglyph- | 6 | Priestly monopoly (OC4, OC6); the Post Office's tariff marks (OC4) |

Over roughly 1.2 million words, the pattern is the same as in the 1850 *Harmonies*. Where esoteric vocabulary appears, it is used polemically or as an ordinary word, never as a term of art.

---

## 2. Freemasonry appears only as the opposite of publicity

The only two uses of *franc-maçonnerie* in the complete works set it up as the **model of secret organisation that the free-trade movement is *not***.

- **London, July 1845, letter to Coudroy (OC1).** Cobden tells him: « La Ligue est une franc-maçonnerie, **à cela près que tout est public** ».
- ***Cobden et la Ligue*, introduction (1845, OC3).** One day the French will ask « dans quel souterrain impénétrable, dans quelles catacombes ignorées elle a été ourdie, **quelle franc-maçonnerie mystérieuse en a noué les fils**; et ce livre sera là pour répondre: Eh, mon Dieu! **cela s'est fait en plein soleil**… Cela s'est accompli en public, par une discussion qui a duré dix ans. »

This is the discourse test of the report (§5) applied to Masonry itself. The Ligue is a brotherhood with the secrecy removed. That fits the "ethos without ritual" verdict (report §8). It also counts against any reading in which Bastiat writes for initiates: in his own published words, the model is "tout est public".

---

## 3. The formative letters (1819–31): the lodge years leave no trace

The Calmètes and Coudroy letters cover exactly the period of the reported membership of *La Zélée* (Bayonne, early 1820s). They record a great deal of his inner life:
- **A religious crisis, 1820–21.** « Mon esprit se refuse à la foi et mon coeur soupire après elle… si le paganisme est la mythologie de l'imagination, le catholicisme est la mythologie du sentiment ». Then: « ce sublime rapprochement de Dieu et de l'homme, **cette rédemption, qu'il doit être doux d'y croire! quelle invention, Calmètes, si c'en est une!** » (Oct. 1820). Then a provisional return to religion (April 1821). Then, in Sept. 1821, « j'ai abandonné mes livres, ma philosophie, ma dévotion… **Je vais dans le monde** ».
- **His reading.**
  - Say's *Traité* and Laromiguière (1820).
  - "Smith, Say, Destutt, et *le Censeur*" (1825).
  - Alfieri, Chesterfield, Casimir Delavigne, Byron, Walter Scott.
  - Franklin's moral essays: « je me suis mis à prendre les mêmes moyens que lui pour devenir aussi bon et aussi heureux » (1827).
  - Lamennais and Dunoyer, the *Revue encyclopédique*, Comte (1827).
  - *Paul et Virginie* and **Pope** (1824).

There is no mention of a lodge, degrees, rituals, brothers, or any esoteric author.

**Two items deserve comment.**

**(a) Pope's *Essay on Man* (letter to Coudroy, 15 Dec. 1824).** Bastiat sends Coudroy the opening lines of Epistle I to translate:

> Let us (since life can little more supply / Than just to look about us to die) / Expatiate free over all this scene of man

(This is Bastiat's transcription. Pope has "…to look about us and to die… o'er all this scene of man".)

The same epistle ends:

> All nature is but art, unknown to thee; / All chance, direction, which thou canst not see; / **All discord, harmony not understood; / All partial evil, universal good**.

That is the whole theodicy of the *Harmonies* in four lines: evil as a component of harmony (« dissonance harmonique », L3067) and order hidden from the ordinary eye (« une naturelle et savante organisation qui agit à notre insu », L277). It is a documented, first-hand, mainstream source for the structure the report had attributed to Leibnizian theodicy in general. It is Pope's popular Leibnizian optimism, which Bastiat was reading line by line with Coudroy in 1824. A second Bernardin text also appears: *Paul et Virginie* is by the author of the *Harmonies de la nature* (1815), which the report had already listed as a next step.

**(b) "La secte écossaise" (letter to Coudroy, Bayonne, 4 Aug. 1830).** Describing the July Revolution in Bayonne, he writes: « je n'eusse été qu'à demi de la **secte écossaise**, j'en serais doublement aujourd'hui ».
- **The editor's reading.** Paillottet, who knew him and handled the manuscripts, glosses it as the school of Adam Smith: liberal politics as the corollary of Scottish political economy. That reading fits the idiom. The economists had been « la secte des économistes » since the physiocrats, and the sentence is about "hommes éclairés, riches, prudents" proving that wealth and enlightenment produce order.
- **The Masonic reading.** In a Masonic context *écossais* would evoke the Scottish Rite (the *Rite Écossais Ancien et Accepté*, or the *Rite Écossais Philosophique* that the *Dictionary* associates with Hermetic high degrees).
- **Assessment (before the lodge records).** The Masonic reading is possible, but nothing in the letter supports it, and it cannot be preferred to the editor's.
- **Update (lodge records, `lodge_records.md`).** Crouzet's history of Bayonne Masonry reads the phrase Masonically ("Laffitte appartenait à la branche écossaise"). Bastiat himself was a Rose-Croix, and in Dec. 1821 his chapter sought Scottish Rite cumul. The two readings are now evenly balanced, and a deliberate double meaning to a friend is possible. I note it because it is the only phrase in the correspondence where a Masonic double meaning is even conceivable. It is also exactly the kind of pun an esoteric hermeneutic would seize on (*Dictionary*, *Secrecy III*; report §0).

---

## 4. Fontenay's *Notice*: a documented route to Maistre, and a religious synthesis attributed to it

Fontenay's biographical notice (OC1) is based on Coudroy's own account. It gives the only documented intellectual channel toward Illuminist-adjacent thought:
- **Coudroy's route to Maistre.** Coudroy, "tourné de bonne heure du côté de l'étude de la philosophie religieuse", had moved from Rousseau and Mably to « la *Politique sacrée* et la *Législation primitive*… **les de Maistre et les Bonald** ». There, liberty and individual dignity were « des principes de **déchéance** et de désordre ».
- **Bastiat's counter-case.** Bastiat, coming from « **les cercles de Bayonne** », argued that free interests limit one another into order, and that « **le mal**… n'est au fond qu'un accident de la recherche même du bien, une erreur que corrigent l'intérêt général… et l'expérience ».
- **The synthesis.** Fontenay then says Bastiat did not come away untouched: « ce ne fut pas sans recevoir lui-même une certaine impression de ces grandes théories de Bonald et de Maistre… c'est peut-être à une sorte de pénétration réciproque des deux principes… qu'il faudrait attribuer **le caractère profondément religieux qui se mêle, dans les écrits de Bastiat, à la fière doctrine du progrès par la liberté** ».

**Why this matters.** Maistre is the one figure in this story who *is* an Illuminist: a Rectified Scottish Rite Mason of Willermoz's Lyon system (*Dictionary*, *Maistre*; *Illuminism* §5). His *Soirées de Saint-Pétersbourg* (1821) carry Illuminist themes (*réversibilité*, providential suffering). A contemporary witness, Fontenay relaying Coudroy, attributes the religious register of Bastiat's economics partly to a long dialogue with a Maistrian-Bonaldian traditionalism. So the esoteric genealogy identified in the report (§2, §9) has a **documented personal channel**: Coudroy's reading of Maistre. It does not need to pass through Ballanche. But Fontenay, like Bastiat, reads Maistre as the theorist of **Authority** that liberty must answer, not as a theosopher. The route runs through Catholic traditionalism, not through lodge teaching.

Fontenay speaks of the « cercles de Bayonne » and says nothing about a lodge. The editors of the collected works, all close to Bastiat, are silent on Masonry throughout.

---

## 5. The genesis of the *Harmonies*: "natural and providential" harmonies against "artificial" ones

- **Letter to Coudroy, Paris, 5 June 1845.** « Si mon petit traité, *Sophismes économiques*, réussit, nous pourrions le faire suivre d'un autre intitulé: *Harmonies sociales*. Il aurait la plus grande utilité, parce qu'il satisferait **le penchant de notre époque à rechercher des organisations, des harmonies artificielles**, en lui montrant la beauté, l'ordre et le principe progressif dans **les harmonies naturelles et providentielles** ».
- **Letter of August 1847.** He plans a course "non d'économie politique pure, mais d'économie sociale… *Harmonie des lois sociales*".

This is direct authorial evidence for the report's §6. The title is **polemically positioned against the Fourierist *Harmonie*** (the "harmonies artificielles" of the organisers), and its positive content is "providential". It is a Christian-providential answer to an esoterically charged socialist word, not an adoption of that word's esoteric content.

---

## 6. The *Projet de préface pour les Harmonies* (late 1847): the reading list of the Mugron years

This draft, written as a letter from Coudroy to "Frédéric", is the most informative single text on the intellectual world in which the *Harmonies* was conceived:
- **Faith by the tombs.** « la racine de la foi reverdissait dans nos âmes à l'aspect de ces tombes chéries ».
- **Plato read for progress.** « Tantôt nous lisions Platon… pour nous assurer de l'extrême infériorité de la société antique; et nous disions:… **l'homme est perfectible** et la foi dans ses destinées n'est pas trompeuse ». Antiquity serves as the measure of progress, not as a store of *prisca sapientia*.
- **The reading list.** « Tantôt nous nous faisions suivre dans nos longues promenades de **Bacon, de Lamartine, de Bossuet, de Fox, de Lamennais, et même de Fourrier** », with Say, Dunoyer and Comte as the scientific base.
- **The humanitarian vision he was urged to write.** « la fusion des races, des intérêts, des langues, des idées… les institutions progressives remplaçant le régime du despotisme absolu et des **castes** héréditaires… **le genre humain se préparant par l'unité aux destinées qui lui sont réservées** ».
- **Harmony as system.** « Toutes les idées forment un tout systématique et **harmonieux** ».

This confirms, from Bastiat's own pen, the "Romantic-humanitarian" layer of the report's conclusion: Lamartine, Lamennais, Fourier, humanity's destiny as unity. It also shows its limits. There is no Ballanche, Saint-Martin, Swedenborg, Fabre d'Olivet or Court de Gébelin, and no Hermetic or alchemical author. The one "esoteric-socialist" author named, Fourier, comes with "et même", i.e. read as an opponent.

---

## 7. Religion in the late fragments: Catholic, ecumenical, anti-sacerdotal, and unity only at the end

- ***Lettre à un ecclésiastique* (Mugron, 28 March 1848).**
  - « j'ai foi dans une **fusion future entre toutes les religions chrétiennes**, ou… dans l'absorption des sectes dissidentes par le catholicisme ».
  - Separation of Church and State as the condition of that fusion.
  - « je suis tellement frappé de **l'infirmité native** de la raison individuelle », the same formula the *Harmonies* uses for value (L1099, L1693).
- **Fragment 79 (c. 1849).** The age-long conflict began « le jour où **un homme s'est servi de Dieu pour faire d'un autre homme son esclave intellectuel** ». This is the *Harmonies*' theocratic spoliation (L3107).
- **Fragment 80, *De la séparation du temporel et du spirituel* (1849).** « Le monde est plein d'honnêtes gens qui voudraient être catholiques et ne le peuvent pas… Ils ont au coeur **une racine de foi**… Mais le sacerdoce serait l'instrument de la religion, la religion ne serait pas l'instrument du sacerdoce. Tout est là. »
- **Fragment 81, on unity.** « **L'unité, en toutes choses, est la consommation suprême, le point vers lequel gravite et gravitera éternellement, sans jamais l'atteindre, l'esprit humain**. Si elle devait se réaliser dans l'humanité, ce ne serait qu'à la fin de toutes les libres évolutions sociales. C'est la variété, la diversité qui sont au commencement… ». This is the clearest statement anywhere of the asymptotic structure in report §1–§2. It is also the decisive difference from Ballanche and the Martinists. For them unity is primordial (the Universal Adam) and lost. For Bastiat it is only ever approached, at the end.
- **Deathbed, Rome, Dec. 1850 (Paillottet's journal, OC1).** He confesses and receives communion. He then says: « Le déiste… n'a de Dieu qu'une idée trop vague… Il faut que l'homme s'appuie sur une révélation pour être véritablement en communication avec Dieu. **Je ne discute pas le dogme, je l'accepte.** » This is an explicit rejection of the deist, "Grand Architect" position, voiced as Catholic submission.

---

## 8. The hieroglyph passage has a fuller twin, and it targets the clergy

*Physiologie de la spoliation* (*Sophismes*, 2nd series, ch. I, 1848; OC4) develops, in the first person of an imagined impostor-priest, what the *Harmonies* compresses at L2977:

> « on sait à quel degré de toute-puissance étaient arrivés **les prêtres égyptiens**… j'interdirais l'examen de mes titres… Je ferais de cette question… des questions *tabou*… je m'attribuerais, ainsi qu'à mes complices, **le monopole de toutes les connaissances, je les cacherais sous les voiles d'une langue morte et d'une écriture hiéroglyphique**, et… j'aurais soin d'inventer **une institution qui me ferait pénétrer, jour par jour, dans le secret de toutes les consciences**… Ainsi les hommes ont un grand besoin d'instruction et de morale: je m'en ferais le dispensateur. »

The "langue morte" (Latin), the institution that penetrates "le secret de toutes les consciences" (confession) and the monopoly of instruction and morals show that the Egyptian priesthood is a **type** whose modern antitype is clerical, not Masonic or occultist. *Individualisme et Fraternité* (OC7) repeats the type once more: « **Le prêtre égyptien**, qui imposait de fausses croyances à ses semblables pour se rendre maître de leurs actions et même de leurs pensées ». This refines report §5: the "caste… hiéroglyphique" at L2977 is Bastiat's recurring figure for **sacerdotal** monopoly of knowledge. It matches the object Marconis and Leroux were naming *ésotérisme*, but Bastiat's own development of it aims at priestcraft generally, the Latin clergy included.

---

## 9. Net effect on the verdict

1. **Hermetic–alchemical source: still not supported, now across the whole œuvre.** In about 1.2 million words there are zero technical terms, zero esoteric authors, and every *alchimie/illuminé/cabalistique* is pejorative.
2. **Masonic influence: weaker than before as a matter of text.**
   - The complete works mention Freemasonry twice, both times as the secret antitype of the Ligue's publicity.
   - The letters of the lodge years say nothing of a lodge.
   - His close friends and editors (Coudroy, Fontenay, Paillottet) are silent on it.
   - His deathbed profession explicitly rejects deism.

   The membership is not refuted. The lodge records (`lodge_records.md`) show it was extensive: Rose-Croix at 20, chapter officer, lodge orator. The silence in his letters and in his editors' notices is therefore discretion. In print, the formation left no Masonic vocabulary, only the Christian-soteriological and fraternal register that the Rose-Croix degree shares with the Church. The phrase *secte écossaise* is now two-sided.
3. **The Christian-providential and Romantic-humanitarian explanation: strengthened by documented, first-hand sources.**
   - Pope's *Essay on Man* (1824), for "all discord, harmony not understood; all partial evil, universal good".
   - Bernardin (*Paul et Virginie*).
   - Franklin's moral perfectionism.
   - The explicit reading list: Plato, Bacon, Lamartine, Bossuet, Lamennais, "and even Fourier".
   - The 1845 plan of *Harmonies* against "harmonies artificielles".
   - The asymptotic unity fragment.
4. **The one esoteric genealogy (Illuminist reintegration → Romantic historiosophy) now has a documented personal channel.** It runs through **Maistre and Bonald via Coudroy**, and Fontenay explicitly credits it with the "caractère profondément religieux" of Bastiat's economics. It reached him as Catholic traditionalism to be answered by liberty, not as Illuminist doctrine.
