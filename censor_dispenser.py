# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

def handle_up_low(lst_of_wrds):
  new_lst = []
  for word in lst_of_wrds:
    new_lst.append(word.title())
    new_lst.append(word.upper())
    new_lst.append(word)
  lst_of_wrds = new_lst
  return lst_of_wrds
negative_words = handle_up_low(negative_words)
proprietary_terms = handle_up_low(proprietary_terms)

all_words = negative_words + proprietary_terms

def censor_words_or_lists(email, word_or_lists):
  if type(word_or_lists) == list:
    for words in word_or_lists:
      email = email.replace(words, len(words) * '*')
    return email
  else:
    return email.replace(word_or_lists, len(word_or_lists) * '*')

censor_words_or_lists(email_one, 'learning algorithms')

censor_words_or_lists(email_two, proprietary_terms)

def filter_negative_words(email):
  email = censor_words_or_lists(email, proprietary_terms).split()
  indexes = [email.index(word) for word in negative_words if word in email]
  indexes.sort()
  indexes = indexes[2:len(indexes)]
  words = [email[index] for index in indexes if index != -1]
  return censor_words_or_lists(" ".join(email), words)

filter_negative_words(email_three)

def list_duplicates_of(seq,item):#Found this gem on StackOverflow!
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

def filter_everything(email):
  new_email = email.split()
  loc = [list_duplicates_of(new_email, word) for word in all_words]
  loc2 = [item for item in loc if item != []]
  loc3 = [items for thing in loc2 for items in thing]
  loc4 = [[item, item+1, item-1] for item in loc3]
  indexes = [items for thing in loc4 for items in thing]
  words = [new_email[index] for index in indexes]
  for index in indexes:
    new_email[index] = len(new_email[index])*"*"
  email = " ".join(new_email)
  return email

filter_everything(email_four))