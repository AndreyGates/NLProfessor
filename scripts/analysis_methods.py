from natasha_parser import Natasha_Parser

nap = Natasha_Parser('./test/test.txt')
nap.segmentation()

nap.morphology()
nap.doc.sents[0].morph.print()

nap.syntax()
nap.doc.sents[0].syntax.print()