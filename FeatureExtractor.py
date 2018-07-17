from DocFileObjects import *
from stemming.porter2 import stem

test_text = [
    [['CURRICULUM VITAE', 'TimesNewRoman-Bold', 12]],
    [['Name:', 'TimesNewRoman-Bold', 12], ['Johanneke Marie VAN DALE (Janneke)', 'TimesNewRoman-Regular', 10]],
    [['Address:', 'TimesNewRoman-Bold', 12], ['Breestraat 21', 'TimesNewRoman-Regular', 10]],
    [['2311 AB LEIDEN', 'TimesNewRoman-Regular', 10]],
    [['the Netherlands.', 'TimesNewRoman-Regular', 10]],
    [['Telephone: ', 'TimesNewRoman-Bold', 12], ['+31 71 5126511', 'TimesNewRoman-Regular', 10]]
]
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
    'academ', 'activ', 'research', 'articl', 'present', 'lectur', 'patent', 'paper', 'public', 'these', 'thesi',
    # work experiences
    'work', 'employ', 'project', 'compet', 'teach',
    # languages
    'languag',
    # honors and awards
    'honor', 'achiev', 'certif', 'reward', 'award',
    # others
    'refer', 'membership', 'interest', 'sport', 'hobbi', 'object', 'goal',  'literacy', 'histori'
    ]


# deprecated function, no need to use:
def line_extractor(input_text):
    text_lines = list()
    for page_text in input_text:
        text_lines.append(page_text.split("\n"))
    return text_lines
# deprecated function ended.


def line_cleaner(input_text):
    cleared_text = list()
    for text_line in input_text:
        for text_part in text_line:
            text_part[0] = text_part[0].strip()
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
    capital = list()
    dot = list()

    for line_couple in line_couples:
        first_line = line_couple[0]
        second_line = line_couple[1]

        # font change
        if first_line[-1][1] == second_line[0][1]:
            font_change.append(False)
        else:
            font_change.append(True)

        # font size change
        if first_line[-1][2] > second_line[0][2]:
            size_change.append(-1)
        elif first_line[-1][2] < second_line[0][2]:
            size_change.append(1)
        else:
            size_change.append(0)

        # first line's last element is a dot
        if len(first_line[-1][0]):
            print(first_line[-1][0])
            print(first_line[-1][0][-1])
            if first_line[-1][0][-1] == '.':
                dot.append(True)
        else:
            dot.append(False)

    return dot, capital, font_change, size_change


cleared_text = line_cleaner(raw_text)
coupled_text = line_coupler(cleared_text)
dot, capital, font_change, size_change = blocking_feature_extractor(coupled_text)
print(dot)
print(raw_text[2][0][-1] == '.')

