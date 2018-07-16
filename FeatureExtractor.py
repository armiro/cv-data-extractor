from DocFileObjects import *


def line_extractor(input_text):
    text_lines = list()
    for page_text in input_text:
        text_lines.append(page_text.split("\n"))
    return text_lines


def line_coupler(text_lines):
    line_couples = list()
    for page_text in text_lines:
        for line_idx in range(0, len(page_text)-1, 2):
            # print(line_idx)
            line_couples.append([page_text[line_idx], page_text[line_idx + 1]])
    return line_couples


def font_extractor(input_text):
    pass


def blocking_feature_extractor(line_couples):
    for line_couple in line_couples:
        pass


lines = line_extractor(raw_text)
# print(raw_text)
# print(lines)
couples = line_coupler(lines)
# print(couples)



