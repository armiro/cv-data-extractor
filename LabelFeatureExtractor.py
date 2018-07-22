test_personal = 'Curriculum Vitae Shahab Teimourimanesh Forskarbacken 3 / room 0232, 104 05 Stockholm, Sweden Mobile: 076 232 1449, E-mail: shahabt@kth.seDate of Birth: September 07, 1982'
test_education = 'Higher Education Master of Science in Engineering Mechanics, GPA: B  Sep 2000 - April 2005          Bachelor’s of Science in Mechanical Engineering-Solid, GPA: 16.00 of 20.00 '
test_personal2 = 'Address: Unit 120, Golshan Tower, Golzar St, Nobonyad Sq, Tehran – Iran Telephone No.:+98-21-22985740 Cell No.:+98-9123389074'
test = 'How Are are Are you You you buddy'

# reading a block's content from a json file received from BlockDetector.py

# not for now

features = ['is_first', 'has_university', 'has_GPA', 'has_DrOrProf']


# inputs a content text and returns as many keywords we have, if there is any
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


t = has_year_number(test_education)
print(t)

