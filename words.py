import os
import errno
import pdfplumber
import string
import json
import matplotlib.pyplot as plt
from collections import Counter

class MostUsed:
    def __init__(self, book_path='books', list_path="list.json"):
        self.book_path = book_path
        self.list_path = list_path

    def del_list(self):
        if os.path.exists(self.list_path):
            os.remove(self.list_path)
            print(f"{self.list_path} silindi")
        else:
            print(f"{self.list_path} doesn't exist already. Continuing...")

    def pdf2json(self):
        try:
            if len(os.listdir(self.book_path)) == 0:
                print(f'{self.book_path} is empty. Continuing...')
                return 0
        except:
            error = FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.book_path)
            raise error

        if not os.path.exists("./books_done"):
           os.mkdir("./books_done")
        for book in os.listdir(self.book_path): 
            print(f'{book} is being read')
            with pdfplumber.open(os.path.join(self.book_path,book)) as file:
                total = []
                words = []
                for i in range(len(file.pages)):
                    total = total + [file.pages[i].extract_text()]
            total = filter(None, total)
            for i in total:
                words.append(i.translate(str.maketrans('', '', string.punctuation)).lower().split())
            if os.path.exists(self.list_path):
                with open(self.list_path, 'r+') as file:
                    old_data=json.load(file)
                    old_data.extend(words)
                    file.seek(0)
                    json.dump(old_data, file, indent = 4)
            else:
                with open(self.list_path, 'w') as file:
                    json.dump(words, file, indent = 4)
            os.replace(f'{self.book_path}/{book}',f'./books_done/{book}')
            print(f'{book} is done')

    def check_freq_alt(self, n = 20): 
        '''
        As I did't know the Counter method i wrote this function then I found out Counter method. When I compared their performances with timeit.timeit() Counter was slightly better than my function so I kept both buth used Counter mainly.
        '''
        with open(self.list_path, 'r') as file:
            words = json.load(file)
        freq = {}
        for j in words:
            for i in j:
                if i in freq:
                    freq[i] += 1
                else:
                    freq.update({i: 1})
        freq=dict(sorted(freq.items(), key = lambda item: item[1]))
        return list(freq.items())[-n:]

    def check_freq(self, n=20):
        with open(self.list_path, 'r') as file:
            words = json.load(file)
        freq = Counter()
        for i in words:
            freq.update(i)
        return freq.most_common(n)


    def graph(self, n=20):
        freq = self.check_freq(n)
        plt.bar(*zip(*freq))
        plt.show()


if __name__=="__main__":
    words = MostUsed()
    words.del_list()
    words.pdf2json()
    w2=words.check_freq_alt(5)
    w=words.check_freq(25)
    words.graph(15)
    print(w)
