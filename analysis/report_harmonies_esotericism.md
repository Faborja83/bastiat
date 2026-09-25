# *Harmonies économiques* (1850) and the Western esoteric traditions: a close reading of the first edition

**Question.** Are the conceptual structures of Bastiat's *Harmonies économiques*, especially the features scholars have found "unusual", better explained by ordinary nineteenth-century liberal/Christian language, or do they show combinations of concepts characteristic of the French Hermetic–alchemical–Masonic tradition?

**Short answer.** The unusual features are real, and they are theological. In the first edition Bastiat builds a soteriology of economic progress: *value is the evil (le mal)* born of the obstacle that the Genesis curse placed between need and satisfaction, and progress is the gradual annihilation of that value into free, common utility, by which "l'humanité se relève de sa déchéance". Structurally, this is the Fall → progressive rehabilitation schema that the *Dictionary of Gnosis and Western Esotericism* traces from Illuminist "reintegration" into Romantic philosophies of history. In Bastiat, however, it arrives already historicised and secularised, stated in the vocabulary of Christian providentialism, physico-theology and Newtonian science. It also comes with an explicit repudiation of alchemy, astrology, imagination, occult qualities, secrecy, hieroglyphic knowledge and priestcraft.

- **Hermetic–alchemical source:** not supported. The parallels are structural (self-limiting evil, "value annihilated", the water cycle, the earth as a "laboratory"). The technical lexicon is entirely absent, and Bastiat projects the alchemist-operator model onto his socialist opponents.
- **Masonic influence:** plausible only at the level of liberal ethos. That ethos includes the republican triad, fraternity, the "niveau" (level) as equalising telos, builders' imagery, and Voltairean anti-priestcraft. No ritual vocabulary appears.

---

## 0. Sources, scope and method

**Primary text.** The uploaded `HARMONIES.txt` is the Brussels 1850 edition (Méline, Cans & Cie), i.e. the text of the **first edition**: the dedication "À la jeunesse française" and chapters I–X (Organisation naturelle/artificielle; Besoins, efforts, satisfactions; Des besoins de l'homme; Échange; De la valeur; Richesse; Capital; Propriété, communauté; Propriété foncière; Concurrence) plus the closing section on spoliation. I reflowed it into paragraphs (`harmonies_1850_reflowed.txt`) and read it in full. Every citation below is to a line (L…) of that file. The full reading notes are in `evidence_register.md`.

**Important scope correction.** The chapters most often quoted on theodicy (*Le Mal*, *Perfectibilité*, *Responsabilité*, *Solidarité*, *Moteur social*) are **posthumous**. Paillottet and Fontenay added them from Bastiat's manuscripts in the 1851 second edition. My earlier answer leaned on them. What follows rests on the first edition only; §7 treats the posthumous material separately. The key theological terms (*mission du mal*, *rédemption*, *déchéance*, *dissonance harmonique*, *graduelle réduction du mal*, *vis medicatrix*) are **all already present in the first edition**. I checked each against the 1851 and 2015 (Institut Coppet) texts.

**Secondary literature used (from your upload).**
- A. Faivre, *Western Esotericism: A Concise History* (SUNY 2010): Introduction, ch. 3 ("in the Shadow of the Enlightenment"), ch. 4 ("From Romantic Knowledge to Occultist Programs").
- W. J. Hanegraaff et al. (eds.), *Dictionary of Gnosis and Western Esotericism*. **Only vol. 2 (I–Z) was uploaded.** Entries used: *Illuminism*, *Maistre*, *Pernety*, *Ragon de Bettignies*, *Politics and Esotericism*, *Romanticism*, *Music III–IV*, *Lacuria*. Vol. 1 (Alchemy, Correspondences, Freemasonry, Hermetism, Fourier…) is missing and should be consulted next.
- K. von Stuckrad, *Locations of Knowledge in Medieval and Early Modern Europe* (Brill 2010): "Approaches to Esotericism", "Secrecy as Social Capital", "Genealogies of Wisdom", "Linguistic Ontologies in Christian Kabbalah".
- Dom A.-J. Pernety, *Dictionnaire mytho-hermétique* (1758). The uploaded `dictionnairemyth00pern_hocr.txt` was not in the container, so I used the identical archive.org scan (`dictionnairemyth00pern`).
- Not usable substantively: the *Cambridge Handbook* file is a one-page book review, and `bibpompidou-640.pdf` (two identical copies) is a study of contemporary esoteric readerships.

**Method: three independent tests plus a prior.**
1. **Form of thought (Faivre).** Are the four intrinsic components present (correspondences, living nature, imagination/mediations, transmutation), plus the two relative ones (concordance, transmission)? Faivre requires all four intrinsic components together, and stresses that "a same component [can] belong to several forms of thought" (Intro §IV).
2. **Lexical markers.** Does the text use the technical vocabulary of the candidate traditions (Pernety's alchemical lexicon; Masonic ritual vocabulary)? A reproducible count is in `lexical_profile.py` / `lexical_profile_output.txt`.
3. **Discourse (von Stuckrad; Hanegraaff).** Does the text make claims to higher/perfect knowledge organised by a back-and-forth of concealment and disclosure? Where does it stand in the polemical boundary-work that constructed "esotericism" as rejected knowledge?
4. **Historical prior.** Bastiat's reported membership of the Bayonne lodge *La Zélée* (1820s). This is attested in biographies and Bayonne Masonic historiography, but not verified here from lodge records.

---

## 1. *Le mal*: your correction is right, and the text goes further than the famous last sentence

You are right that *mal* is not a mere logical opposite. The first edition uses it in all three classical senses (cf. Leibniz, *Théodicée* §21):
- **physical** (*douleur*, *souffrance*): "il ne nous reste guère que le choix des maux" (L569, L471, L3081);
- **moral** (*erreur*, *vice*, *spoliation*): "le libre arbitre implique l'erreur… et l'erreur, c'est le mal" (L2945);
- **metaphysical** (limitation): "notre infirmité native" (L1099, L1693, L1765, L2177), "imperfection native" (L1175).

It is an explicitly **theodicean** term: "On a demandé souvent si l'existence du mal pouvait se concilier avec la bonté infinie du Créateur, redoutable problème que la philosophie agitera toujours et ne parviendra probablement jamais à résoudre" (L569).

The first edition's decisive move is to **identify value itself with evil**:

> « L'utilité est le bien qui fait cesser le besoin par la satisfaction. **La valeur est le mal**, car elle naît de l'obstacle qui s'interpose entre le besoin et la satisfaction ; sans ces obstacles… l'utilité serait infinie, gratuite et commune sans condition, et la notion de valeur **ne se serait jamais introduite dans ce monde**. » (L1573)

> « [La valeur] est le signe, le symptôme, le témoin, la preuve de **notre infirmité native**. Elle nous rappelle incessamment cet **arrêt prononcé à l'origine : Tu mangeras ton pain à la sueur de ton front**. Pour l'Être tout-puissant ces mots : effort, service, et par conséquent valeur n'existent pas. » (L1693)

> « S'il n'y avait jamais d'obstacles… il n'y aurait ni efforts, ni service, ni valeurs, **non plus qu'il n'y en a pour Dieu**, et… l'humanité serait, **comme Dieu**, en possession de la richesse infinie. » (L1703)

He then accuses his opponents of "confondre la valeur avec l'utilité, c'est-à-dire **le mal avec le bien**" (L1751; cf. L1739: "si le mal est le bien"; L1783).

**Consequence for interpretation.** The closing sentence ("l'harmonie ne consiste pas dans l'absence absolue du mal, mais dans sa **graduelle réduction**", L3123) is not only about crime or suffering. It names the telos of the whole value theory. Progress is the progressive *annihilation* of value (*valeur anéantie*, 34 occurrences) and its passage "du domaine de la propriété dans celui de la communauté" (L1787, L2089). That is, the gradual reduction of the evil of the obstacle toward a God-like gratuity which humanity approaches but never reaches ("L'infini… n'est sous aucun rapport l'attribut de l'humanité", L1705; "l'homme a beau s'élever, il est toujours aussi loin de l'omnipotence", L2179). Economists have mostly missed this link, and it is the core of what is "unusual" in the book.

The evil also has a **mission** and **limits itself**. It must "se servir de limite à lui-même, se détruire par sa propre action, et… chaque douleur prévienne une douleur plus grande en réprimant sa propre cause" (L145). The mission of suffering is "de détruire progressivement ses propres causes… en nous la faisant acheter et mériter" (L583), and a crime's punishment is born "naturellement du crime même" (L2623). The first edition already names this "une **dissonance harmonique**" (L3067).

---

## 2. The deep structure is a soteriology, and it is in the first edition

Put together, the first edition articulates a complete Fall/redemption narrative in economic terms:

| Moment | First-edition wording |
|---|---|
| Decree/curse | « cet arrêt… prononcé sur l'homme dès l'origine : Tu mangeras ton pain à la sueur de ton front » (L1693, L3099) |
| Evil = obstacle = value | « La valeur est le mal » (L1573); value = proof of « notre infirmité native » (L1693) |
| Sin = revolt against the decree | the human "révolte contre cette loi", saying « à son frère : À toi le travail ; à moi le fruit du travail » → spoliation (L3099; cf. Cain) |
| Redemption through labour | « le genre humain… **se rachète à la sueur de son front**… les plus avancés dans **la voie de la rédemption** vous tendent une main secourable, volontairement ou à leur insu » (L2013) |
| Instruments of providence | property's « mission… est de réaliser de plus en plus la communauté » (L2055); competition is the « ressort » God set to keep his gifts in their « **destination primitive**, la gratuité, la communauté » (L2833) |
| Rising from the Fall | « on voit clairement **l'humanité se relever de sa déchéance** » (L3025) |
| Asymptote | humanity "comme Dieu… richesse infinie" in the limit (L1703); « Que sont les degrés qu'il parcourt sur l'échelle de l'infini ? » (L2179) |

**Its language is Christian, and deliberately so.**
- *Rédemption*, *déchéance*, *infirmité native*, Genesis 3:19, *Fiat lux* (L2179), Psalm 19 "Coeli enarrant gloriam Dei" (L441; cf. L131 "la mécanique sociale… raconte sa gloire"), "Digitus Dei est hic" (Exod. 8:19; L3063, L3123).
- Gethsemane: « en acceptant d'avance **le calice**, je n'en dois pas moins m'efforcer de l'éloigner », L2285.
- The father "qui **bénit le pain** qu'il rompt" as proof that there is something *gratuit* in providence (L1471). Gratuity here functions as *grace*: God's gifts are « prodigués avec une libéralité qu'il ne doit pas à son propre mérite » (L1941).
- Communauté progressive is « la plus touchante **dispensation** de la Providence » (L1467). *Dispensatio* is the Latin for theological *oikonomia*.
- He ends with an explicit Christianity/economics concordance: « Le christianisme a introduit dans le monde le grand principe de la fraternité humaine… L'économie politique vient faire accepter le même principe à la froide raison » (L3019).

**Why this matters for the esoteric question.** The *Dictionary*'s *Romanticism* entry (§6) describes exactly this schema. Illuminist theosophers (Saint-Martin, Fabre d'Olivet) placed reintegration outside history. Ballanche's *Palingénésie sociale* made historical events "the necessary and efficacious means of the reintegration". Then "Lamartine and Quinet [substituted] a rationalist perfectibilitarianism… for the esotericist telos of the rehabilitation of humanity from the Fall… historical progress, while providentially guided… becomes the end in itself. Salvation is now conceived of as a spiritualization of terrestrial humanity within the historical process… later Romantics historicized reintegration itself."

Bastiat fits exactly at that end of the spectrum, transposed into political economy. Capital makes enjoyments « plus pures… plus spiritualistes » (L1999), and property's « mission » and competition's « intentions finales » (L2873) do the providential work. There is one decisive difference from the Martinist *Réintégration*. Pasqually posits a primordial perfection lost by misuse of freedom. Bastiat **denies** a primordial perfection: "la perfection n'est pas au commencement mais à la fin de l'évolution humaine" (L649); equality, liberty, fraternity, unity are « une fin et non un point de départ » (L811); the starting point is « une parfaite égalité de misère, de dénûment et d'ignorance » (L2013). His *déchéance* is the Genesis condition of labour and need, not the loss of a golden age. Rousseau's golden-age schema is his explicit target (L649–653).

So what is "unusual" is a **historicised, economic reintegration narrative**. Its genealogy passes through the Romantic appropriation of Illuminist themes. It is voiced in the orthodox-sounding vocabulary of providence and Genesis, and it does not draw on Hermetic or alchemical sources.

---

## 3. Faivre's components, tested against the first edition

**(1) Correspondences: weak; analogy of law, not correspondence.**
- Bastiat constantly analogises the social and physical worlds: celestial ↔ social mechanics (L229, L413, L1197, L1847); molecules seeking the level ↔ interests (L23); centripetal/centrifugal forces ↔ self-interest/sympathy (L1053) and centripetal/centrifugal competition (L2957); the human body ↔ the social body (L3065, L3123); circulation « dans toutes les veines du corps social » (L2993).
- Closest to a microcosm formula: « Ce qui est vrai de l'homme est vrai de la société… [l'homme isolé] est comme un résumé de la société… l'humanité… est **un homme immense, collectif, multiple** » (L679; cf. L1803).
- But these are **causal-nomological** analogies (Newton, Laplace), not Faivre's "non-causal correspondences" in a "theatre of mirrors". The "homme immense" is the Pascalian/Enlightenment collective subject (and a methodological Robinson device), not Swedenborg's *Maximus Homo*.
- Most tellingly, Bastiat is **hostile to metaphor as a source of knowledge**. Value in things exists "par pure **métonymie**… la **métaphore** a fait dévier la science" (L863; also L1275, L1443, L1627, L2239, L2699). He cites *tout est dans tout* only to warn against over-generalising (L1237). Compare the Christian Kabbalah that von Stuckrad describes, where reality is a "texture of metonymically arranged names" (Gikatilla/Knorr). For Bastiat, metonymy is precisely the error to be corrected.

**(2) Living nature: physico-theological, not Hermetic.**
- Nature is an agent: it « travaille, de toute éternité peut-être » (L2221). The earth is a « grand laboratoire… dans lequel s'accomplissent des mystères dont à peine la science humaine a soulevé le voile » (L1331; cf. Say quoted at L1545 and L2439, "atelier chimique"). There are « élaborations mystérieuses et inconnues » (L2239) and « miracles de végétation » (L2737).
- The most "Hermetic-looking" line in the book is Virgil's world-soul verse: in social mechanics « vit aussi la pensée universelle, **mens agitat molem** » (Aen. VI.727), where « chaque atome est un être animé, pensant… [doué de] la LIBERTÉ » (L413). Its point, though, is that the social "atoms" are free wills.
- Against this, nature is equally an **instrument**: « La nature devient un **esclave** qu'il ne faut ni nourrir, ni vêtir… » (L939), natural forces are « contraintes à agir » (L1929, L2691) and « asservies » (L1827, L3041), and nature must be « domptée » (L2001). Its work never has value: « Il n'y en a pas une [obole] qui ira rémunérer Dieu ou la nature » (L1337). There is no inner light or fire, no history of nature, no suffering nature awaiting deliverance (Rom. 8, which Faivre cites as typical).
- **The test passage** is the water cycle, called « **le travail de Dieu** » (L2685). The sun evaporates the ocean, the water, « dégagée du sel qui l'altère, s'élève… », condenses, « se filtre et s'épure », and « changement de formes, changement de lieux, utilité, rien n'y manque ». It reads like distillation (cf. the Emerald Tablet's "ascendit a terra in coelum"). In fact "changement de forme/de lieu" are **J.-B. Say's categories of production** (manufacture, transport), applied to divine *industry*. It is the classic providential water cycle of French physico-theology (Fénelon, whom Bastiat quotes at L597, and the *Spectacle de la nature* tradition), not a stage of the Work.

**(3) Imagination and mediations: absent, and explicitly opposed.**
- Imagination is the faculty Bastiat assigns to the enemy. Socialism, « comme l'astrologie et l'alchimie, procède par l'imagination ; l'autre, comme l'astronomie et la chimie, procède par l'observation… entre l'astronome qui observe et l'astrologue qui imagine, l'abîme est infranchissable » (L75–81). The inventions of reformers are « aussi illimitées que le domaine de l'imagination » (L329).
- There are no angels, spirits or symbols. God works through « ressorts » (self-interest, competition), and the « grand Mécanicien » (L2015) is a clockmaker deity. Economics has « sa poésie… Mais elle est dans les résultats, non dans la démonstration. Elle se révèle, on ne la crée pas. **Képler** ne s'est pas donné pour poète » (L459).
- This places Bastiat exactly on the **Kepler side of the Kepler–Fludd controversy** that the *Dictionary* (Music III) treats as the founding boundary between "true" and "false" harmonic knowledge. Kepler dismissed Fludd's harmonies as having "no other foundation than the imagination".

**(4) Transmutation: the closest analogue, but collective, social and anti-operative.**
- Progress "transforme l'utilité onéreuse en utilité gratuite" (L2085). Value is « anéantie » and « passée du domaine de la propriété dans celui de la communauté » (L1787). The capitalist's capital « épure », « ennoblit », « spiritualise » (L1999–2001), and « l'humanité se relève de sa déchéance » (L3025).
- This is the structural core that an esoteric reader will recognise, and it is why the book *feels* alchemical: a base, onerous condition is progressively refined into a free, common and "purer" one.
- But there is no **inner** transformation or second birth of the subject (Faivre's defining feature). The mechanism is exchange, tools, competition, and it happens « à leur insu » (L2013), « sans le savoir, sans le vouloir » (L2873).
- Crucially, Bastiat attributes the *operative* transmutation of human nature to his opponents and rejects it:
  - Rousseau's legislator must « changer la nature humaine… donner le mouvement et la volonté, le sentiment et la vie » to "vile matière" (L359–361, L397);
  - reformers « mettent le mal au **creuset** » (L425);
  - 1848 is « faciamus experimentum in corpore vili… des expériences sociales avec des hommes comme on fait des **expériences chimiques avec des alcalis et des acides**… un représentant fouriériste… pour **manipuler** sa société modèle… un autre… offrit aussi sa **recette** » (L1113).
- Faivre's fourth component is thus present only in inverted form: Bastiat's providence refines society *without* an operator, and he treats the would-be operators as alchemists.

**(5) Concordance: present only as eclecticism and a Christian–economic accord.**
- Bastiat reconciles schools: « toutes ont entrevu la vérité, mais la vérité partielle » (L1185, L1639); « réconcilier les écoles antagoniques dans une **commune foi** » (L2009). He also reconciles Christianity with political economy (L3019).
- There is no *prisca theologia* or *philosophia perennis*: no Hermes, Zoroaster, Orpheus or Pythagoras. His authorities are Say, Smith, Destutt de Tracy, Dunoyer, Carey, Fénelon, Newton and Laplace. This is Cousinian eclecticism and the unity of the sciences (« pour une intelligence infinie, il n'y aurait qu'une seule vérité », L505; « deux vérités ne sauraient être antagoniques », L557), not esoteric concordance.

**(6) Transmission: secular.**
- The dedication casts the book as a « semence qui n'a pas en elle le principe de vie » to be completed by youth (L7–9). One of them will « arriver enfin à la démonstration rigoureuse… celui-là sera le bienfaiteur du genre humain » (L1085). The reader should rise « **par ses propres efforts** à la certitude » (L1073).
- He calls Quesnay, Turgot, Smith, Malthus and Say « **mes initiateurs, mes guides, mes maîtres** » (L2799). Initiation here means scholarly lineage in an open science. Faivre's criterion is initiation into a "regular" affiliation, where "self-initiation is not possible".

**Result of test 1.** None of the four intrinsic components is present in Faivre's sense. Only transmutation has a strong *structural* analogue, and it is inverted. By Faivre's own construct, the text is not an instance of the esoteric form of thought. It does share components with it, which Faivre explicitly allows for any form of thought (theological, scientific, utopian).

---

## 4. Lexical test: the technical vocabularies are absent

Word-bounded counts over the full first edition (≈115,600 words; `lexical_profile_output.txt`):

- **Alchemical terms of art** (Pernety): *transmutation, grand œuvre, magistère, élixir, pierre philosophale, putréfaction, calcination, coagulation, mercure, soufre, teinture, régénération, volatil, quintessence, Hermès/hermétique, athanor, alambic*: **0 each**.
  - *alchimie*: 2, both pejorative (L75; Blanqui quoted, L2451: « la patience des alchimistes n'a découvert le secret de faire de l'or »).
  - *creuset*: 1, pejorative, of socialists (L425).
  - *sels*: 4 (agricultural chemistry). *rosée*: 4 (meteorology). *matières premières*: 2 (redefined economically, L757).
  - *adeptes*: 3, always of Rousseau's disciples or the socialists (L327, L811, L2815).
- **Masonic ritual vocabulary**: *loge, grade, équerre, compas, Hiram, acacia, vénérable, franc-maçon*: **0 each**.
  - *maçon*: 2, literal (a baker's oven-builder, L1335; a trade in a list, L1411). *temple*: 1 (liberty "anathématisée dans les temples", L3109). *colonne*: 1 (property as "la colonne chancelante" under battering rams, L2021). *Orient*: 1, geographical (L3011).
  - Resonant but ordinary: *niveau/nivellement* 28, *fraternité* 15, *frère(s)* 23, *atelier* 5, *pierres angulaires* 1, *pierre d'attente* 1, *divin Ouvrier* 1, *grand Mécanicien* 1.
- **Christian theology**: *Providence* 48, *Dieu* 114, *Créateur* 7, plus the soteriological terms listed in §2.
- **Newtonian/Enlightenment science**: *gravitation* 20, *mécanisme* 35, *mécanique* 15, *observation* 25, *élasticité* 14, *électricité* 11; Newton ×5, Kepler, Laplace.
- *harmoni-* 207; *gratuit-* 216; *communauté* 103; *dons de Dieu* 34; *anéanti-* 34.

A text encoding Hermetic or lodge teaching for insiders would be expected to leave some term of art. This one leaves none, while saturating its pages with providential, Genesis and Newtonian vocabulary.

---

## 5. Discourse test: Bastiat performs the anti-esoteric boundary-work

**No claim to higher or revealed knowledge.**
- « Aurais-je eu la prétention de **révéler le plan de la Providence**…? Non certes » (L11).
- « Je crois… **non d'une foi soumise et aveugle, car il ne s'agit pas du mystérieux domaine de la révélation, mais d'une foi scientifique et raisonnée** » (L221).
- Truth is warranted by « l'expérience raisonnée… l'universelle pratique » (L1427), « l'universel instinct de l'humanité » (L2355) and « la pratique universelle » (L2893).
- On eschatology he declines to speculate: « faut-il croire, avec le dogme chrétien, à la destruction de ce monde ? Évidemment ce ne sont plus là des problèmes économiques… substituer à un acte de curiosité un acte de confiance » (L2673). On the "pensée divine qui se cache" under solidarity: « **La science humaine l'ignore** » (L3039).
- The "wisdom beyond demonstration" that von Stuckrad identifies as the esoteric epistemic claim (Pico, Reuchlin) is exactly what Bastiat refuses. He even glosses *Fiat lux* as Moses' "impuissance à exprimer", which interposed « l'obstacle d'un mot à prononcer » (L2179). That is the opposite of the Kabbalistic ontology of the creative Word.

**Concealment and disclosure, but the veil is habit, not initiation.**
- Bastiat does speak of hidden order: « une naturelle et savante organisation qui agit **à notre insu** » (L277); « l'accoutumance, **ce voile étendu sur les yeux du vulgaire** » (L2089); « notre esprit a beaucoup de peine à saisir **les négations** » (L2877).
- But the veil is lifted by attention and philosophy (the Rousseau line "il faut beaucoup de philosophie pour observer ce qu'on voit tous les jours", L913, L2089), by anyone.

**Secrecy treated as rent and dissolved.** In von Stuckrad's terms (secrecy as social/symbolic capital, after Simmel, Bourdieu, Urban), Bastiat's economics contains an explicit **theory of secret knowledge as a temporary monopoly** that providence dissolves into the commons:
- the inventor « maître de son secret » holds a free natural agent that is « pas encore commun » (L2827);
- advantage lies in « la connaissance exclusive des procédés » (L2851, L2895);
- competition carries every invention through its « cycle » to « la diffusion universelle, [la] communauté, [la] gratuité » (L2903–2907).

And explicitly:

> « la science, monopolisée par une classe ou même une caste, **voilée par une langue morte ou scellée dans une écriture hiéroglyphique**, s'écrit et s'imprime en langue vulgaire, pénètre… l'atmosphère et se respire comme l'air. » (L2977)

This is an Enlightenment programme for dismantling esoteric capital.

**Polemical othering.** Bastiat actively writes what Hanegraaff calls the "Grand Polemical Narrative":
- Socialists are astrologers and alchemists (L75), reformers who claim a « secret social » (L339), « révélateurs », « prophètes », « pétris d'un autre limon » with a « phraséologie mystique » (L435) and a « ton d'afféterie mystique » (L343). One « prétend avoir **dérobé le secret de Dieu** » (L573).
- Fourier prefixed his Deuteronomy with a « Genèse » (L341), and the Saint-Simonians had « velléités apostoliques » (L341).
- Condillac's explanation of exchange is mocked with Molière's *virtus dormitiva*. Exchange has no « vertu mystérieuse… inaccessible à toute explication » (L893–895), which is the classic mechanist ridicule of occult qualities.
- Talismanic « petites images » and « une bulle d'indulgence plénière » are false values, destined to vanish (L1409, L1503).
- Theocratic spoliation: « prêtres égyptiens, oracles grecs, augures romains, druides gaulois, bramines indiens… jongleurs, sorciers, devins… le génie de la spoliation place son point d'appui dans le ciel… l'esclavage mental » (L3107).

The **Egyptian priests**, whom Ragon's Masonic historiography and the Egyptian rites (Misraïm, Memphis) revered as keepers of initiation (see the *Dictionary* entries *Ragon*, *Illuminism*), appear here as spoliators. The euhemerist handling of myth points the same way:
- agricultural inventors who received « les honneurs de l'apothéose » (L2979);
- « la race de **Cadmus** » and « Triptolème » as mere inventors of letters and the plough (L3003).

In Pernety, Cadmus is the husband of **Harmonia** and an alchemical figure ("changés en serpents", Pernety s.v. *Cadmus*, *Harmonie*). Bastiat, the author of *Harmonies*, invokes Cadmus only as the patron of literacy that competition must make common. This is the reverse of Pernety's *Fables égyptiennes et grecques dévoilées*.

**Where the esoteric–political nexus actually was.** The *Dictionary*'s *Politics and Esotericism* entry locates the association of esotericism with politics in the first half of the nineteenth century on the **socialist** side: Owen, **Pierre Leroux** ("one of the first to use the term *ésotérisme*"), the Saint-Simonians awaiting the feminine Messiah, and Lévi in 1848. Faivre (ch. 4 §I.4) notes Fourier's "involuntary parody" of Swedenborg, "Hortensius Flamel" combining **Fourierism and Hermetism** (1842), and the "illuminated socialism" around 1848–53. Bastiat's named targets (Fourier, Saint-Simon, Owen, Considérant's "association intégrale" and "capital incréé", Proudhon, Cabet, Louis Blanc; L329, L2471–2505, L2805) are precisely that milieu. So is the *solidarité/fraternité* slogan he attacks at L3117, which was Leroux's watchword, though Leroux is not named in the first edition. His book is, among other things, a counter-offensive against the esoterically inflected social theory of 1848.

---

## 6. "Harmonies": the alchemical, esoteric-socialist and Newtonian senses

You note that *harmonie* is "a big one in alchemy". It is, and the contrast is instructive.
- **Pernety (1758).** *Sel harmoniac* is the matter at the white stage, "ainsi appellée de ce que l'harmonie commence à s'établir entre les principes de l'œuvre, qui pendant la putréfaction étoit un cahos plein de confusion". Lull's elixir drives out demons "ennemis de l'ordre, du concert & de l'harmonie" and "remet l'équilibre dans les humeurs". *Harmonie/Hermione* is Cadmus' wife. Harmony is **a stage of the Work** after putrefaction.
- **The esoteric-socialist field of Bastiat's day.**
  - Mesmer's initiatic **Société de l'Harmonie** (1783), with Masonic-style symbols (Faivre, ch. 3 §II.3).
  - Fourier's *Harmonie* (the post-civilisation era).
  - Abbé **Lacuria**'s *Les Harmonies de l'Être exprimées par les nombres* (1844/1847). Lacuria was a Lamennaisian liberal Catholic who "dreamed of a social body kept in equilibrium by the inner regeneration of its members" (*Dictionary*, *Lacuria*).
  - The "many French esotericists whose universal cosmic systems gave an important role to music": Fabre d'Olivet, Fourier, Wronski, Lacuria, Louis Lucas (*Dictionary*, Music IV).
  - Lamartine's *Harmonies poétiques et religieuses* (1830) belongs to the same Romantic climate. Bastiat mocks the lyre ("autant j'aimerais que Lamartine consultât la table des logarithmes", L457).
- **Bastiat's harmony** is Newton's and Kepler's: « les lois harmoniques devant lesquelles s'inclinait Newton » (L441), « les harmonies de la mécanique céleste » (L1197), the astronomer's *Digitus Dei est hic* (L3063).
  - His dissonance is musical-physical. Dissonances « tendent incessamment à disparaître » because error leads to deception and vice to punishment (L497). Evil's intensity decays « comme les **vibrations du son**, comme les oscillations du pendule » (L3039).
  - It is **not** a coincidence of opposites. He rejects Proudhon's claim that contradiction is "dans l'essence même des choses… la loi intime des êtres" (L1747–1749). He insists that property and spoliation can no more be identified « que le oui avec le non, la lumière avec les ténèbres, le bien avec le mal, l'harmonie avec la discordance » (L2065).
  - The Boehmean or Hegelian polarity of being, which is the esoterically genealogised position, belongs to his opponent. Bastiat's "chaos" is only where a pressed error ends (L2799), never a phase of a work.

---

## 7. The posthumous chapters (1851) in brief

Chapters XVIII–XXV of the 1851 and later editions heighten the theological register. They were edited from Bastiat's manuscripts and should be cited as such.
- *Le Mal*: Christ's cup; "L'homme et l'humanité ont leur rédemption. À lui une âme immortelle. À elle une perfectibilité indéfinie".
- *Perfectibilité*: the *imago Dei*; "l'erreur, mère du mal".
- *Solidarité*: original sin and Voltaire.
- *Moteur social*: "Les volontés, comme les molécules inertes, ont leur loi de gravitation… attraction et répulsion", which is close to Fourier's language of attraction.

These deepen the pattern of §2. They do not introduce Hermetic vocabulary. The *Solidarité* chapter's treatment of innocents suffering for others is the one place worth comparing with Joseph de Maistre's Illuminist-Catholic doctrine of *réversibilité*. Maistre was a Rectified Scottish Rite Mason; see *Dictionary*, *Maistre*, on the *Soirées de Saint-Pétersbourg*, "entretiens sur le gouvernement temporel de la Providence". In the first edition, Bastiat raises the same question (« le bonheur d'une région ou d'un siècle… acheté par les souffrances d'un autre… ? ») and answers that "la science humaine l'ignore" (L3039).

*Textual note:* the Institut Coppet 2015 OCR reads "cet être qui n'est perfectible que parce qu'il est **parfait**". The 1850 and 1851 texts read **imparfait** (L3123).

---

## 8. The Masonic channel, reassessed

- **Prior.** Bastiat's membership of *La Zélée* (Bayonne) from c. 1820 is reported by biographers and by Bayonne Masonic historiography. His offices (keeper of the seals 1822, orator 1823) are more weakly sourced. The *Dictionary* shows that the Hermetic strand of French Masonry lived in specific high-degree systems (the Rite Hermétique/Écossais philosophique around Pernety; Misraïm; Memphis), whereas ordinary Grand Orient lodges of the 1820s were deist-liberal.
- **Text.** Nothing indicates the high-degree Hermetic strand. What is present fits the ethos of liberal symbolic lodges, though each item is also ordinary:
  - fraternity as a derived republican value: « Serions-nous frères…? Pourrions-nous nous considérer comme les fils d'un Père commun?… Il ne resterait rien de la devise républicaine » (L2865; cf. « la grande famille », L2259, L2835);
  - a craftsman's God (« divin Ouvrier », « grand Mécanicien »; not the "Grand Architecte");
  - builders' imagery (« architectes… faire le tour de l'édifice », « pierres angulaires », « pierre d'attente », L1191–1193, L1265; « le monde est un vaste atelier », L2185);
  - the **level** (*niveau*) as the recurring telos formula: « approximation constante de tous les hommes vers un niveau qui s'élève toujours » (L221, L441, L1175, L2259, L3061). In Masonic symbolism the Level signifies equality, but Bastiat's first use is hydrostatic (L23);
  - a Voltairean anti-sacerdotalism (L3107).
- **Verdict.** A lodge culture may have shaped Bastiat's moral-political idiom in his twenties, which cannot be excluded. It left no ritual or Hermetic trace in the 1850 text.

---

## 9. Conclusion

1. **The "unusual" elements are genuine and should be read theologically.** *Mal* is evil in the full sense. Value is evil born of the Genesis obstacle, progress is its gradual reduction, and the market order is a providential economy of redemption that lifts humanity « de sa déchéance » toward an unreachable divine gratuity.
2. **These structures are best explained by ordinary, though intense, nineteenth-century Christian-liberal language**, specifically:
   - Genesis/Psalms physico-theology (Fénelon, cited);
   - Leibnizian theodicy (three kinds of evil, dissonance serving harmony);
   - Newtonian/Keplerian harmony;
   - J.-B. Say's economics;
   - the Romantic-humanitarian historicisation of the Fall–rehabilitation narrative (Ballanche → Lamartine/Quinet) that the *Dictionary* describes as the late, secularised afterlife of Illuminist reintegration.

   Only this last layer has an esoteric genealogy. Bastiat receives it at third hand, through the common culture of 1830–48, not from Hermetic or alchemical sources.
3. **Hermetic–alchemical influence is not supported.** The homologies exist (self-limiting evil ~ poison as its own remedy; value annihilated ~ purification of the base; the water cycle ~ distillation; sun, moon, dew, salts, laboratory, veil). But the technical lexicon is absent, and the text repeatedly and explicitly repudiates alchemy, astrology, imagination, occult qualities, secrecy, hieroglyphic learning and priestcraft. The alchemist-operator is cast as Bastiat's opponent. This is a component "common to several forms of thought" (Faivre), not borrowing.
4. **Masonic influence is plausible only as ethos** (fraternity, the level/equality, the craftsman God, anti-priestcraft), consistent with his reported liberal lodge membership and not demonstrable from the text.

**Suggested next steps.**
- *Dictionary* vol. 1 entries: *Alchemy*, *Correspondences*, *Freemasonry*, *Fourier*, *Hermetism*.
- Bernardin de Saint-Pierre, *Harmonies de la nature* (1815).
- Ballanche, *Essais de palingénésie sociale*.
- Leroux, *De l'humanité* (1840) and his concept of *solidarité*.
- Maistre, *Soirées*, on *réversibilité*.
- Lacuria, *Harmonies de l'Être*.
- Bastiat's 1820s correspondence and the *La Zélée* records (BnF, fonds maçonnique).
- For the theological-economic structure, the literature on *oikonomia* and providential government (e.g. G. Agamben, *Il Regno e la Gloria*, 2007). This is not in the uploaded corpus and is flagged for verification.

---

*Files:* `analysis/harmonies_1850_reflowed.txt` (reading text with line numbers) · `analysis/evidence_register.md` (all passages read, by chapter) · `analysis/lexical_profile.py` and `analysis/lexical_profile_output.txt` (reproducible lexical counts).
