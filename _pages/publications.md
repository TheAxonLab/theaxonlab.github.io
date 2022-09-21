---
title: "AxonLab :: Publications"
layout: default
excerpt: "AxonLab -- Publications"
sitemap: false
permalink: /publications/
---

# Publications

<div class="accordion accordion-flush" id="accordionPublications">
<div class="accordion-item">
<h2 class="accordion-header" id="flush-headingOne">
<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
Journal publications
</button>
</h2>
<div id="flush-collapseOne" class="accordion-collapse collapse show" aria-labelledby="flush-headingOne" data-bs-parent="#accordionPublications">
<div class="accordion-body">
{% assign number_printed = 0 %}
{% for year in site.data.pub_journal %}
<p style="font-weight: bold; border-bottom: 1px solid #888; padding: 30px 0 0">{{ year.Year }}</p>      
<table class="table table-striped table-hover table-borderless table-sm">
<caption>Number of citing references extracted from Google Scholar on Aug 11, 2022.</caption>
{% if number_printed == 0 %}
<tr style="font-size: small">
<th>Citation</th>
<th>Cited by*</th>
</tr>
{% endif %}
<tbody class="table-group-divider">
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
</tbody>
</table>
{% assign number_printed = number_printed | plus: 1 %}
{% endfor %}
</div>
</div>
</div>

<div class="accordion-item">
<h2 class="accordion-header" id="flush-headingTwo">
<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
Conference communications
</button>
</h2>
<div id="flush-collapseTwo" class="accordion-collapse collapse" aria-labelledby="flush-headingTwo" data-bs-parent="#accordionPublications">
<div class="accordion-body">
{% assign number_printed = 0 %}
{% for year in site.data.pub_conference %}

<p style="font-weight: bold; border-bottom: 1px solid #888; padding: 30px 0 0">{{ year.Year }}</p>
<table class="table table-striped table-hover table-borderless table-sm">
<caption>Number of citing references extracted from Google Scholar on Aug 11, 2022.</caption>
{% if number_printed == 0 %}
<tr style="font-size: small">
<th>Citation</th>
<th>Cited by*</th>
</tr>
{% endif %}
<tbody class="table-group-divider">
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
</tbody>
</table>
{% assign number_printed = number_printed | plus: 1 %}
{% endfor %}
</div>
</div>
</div>
</div>
