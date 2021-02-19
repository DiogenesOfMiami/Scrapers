from string import ascii_lowercase

def MIT_to_standard(filename):
    """
    Scrapes words from MIT style file (all words in one line). 
    
    Takes filename (including extension) as argument.

    Returns list of words in standard format (one word per line).
    """
    print("Scraping words from " + filename + " ...")
    # all_words: file
    with open(filename, 'r') as f:
    # line: string
        line = f.readline()
    # wordlist: list of strings
    wordlist = line.split()

    with open('new_'+ filename, 'w') as f:
        for item in wordlist:
            f.write("%s\n" % item)

def words_to_list(filename):
    """
    Scrapes words from file (one word per line). 
    
    Takes filename (including extension) as argument.

    Returns list of words.
    """
    print("Scraping words from file...")
    # all_words: file
    with open('words.txt') as all_words:
    # line: string
        line = all_words.readline()
    # wordlist: list of strings
    wordlist = line.split()
    new_wordlist = []
    no_wordlist = []
    
    with open(filename) as sp_words:

        for line in sp_words:
            sp_line = sp_words.readline()
            sp_list = sp_line.split()
            
            for word in sp_list:
                new_word = ''
                for letter in word.lower():
                    if letter in ascii_lowercase:
                        new_word = new_word + letter
                if new_word in wordlist:
                    new_wordlist.append(new_word)
                else:
                    if new_word in no_wordlist or new_word in new_wordlist:
                        continue
                    else:
                        selection = input("Add '" + new_word + "' ? Y/N: ")
                        if selection is 'y' or selection is 'Y':
                            new_wordlist.append(new_word)
                        else:
                            no_wordlist.append(new_word)

    new_wordlist = list(set(new_wordlist))

    print("  ", len(new_wordlist), "words scraped.")

    with open('new_wordlist.txt', 'w') as f:
        for item in new_wordlist:
            f.write("%s\n" % item)
    
    # print("New wordlist:", new_wordlist)
    # print("Omitted words:", no_wordlist)
    return new_wordlist

def url_scraper(URL):
    '''
    Takes string as desired URL.

    Returns full HTML of website.
    '''
    import urllib.request
    with urllib.request.urlopen(URL) as u:
	    lines = u.read()
	    return str(lines)

def html_scraper(HTML):
    '''
    Takes one line HTML string (via url_scraper).

    Returns text of embedded lists (starting at <ul><li>).
    '''
    writing = False
    tagscan = False
    tag = ''
    current_tags = {}
    return_string = ''
    for char in HTML:

        if tagscan == True:
            tag = tag+char

        if char == '<':
            tagscan = True
            tag = char
        elif char == '>':
            tagscan = False
            if '/' in tag:
                if tag.replace('/', '') in current_tags:
                    current_tags[tag.replace('/', '')] -= 1
                else:
                    current_tags[tag.replace('/', '')] = -1
            else:
                if tag in current_tags:
                    current_tags[tag] += 1
                    print(tag, current_tags[tag])                           #Debug printing
                else:
                    current_tags[tag] = 1
                    print(tag, current_tags[tag])                           #Debug printing
            tag = ''

        if writing == True:
            return_string = return_string+char
        
        if '<ul>' in current_tags and current_tags['<ul>'] == 1 and '<li>' in current_tags and current_tags['<li>'] == 1:
            writing == True
        else:
            writing == False

    return return_string

#Uncomment for final test:
#print(html_scraper(url_scraper('https://spongebob.fandom.com/wiki/Help_Wanted/transcript')))

print(html_scraper('abc\n<ul><li><b>French Narrator:</b> Ah, the sea... so fascinating. So wonderful. Here, we see Bikini Bottom, teeming with life. <i>[shows from left to right Patrick\'s, Squidward\'s, and SpongeBob\'s houses. Zooms in on SpongeBob\'s house.]</i> Home to one of my favorite creatures, SpongeBob SquarePants. Yes, of course he lives in a'))