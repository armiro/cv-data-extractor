from DocFile import DocFile
from stemming.porter2 import stem
# from stemming.paicehusk import stem
import json
import pandas as pd
import ast


for f in range(1, 234):
    path = 'CV (%d).pdf' % f
    one = DocFile(path)
    raw_text = one.pdf2textlines()
    # test_text = [
    #     [['CURRICULUM VITAE', 'TimesNewRoman-Bold', 12]],
    #     [['Name:', 'TimesNewRoman-Bold', 12], ['Johanneke Marie VAN DALE (Janneke)', 'TimesNewRoman-Regular', 10]],
    #     [['Address:', 'TimesNewRoman-Bold', 12], ['Breestraat 21', 'TimesNewRoman-Regular', 10]],
    #     [['2311 AB LEIDEN', 'TimesNewRoman-Regular', 10]],
    #     [['the Netherlands.', 'TimesNewRoman-Regular', 10]],
    #     [['Telephone: ', 'TimesNewRoman-Bold', 12], ['+31 71 5126511', 'TimesNewRoman-Regular', 10]]
    # ]

    # print(stem('scientific'))
    # extracted stemmed keywords happening frequently in CV/Resume files
    block_starting_keywords = [
        # personal information
        'contact', 'info', 'person', 'about', 'social', 'societi',
        # education and scientific background
        'educ', 'qualif', 'background', 'scientif', 'field',
        # skills
        'experi', 'skill', 'profession', 'profess', 'workshop',
        # academic activities
        'academ', 'activ', 'research', 'articl', 'lectur', 'patent', 'paper', 'public', 'these', 'thesi', 'present',
        # work experiences
        'work', 'employ', 'compet', 'teach', 'journal', 'book',
        # languages
        'languag',
        # honors and awards
        'honor', 'achiev', 'certif', 'reward', 'award',
        # others
        'refer', 'membership', 'interest', 'sport', 'hobbi', 'object', 'goal',  'literacy', 'histori'
        ]

    # deprecated block-starting-words: 'present', 'project'


    # deprecated function, no need to use:
    def line_extractor(input_text):
        text_lines = list()
        for page_text in input_text:
            text_lines.append(page_text.split("\n"))
        return text_lines
    # deprecated function ended.


    def line_cleaner(input_text):
        for text_line in input_text:
            for text_part in text_line:
                text_part[0] = text_part[0].strip()
                if len(text_part[0]):
                    if text_part[0].endswith(':'):
                        text_part[0] = text_part[0][:-1]
        return input_text


    def line_coupler(text_lines):
        line_couples = list()
        for line_idx in range(0, len(text_lines)-1, 1):
            # print(line_idx)
            line_couples.append([text_lines[line_idx], text_lines[line_idx + 1]])
        return line_couples


    def blocking_feature_extractor(line_couples):
        font_change = list()
        size_change = list()
        has_dot = list()
        has_keyword = list()
        content = line_couples

        feature_dict = list()
        found = False

        # feature_values = [content, font_change, size_change, has_dot, has_keyword, label]
        feature_keys = ['content', 'font_change', 'size_change', 'has_dot', 'has_keyword', 'label']

        for line_couple in line_couples:
            first_line = line_couple[0]
            second_line = line_couple[1]

            if first_line and second_line:

                # font change
                if first_line[-1][1] == second_line[0][1]:
                    font_change.append(0)
                else:
                    font_change.append(1)

                # font size change
                if first_line[-1][2] > second_line[0][2]:
                    size_change.append(-1)
                elif first_line[-1][2] < second_line[0][2]:
                    size_change.append(1)
                else:
                    size_change.append(0)

                # first line's last element is a dot
                if len(first_line[-1][0]):
                    if first_line[-1][0][-1] == '.':
                        has_dot.append(1)
                    else:
                        has_dot.append(0)
                else:
                    has_dot.append(0)

                # first line's first word is a block-starting-keyword
                target_words = first_line[0][0].split()
                for target_word in target_words:
                    target_word = stem(target_word.lower())
                    for block_starting_keyword in block_starting_keywords:
                        if target_word == block_starting_keyword.lower():
                            has_keyword.append(1)
                            # print(target_word)
                            found = True
                            # break
                    # if a title has more than one keyword, just consider the first!
                    if found is True:
                        break
                if found is False:
                    has_keyword.append(0)
                found = False
            else:
                has_keyword.append(0)
                has_dot.append(0)
                font_change.append(0)
                size_change.append(0)

        label = [0] * len(has_keyword)
        for index in range(0, len(label)):
            this_record = [content[index], font_change[index], size_change[index], has_dot[index],
                            has_keyword[index], label[index]]
            this_record = pd.Series(this_record, index=feature_keys)
            this_record = this_record.to_json(orient='index')
            this_record = ast.literal_eval(this_record)
            feature_dict.append(this_record)
        return feature_dict


    # main code, receives raw-text extracted from PDF file and returns the features
    # if __name__ == '__main__':

    cleared_text = line_cleaner(raw_text)
    coupled_text = line_coupler(cleared_text)
    block_detection_features = blocking_feature_extractor(coupled_text)

    # print(len(raw_text))
    # print(len(cleared_text)) # should be len(raw_text) - 1
    # print(len(coupled_text)) # should be len(raw_text) - 1
    # print(len(block_detection_features)) # should be 6
    # print(coupled_text)
    # print(block_detection_features)

    with open('blocks/Blocks%d.json' % f, 'w+') as file:
        json.dump(block_detection_features, file, indent=2)
    file.close()
