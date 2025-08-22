#!/usr/bin/env python3
import sys
import yaml
from collections import defaultdict, OrderedDict

def short_authors(authors):
    """Return shortened author list: first, … last."""
    if not authors:
        return ""
    def fmt(name):
        parts = [p.strip() for p in name.split(',')]
        if len(parts) == 2:
            last, firsts = parts
            initials = ''.join(f"{w.strip()[0]}." for w in firsts.split())
            return f"{last}, {initials}"
        return name
    if len(authors) == 1:
        return fmt(authors[0])
    return f"{fmt(authors[0])}, … {fmt(authors[-1])}"

def article_citation(e):
    pub = e.get('AbbrvPublication') or e.get('Publication', '')
    vol = e.get('Volume')
    num = e.get('Number')
    pages = e.get('Pages')
    citation = (
        f"{short_authors(e.get('Authors', []))} ({e.get('Year')}).\n"
        f"      {e.get('Title')}\n"
        f"      <i>{pub}</i>"
    )
    if vol:
        citation += f" {vol}"
    if num:
        citation += f"({num})"
    if pages:
        citation += f":{pages}"
    citation += "."
    return citation

def conference_citation(e):
    pub = e.get('AbbrvPublication') or e.get('Publication', '')
    volume = e.get('Volume')
    pages = e.get('Pages')
    place = e.get('Place')
    citation = (
        f"{short_authors(e.get('Authors', []))} ({e.get('Year')}).\n"
        f"      {e.get('Title')}\n"
        f"      <i>{pub}</i>"
    )
    if volume:
        citation += f" {volume}"
    if pages:
        citation += f", {pages}"
    if place:
        citation += f",\n      {place}"
    citation += "."
    return citation

def other_citation(e):
    pub = e.get('AbbrvPublication') or e.get('Publication', '')
    vol = e.get('Volume')
    num = e.get('Number')
    pages = e.get('Pages')
    citation = (
        f"{short_authors(e.get('Authors', []))} ({e.get('Year')}).\n"
        f"      {e.get('Title')}\n"
        f"      <i>{pub}</i>"
    )
    if vol:
        citation += f" {vol}"
    if num:
        citation += f"({num})"
    if pages:
        citation += f":{pages}"
    citation += "."
    return citation

def group_by_year(entries):
    grouped = defaultdict(list)
    for e in entries:
        year = e.get('Year')
        try:
            year = int(year)
        except Exception:
            pass
        grouped[year].append(e)
    return OrderedDict(sorted(grouped.items(), key=lambda x: x[0], reverse=True))

class LiteralDumper(yaml.SafeDumper):
    pass

def str_presenter(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

LiteralDumper.add_representer(str, str_presenter)

def bool_presenter(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:bool', 'True' if data else 'False')

LiteralDumper.add_representer(bool, bool_presenter)

def write_articles(entries, path):
    years = group_by_year(entries)
    out = []
    for year, items in years.items():
        year_items = []
        for e in items:
            item = {
                'Citations': e.get('Citations', ''),
                'DOI': e.get('DOI', ''),
                'Year': e.get('Year'),
                'Citation': article_citation(e),
            }
            oa_url = e.get('OA URL')
            if oa_url:
                item['OA'] = oa_url
            elif e.get('OA'):
                item['OA'] = True
            year_items.append(item)
        out.append({'Year': year, 'Items': year_items})
    with open(path, 'w') as f:
        yaml.dump(out, f, Dumper=LiteralDumper, sort_keys=False, allow_unicode=True)

def write_conferences(entries, path):
    years = group_by_year(entries)
    out = []
    for year, items in years.items():
        year_items = []
        for e in items:
            item = {
                'DOI': e.get('DOI', '') or '',
                'URL': e.get('URL', '') or '',
                'OA URL': e.get('OA URL', '') or '',
                'Citation': conference_citation(e),
            }
            year_items.append(item)
        out.append({'Year': year, 'Items': year_items})
    with open(path, 'w') as f:
        yaml.dump(out, f, Dumper=LiteralDumper, sort_keys=False, allow_unicode=True)

def write_others(entries, path):
    years = group_by_year(entries)
    out = []
    for year, items in years.items():
        year_items = []
        for e in items:
            item = {
                'Type': e.get('Type', ''),
                'Citation': other_citation(e),
            }
            year_items.append(item)
        out.append({'Year': year, 'Items': year_items})
    with open(path, 'w') as f:
        yaml.dump(out, f, Dumper=LiteralDumper, sort_keys=False, allow_unicode=True)

def main(src, outdir):
    with open(src) as f:
        data = yaml.safe_load(f)
    articles, conferences, others = [], [], []
    for e in data:
        t = e.get('Type', '').lower()
        if t == 'article':
            articles.append(e)
        elif t in {'poster', 'oral'}:
            conferences.append(e)
        else:
            others.append(e)
    write_articles(articles, f"{outdir}/pub_journal.yml")
    write_conferences(conferences, f"{outdir}/pub_conference.yml")
    write_others(others, f"{outdir}/pub_other.yml")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: update_publications.py <source_yml> <output_dir>')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
