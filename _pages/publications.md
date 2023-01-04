---
title: "AxonLab :: Scientific outcomes and publications"
layout: default
excerpt: "AxonLab -- Scientific outcomes and publications"
sitemap: false
permalink: /publications/
---

# Scientific outputs

Below we list the most outstanding communications our lab has produced, next to the number of citations if applicable.
Number of citing references extracted from Google Scholar on Jan 4, 2023.
  
<div class="accordion accordion-flush" id="accordionPublications">
<div class="accordion-item">
<h2 class="accordion-header" id="flush-headingOne">
<button class="accordion-button collapsed fs-3" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
Journal publications
</button>
</h2>
<div id="flush-collapseOne" class="accordion-collapse collapse show" aria-labelledby="flush-headingOne" data-bs-parent="#accordionPublications">
<div class="accordion-body">
{% for year in site.data.pub_journal %}
<p style="font-weight: bold; padding: 30px 0 0">{{ year.Year }}</p>      
<table class="table table-striped table-hover table-borderless table-sm">
<tbody class="table-group-divider">
{% for entry in year.Items %}
<tr class="small">
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
{% endfor %}
</div>
</div>
</div>

<div class="accordion-item">
<h2 class="accordion-header" id="flush-headingTwo">
<button class="accordion-button collapsed fs-3" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
Conference communications
</button>
</h2>
<div id="flush-collapseTwo" class="accordion-collapse collapse" aria-labelledby="flush-headingTwo" data-bs-parent="#accordionPublications">
<div class="accordion-body">
{% for year in site.data.pub_conference %}
<p style="font-weight: bold; padding: 30px 0 0">{{ year.Year }}</p>
<table class="table table-striped table-hover table-borderless table-sm">
<tbody class="table-group-divider">
{% for entry in year.Items %}
<tr class="small">
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
{% endfor %}
</div>
</div>
</div>
</div>
