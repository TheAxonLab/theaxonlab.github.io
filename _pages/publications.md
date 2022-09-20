---
title: "AxonLab :: Publications"
layout: publications
excerpt: "AxonLab -- Publications"
sitemap: false
permalink: /publications/
---

# Publications

## Journal publications

{% assign number_printed = 0 %}
{% for year in site.data.pub_journal %}

<p style="font-weight: bold; border-bottom: 1px solid #888; padding: 30px 0 0">{{ year.Year }}</p>
<table>
  {% if number_printed == 0 %}
  <tr style="font-size: small">
    <th>Citation</th>
    <th>Cited by*</th>
  </tr>
  {% endif %}
  {% for entry in year.Items %}
  <tr>
    <td>
      {{ entry.Citation }}
      doi:<a href="https://doi.org/{{ entry.DOI }}">{{ entry.DOI }}</a>{% if entry.OA %}{% else %} (OA){% endif %}.
      {% if entry.OA %}
      <a href="{{ entry.OA }}">OA</a>.
      {% endif %}
    </td>
    <td style="text-align:right">
      {{ entry.Citations }}
    </td>
  </tr>
  {% endfor %}
</table>
{% assign number_printed = number_printed | plus: 1 %}
{% endfor %}

\* Number of citing references extracted from Google Scholar on Aug 11, 2022.


## Conference communications

{% assign number_printed = 0 %}
{% for year in site.data.pub_conference %}

<p style="font-weight: bold; border-bottom: 1px solid #888; padding: 30px 0 0">{{ year.Year }}</p>
<table>
  {% if number_printed == 0 %}
  <tr style="font-size: small">
    <th>Citation</th>
    <th>Cited by*</th>
  </tr>
  {% endif %}
  {% for entry in year.Items %}
  <tr>
    <td>
      {{ entry.Citation }}
    </td>
    <td style="text-align:right">
      n/a
    </td>
  </tr>
  {% endfor %}
</table>
{% assign number_printed = number_printed | plus: 1 %}
{% endfor %}