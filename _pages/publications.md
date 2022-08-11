---
title: "AxonLab :: Publications"
layout: publications
excerpt: "AxonLab -- Publications"
sitemap: false
permalink: /publications/
---

# Publications

## Journal publications

<table>
  <tr>
    <th>Citation</th>
    <th style="width: 200px">Cited by</th>
  </tr>
</table>

{% assign number_printed = 0 %}
{% for year in site.data.pub_journal %}

<p style="font-weight: bold">{{ year.Year }}</p>

<table>
  {% for entry in year.Items %}
  <tr>
    <td>
      {{ entry.Citation }} doi:<a href="https://doi.org/{{ entry.DOI }}">{{ entry.DOI }}</a>
    </td>
    <td style="text-align:right">
      {{ entry.Citations }}
    </td>
  </tr>
  {% endfor %}
</table>
{% endfor %}
