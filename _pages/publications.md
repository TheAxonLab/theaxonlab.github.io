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

### {{ year.Year }}

<table>
  <tr>
    <th>Citation</th>
    <th>Cited by</th>
  </tr>
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
