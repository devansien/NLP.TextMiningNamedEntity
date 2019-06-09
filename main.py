import nltk
from nltk.tree import Tree
from nltk import ne_chunk, pos_tag, word_tokenize


def get_continuous_chunks(text):
    sentence_count = 1
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    continuous_chunk = []
    current_chunk = []
    # prev = None

    for i in chunked:
        if str(i[0]) == '.':
            sentence_count += 1
        if type(i) == Tree:
            current_chunk.append(str(sentence_count) + " " + str([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)

    return continuous_chunk


# load text
with open('data/Firearms.txt', 'r') as file:
    txt = file.read().replace('\n', ' ')

# tag, label, and sentence numbers
print(get_continuous_chunks(txt))

# for sent in nltk.sent_tokenize(txt):
#     for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#         if hasattr(chunk, 'label'):
#             print(chunk.label(), ' '.join(c[0] for c in chunk))
