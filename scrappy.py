import requests, bs4, re

url = requests.get('https://secure.tibia.com/community/?subtopic=worlds&world=Unitera')
zupka = bs4.BeautifulSoup(url.text, 'lxml')
print(type(zupka))
string_zupka = str(zupka)
print(type(string_zupka))
html_elements = zupka.findAll("tr", class_="Odd")
html_elements.extend(zupka.findAll("tr", class_="Even"))
#names_regex = re.findall(r'')
counter = 0
for element in html_elements:
    #print(element)
    match = re.search(r'name=([a-zA-Z+]+).*>(\d{1,3})<', str(element))
    if match:
        level = int(match.group(2))
        if level < 100 and level > 8:
            print(match.group(1).replace('+', ' '), match.group(2))
            counter+=1
    else:
        print(element)
print(counter)
#print(zupka2[5])

#<tr class="Even" style="text-align:right;"><td style="width:70%;text-align:left;"><a href="https://secure.tibia.com/community/?subtopic=characters&amp;name=Zuczkinns+Antica">Zuczkinns Antica</a></td><td style="width:10%;">7</td><td style="width:20%;">Sorcerer</td></tr>

