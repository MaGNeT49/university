import re
import urllib.request
import csv

site = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/").read().decode()
pattern = (r"(?:org-widget-header__title-link\">)(?P<names>[^<]+)(?:[^\n]+)(?:[^>]+>)\n\s+(?:(?:<span class=\"org-widget-header__meta\">)[^o]+org-widget-header__meta org-widget-header__meta--location\">|(?:<span class=\"org-widget-header__meta org-widget-header__meta--location\">))\s+(?P<address>[^\n]+)(?:[^Т]+)(?:Телефон</span></dt>\n\s+<dd class=\"spec__value\">)(?P<phones>[^<]+)(?:[^Ч]+\Часы работы)(?:[^>]+>){2}\s+(?:[^>]+>)(?P<work_time>[^<]+)")
matches = re.findall(pattern, site)
lst = []

for match in matches:
    lst.append(match)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['names', 'address', 'phones', 'work_time'])

    for i in lst:
        writer.writerow(i)
