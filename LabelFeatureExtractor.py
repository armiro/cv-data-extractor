test_personal = 'Curriculum Vitae Shahab Teimourimanesh Forskarbacken 3 / room 0232, 104 05 Stockholm, Sweden Mobile: 076 232 1449, E-mail: shahabt@kth.se Date of Birth: September 07, 1982'
test_education = 'Higher Education Master of Science in Engineering Mechanics, GPA: B  Sep 2000 - April 2005          Bachelor’s of Science in Mechanical Engineering-Solid, GPA: 16.00 of 20.00 '
test_personal2 = 'Address: Unit 120, Golshan Tower, Golzar St, Nobonyad Sq, Tehran – Iran Telephone No.:+98-21-22985740 Cell No.:+98-9123389074'
test = 'How ,Are are, ,Are you, You you buddy'
test_work = '➢ Corporation in Design and installation of HEPA filters for HVAC systems in the industrial plant. ➢ Design of air sampling systems from ducts and stack of an Industrial Plant of IRAN. ➢ Administrator of Design, Construction, Installation and Commossioning of Meteorological station of an Industrial Facility. ➢ Investigation of Diffusion of radioactive pollutants from two Industrial Facilities’s Stack (Tehran Research Reactor and Natanz Nuclear Facility). ➢ ICDL teacher of IT center if Zahedan, IRAN (for 6 months) ➢ Familiar with radioactive & Gas Analyzer in job experience such as: •  and  Detectors •  Detectors • Gas Analyzers (O2 , HF and …)'
test_skill = 'Skills Computer Literacy Programming Languages: FORTRAN Developing Tools: AutoCAD, MathCAD, Office, MATLAB, CATIA, ANSYS, MAPLE'


# reading a block's content from a json file received from BlockDetector.py

# not for now

features = ['has_university', 'has_gpa', 'has_email', 'has_prof_name',
            'has_language', 'has_phone_number', 'has_year_number', 'num_of_capital_characters',
            'avg_word_length', 'num_of_commas']


# inputs a content text and returns as many keywords we have, if there is any
# used in various other functions
def keyword_finder(content):
    content = content.lower()
    content = content.split()
    word_dict = dict()
    keywords = list()
    for word in content:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    max_freq = max(word_dict.values())
    if max_freq > 1:
        for item in word_dict.items():
            if item[1] == max_freq:
                keywords.append(item[0])
        return keywords
    else:
        return 'No keywords!'


def has_university(content):
    content = content.lower()
    found = list()
    found.append(content.find('university'))
    found.append(content.find('department'))
    found.append(content.find('faculty'))
    found.append(content.find('institute'))
    return not(all(element == -1 for element in found))


def has_gpa(content):
    content = content.lower()
    found = list()
    found.append(content.find('gpa'))
    found.append(content.find('grade'))
    return not (all(element == -1 for element in found))


def has_email(content):
    content = content.lower()
    found = list()
    found.append(content.find('email'))
    found.append(content.find('e-mail'))
    found.append(content.find('@'))
    return not (all(element == -1 for element in found))


def has_prof_name(content):
    content = content.lower()
    found = list()
    found.append(content.find('dr'))
    found.append(content.find('prof'))
    return not (all(element == -1 for element in found))


def has_language(content):
    content = content.lower()
    found = list()
    found.append(content.find('english'))
    found.append(content.find('persian'))
    return not (all(element == -1 for element in found))


def has_phone_number(content):
    # num = 0
    content = content.lower()
    for word in content.split():
        num = 0
        for char in list(word):
            if char.isdigit():
                num += 1
        if num >= 7:
            # print(word)
            return True
    return False


def has_year_number(content):
    content = content.lower()
    for word in content.split():
        num = 0
        for char in list(word):
            if char.isdigit():
                num += 1
        if num == 4:
            try:
                word = int(word)
                if (word >= 1900) and (word <= 2018):
                    return True
            except:
                pass
    return False


# may helps labeling 'skill' blocks
def num_of_capital_characters(content):
    num = 0
    split = content.split()
    for word in content:
        for char in list(word):
            if char.isupper():
                num += 1
            else:
                pass
    avg = round(num / len(split), 2)
    return avg


# may helps
def avg_word_length(content):
    length = len(content)
    split = content.split()
    num_words = len(split)
    avg_length = round(length / num_words, 2)
    normalized = round(avg_length/longest_word(content), 2)
    return normalized


# used in avg_word_length() function
def longest_word(content):
    content = content.split()
    lengths = list()
    for word in content:
        lengths.append(len(word))
    return max(lengths)


# may helps
def num_of_commas(content):
    content = content.split()
    num = 0
    for word in content:
        is_comma = word is ','
        commas = [char is ',' for char in list(word)]
        has_comma = any(commas) is True
        if is_comma or has_comma:
            num += 1
    avg = round(num / len(content), 2)
    return avg


def num_of_bold_words(content):
    # needs input
    pass


def font_change_frequency(content):
    # needs input
    pass


def size_change_frequency(content):
    # needs input
    pass





