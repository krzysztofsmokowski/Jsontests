import json
import argparse
from urllib import request



class Gists(object):
    def __init__(self, username):
        self.username = username
        self.json_data = self.get_json_data()

    def get_json_data(self):
        with request.urlopen("https://api.github.com/users/{}/gists".format(self.username)) as url:
            return json.loads(url.read().decode())

    def urls(self):
        urls = []
        for data in self.json_data:
            urls.append(data["url"])
        return urls

    def languages(self):
        language_array = []
        for data in self.json_data:
            for filename in data["files"]:
                language_array.append(data["files"][filename]["language"])
        return language_array


    def most_used(self):
        languages_for_files = self.languages()
        list_of_languages = {}
        for language in languages_for_files:
            if language not in list_of_languages:
                list_of_languages[language] = 0
            else:
                list_of_languages[language] = list_of_languages[language]+1
        return max(list_of_languages, key=list_of_languages.get)


    def lang_counter(self, counter):
        language_array = self.languages()
        return language_array.count(counter)

    def files(self):
        files = []
        for data in self.json_data:
            for name in data["files"]:
                files.append(data["files"][name]["filename"])
        return files


    def total_size(self):
        size_array = []
        for data in self.json_data:
            for name in data["files"]:
                size_array.append(data["files"][name]["size"])
        overall_sum = sum(size_array)
        return overall_sum


    def phrase(self, word):
        urls_phrase = []
        for data in self.json_data:
            if data['description']:
                if word in data["description"]:
                    urls_phrase.append(data["url"])
        return urls_phrase


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", action="store_true", help='printing urls')
    parser.add_argument("--languages", action="store_true", help="printing list of programming languages in which user is operating")
    parser.add_argument("--most_used", action="store_true", help="printing most used programming language")
    parser.add_argument("--files", action="store_true", help=" ")
    parser.add_argument("--total_size", action="store_true", help="printing sum of file sizes")
    parser.add_argument("--username", help="Username for listing gists")
    parser.add_argument("--phrase", help="phrase to find in gists description")
    parser.add_argument("--counter", help="counting certain programming language")
    args = parser.parse_args()
    gists = Gists(args.username)
    if args.urls:
        what_to_print = gists.urls()
    if args.languages:
        what_to_print = gists.languages()
    if args.files:
        what_to_print = gists.files()
    if args.total_size:
        what_to_print = gists.total_size()
    if args.phrase:
        what_to_print = gists.phrase(args.phrase)
    if args.most_used:
        what_to_print = gists.most_used()
    if args.counter:
        what_to_print = gists.lang_counter(args.counter)
    print(what_to_print)

if __name__ == '__main__':
    main()
