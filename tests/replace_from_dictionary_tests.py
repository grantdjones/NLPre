from nose.tools import *
from nlpre import replace_from_dictionary
import os


class Replace_From_Dictionary_Test:

    @classmethod
    def setup_class(cls):
        MeSH_dict = "dictionaries/"
        local_dir = os.path.dirname(os.path.abspath('nlpre/dictionaries'))
        f_MeSH = os.path.join(
            local_dir,
            MeSH_dict,
            'MeSH_two_word_lexicon.csv')
        cls.replace_MeSH = replace_from_dictionary(f_MeSH, prefix='MeSH_')

    def bad_dictionary_test(self):
        mesh_dict = "dictionaries/"
        local_dir = os.path.dirname(os.path.abspath('nlpre/dictionaries'))
        path_to_meshdict = os.path.join(local_dir, mesh_dict)

        assert_raises(IOError, replace_from_dictionary,
                      'MeSH_two_word_lexicon1.csv', path_to_meshdict)

    def default_dictionary_test(self):
        ''' Use the default dictionary if one is missing. '''
        MeSH = replace_from_dictionary(prefix='MeSH_')

        doc = '0-beta-Hydroxyethylrutoside is great'
        doc_right = 'MeSH_Hydroxyethylrutoside is great'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def hydroxyethylrutoside_test1(self):
        doc = '0-beta-Hydroxyethylrutoside is great'
        doc_right = 'MeSH_Hydroxyethylrutoside is great'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def hydroxyethylrutoside_test2(self):
        doc = '0 beta Hydroxyethylrutoside is great'
        doc_right = 'MeSH_Hydroxyethylrutoside is great'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def pandemic_test(self):
        doc = '1918-1919 Influenza Pandemic was awful'
        doc_right = 'MeSH_Influenza_Pandemic_1918-1919 was awful'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    # fails because periods are split on
    # def period_test(self):
    #    doc = '19th Cent. History of Medicine was a good century'
    #    doc_right = 'MeSH_History_19th_Century was a good century'
    #    doc_new = self.replace_MeSH(doc)

    #    assert_equal(doc_right, doc_new)

    def dimethylethyl_test(self):
        doc = '(11-Dimethylethyl)-4-methoxyphenol is great'
        doc_right = 'MeSH_Butylated_Hydroxyanisole is great'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def dimethylethyl_test(self):
        doc = '(11-Dimethylethyl)-4-methoxyphenol'
        doc_right = 'MeSH_Butylated_Hydroxyanisole'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def dimethylethyl_parens_test(self):
        doc = '((11-Dimethylethyl)-4-methoxyphenol).'
        doc_right = '(MeSH_Butylated_Hydroxyanisole).'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def multiple_paranthesis_test(self):
        doc = '((2-Hexahydro-1(2H)-azocinyl)ethyl)guanidine is tasty'
        doc_right = 'MeSH_Guanethidine is tasty'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def extra_paranthesis_test(self):
        doc = '(((2-Hexahydro-1(2H)-azocinyl)ethyl)guanidine) is tasty'
        doc_right = '(MeSH_Guanethidine) is tasty'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def methyl_test(self):
        doc = '3-Methyl-2-Oxobutanoate Dehydrogenase (Lipoamide) is tasty'
        doc_right = 'MeSH_3-Methyl-2-Oxobutanoate_Dehydrogenase_(Lipoamide) is tasty'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def mesh_middle_sentence(self):
        doc = 'I think that 3-Methyl-2-Oxobutanoate Dehydrogenase (Lipoamide) is tasty'
        doc_right = 'I think that MeSH_3-Methyl-2-Oxobutanoate_Dehydrogenase_(Lipoamide) is tasty'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def punctuation_after_mesh(self):
        doc = 'I think that 3-Methyl-2-Oxobutanoate Dehydrogenase (Lipoamide), a chemical, is tasty'
        doc_right = 'I think that MeSH_3-Methyl-2-Oxobutanoate_Dehydrogenase_(Lipoamide), a chemical, is tasty'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def apostrophe_test(self):
        doc = "3' 5' Exonuclease is tasty"
        doc_right = 'MeSH_Exonucleases is tasty'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def plus_test(self):
        doc = "Abscisic Acid (+-)-Isomer is tasty"
        doc_right = 'MeSH_Abscisic_Acid is tasty'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)

    def colon_test(self):
        doc = "Acetylcholine Sulfate (1:1) is tasty"
        doc_right = 'MeSH_Acetylcholine is tasty'
        doc_new = self.replace_MeSH(doc)

        assert_equal(doc_right, doc_new)
