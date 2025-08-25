#!/usr/bin/env python3
import sys
from datetime import date
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString


yaml = YAML()
yaml.default_flow_style = False
yaml.allow_unicode = True
yaml.boolean_representation = ['False', 'True']

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

def group_entries(entries):
    """Return entries split into current, previous, and before previous year."""
    current = date.today().year
    previous = current - 1
    groups = {current: [], previous: [], f"Before {previous}": []}
    for e in entries:
        try:
            year = int(e.get('Year'))
        except Exception:
            continue
        if year == current:
            groups[current].append(e)
        elif year == previous:
            groups[previous].append(e)
        else:
            groups[f"Before {previous}"].append(e)
    for items in groups.values():
        items.sort(key=lambda x: int(x.get('Citations') or 0), reverse=True)
    order = [current, previous, f"Before {previous}"]
    return [(label, groups[label]) for label in order if groups[label]]

def write_articles(entries, path):
    sections = group_entries(entries)
    out = []
    for label, items in sections:
        year_items = []
        for e in items:
            item = {
                'Citations': e.get('Citations', ''),
                'DOI': e.get('DOI', ''),
                'Year': e.get('Year'),
                'Citation': LiteralScalarString(article_citation(e)),
            }
            oa_url = e.get('OA URL')
            if oa_url:
                item['OA'] = oa_url
            elif e.get('OA'):
                item['OA'] = True
            year_items.append(item)
        out.append({'Year': label, 'Items': year_items})
    with open(path, 'w') as f:
        yaml.dump(out, f)


def write_conferences(entries, path):
    sections = group_entries(entries)
    out = []
    for label, items in sections:
        year_items = []
        for e in items:
            item = {
                'DOI': e.get('DOI', '') or '',
                'URL': e.get('URL', '') or '',
                'OA URL': e.get('OA URL', '') or '',
                'Citation': LiteralScalarString(conference_citation(e)),
            }
            year_items.append(item)
        out.append({'Year': label, 'Items': year_items})
    with open(path, 'w') as f:
        yaml.dump(out, f)


def write_others(entries, path):
    sections = group_entries(entries)
    out = []
    for label, items in sections:
        year_items = []
        for e in items:
            item = {
                'Type': e.get('Type', '').title(),
                'Citation': LiteralScalarString(other_citation(e)),
            }
            year_items.append(item)
        out.append({'Year': label, 'Items': year_items})
    with open(path, 'w') as f:
        yaml.dump(out, f)

def main(src, outdir):
    with open(src) as f:
        data = yaml.load(f)
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
