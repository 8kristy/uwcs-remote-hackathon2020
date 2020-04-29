from sklearn.feature_extraction.text import HashingVectorizer
import textblob, string

# most of this stuff is taken from here https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/

# needed when counting word families
pos_family = {
    'noun' : ['NN','NNS','NNP','NNPS'],
    'pron' : ['PRP','PRP$','WP','WP$'],
    'verb' : ['VB','VBD','VBG','VBN','VBP','VBZ'],
    'adj' :  ['JJ','JJR','JJS'],
    'adv' : ['RB','RBR','RBS','WRB']
}

# function to check and get the part of speech tag count of a words in a given sentence
def check_pos_tag(x, flag):
    cnt = 0
    try:
        wiki = textblob.TextBlob(x)
        for tup in wiki.tags:
            ppo = list(tup)[1]
            if ppo in pos_family[flag]:
                cnt += 1
    except:
        pass
    return cnt

# all vectors to be returned
hashes, counts, word_family_counts = [], [], []

# calcualtes all the hashes
def getData(title, content):
    # hashes the content into a 100 feature vector
    hashes.append(HashingVectorizer(n_features=100).transform([content]).toarray()[0])

    # preforms counts on the title
    title_char_count = len(title)
    title_word_count = len(title.split())
    title_word_density = title_char_count/(title_word_count + 1)
    title_punctuation_count = sum([1 for x in title if x in string.punctuation])
    title_upper_count = len([wrd for wrd in title.split() if wrd.isupper()])

    # preforms counts on the content
    char_count = len(content)
    word_count = len(content.split())
    word_density = char_count/(word_count + 1)
    punctuation_count = sum([1 for x in content if x in string.punctuation])
    upper_count = len([wrd for wrd in content.split() if wrd.isupper()])

    counts.append([title_char_count, title_word_count, title_word_density, title_punctuation_count, title_upper_count, char_count, word_count, word_density, punctuation_count, upper_count])

    # looks for words in the title
    title_nouns = check_pos_tag(title, 'noun')
    title_prons = check_pos_tag(title, 'pron')
    title_verbs = check_pos_tag(title, 'verb')
    title_adjs  = check_pos_tag(title, 'adj')
    title_advs  = check_pos_tag(title, 'adv')

    # looks for words in the content
    nouns = check_pos_tag(content, 'noun')
    prons = check_pos_tag(content, 'pron')
    verbs = check_pos_tag(content, 'verb')
    adjs  = check_pos_tag(content, 'adj')
    advs  = check_pos_tag(content, 'adv')

    word_family_counts.append([title_nouns, title_prons, title_verbs, title_adjs, title_advs, nouns, prons, verbs, adjs, advs])
    
    return hashes, counts, word_family_counts
