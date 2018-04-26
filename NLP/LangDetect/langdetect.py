from collections import Counter
def tokenize(chain):
    return chain.split(' ')


def get_text_ngrams(word, amount):
    length = len(word)
    if(length<amount):
        return [word]
    finals = []
    for i in range(length-amount+1):
        finals.append(word[i:i+amount])
    return finals

def get_words_from_file(filepath):
    with open(filepath) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    return content

def get_ngrams_from_file(filename, n):
    lang_tokens = get_words_from_file(filename)
    end_ngrams = []
    for i in lang_tokens:
        end_ngrams += (get_text_ngrams(i,n))
    return end_ngrams
# res = get_text_ngrams("My name is manuel".replace(" ","#"), 2)
# print(res)

##LOAD ALL RELEVANT LANGUAGES

def calculate_text_lang_with_ngrams(text, n_size):
    esp_ngrams= get_ngrams_from_file("espanol.txt",n_size)
    print("NGrams in spanish: ",len(esp_ngrams))
    esp_cnt = Counter(esp_ngrams)
    print(esp_cnt.most_common(10),"\n")

    eng_ngrams= get_ngrams_from_file("usa.txt",n_size)
    print("NGrams in english: ",len(eng_ngrams))
    eng_cnt = Counter(eng_ngrams)
    print(eng_cnt.most_common(10),"\n")

    ger_ngrams= get_ngrams_from_file("deutsch.txt",n_size)
    print("NGrams in german: ",len(ger_ngrams))
    ger_cnt = Counter(ger_ngrams)
    print(ger_cnt.most_common(10),"\n")

    fra_ngrams= get_ngrams_from_file("francais.txt",n_size)
    print("NGrams in french: ",len(fra_ngrams))
    fra_cnt = Counter(fra_ngrams)
    print(fra_cnt.most_common(10),"\n")

    text_ngrams = []
    for i in tokenize(text):
        text_ngrams+=get_text_ngrams(i,n_size)
    print(text_ngrams)


    fra_total =0
    eng_total =0
    esp_total =0
    deu_total =0
    for i in text_ngrams:
        fra_total += fra_cnt[i] / len(fra_ngrams)
        esp_total += esp_cnt[i] / len(esp_ngrams)
        deu_total += ger_cnt[i] / len(ger_ngrams)
        eng_total += eng_cnt[i] / len(eng_ngrams)

    total = fra_total+esp_total+deu_total+eng_total
    print("Francais score:",fra_total, (fra_total/total)*100)
    print("Espanol score:",esp_total, (esp_total/total)*100)
    print("English score:",eng_total, (eng_total/total)*100)
    print("Deutsch score:",deu_total, (deu_total/total)*100)

