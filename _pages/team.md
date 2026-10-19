---
title: "AxonLab :: About us"
layout: default
excerpt: "AxonLab -- Team members"
sitemap: false
permalink: /team/
---

<div class="px-2 gx-2">
<!--
**We are  looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**
Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors).
-->


# About us

## Our team

{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

<!-- Card -->
<div class="card mb-3 border-0">
<div class="row g-0">
<div class="col-md-4">
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-fluid rounded-start" alt="{{ member.name }}">
</div>
<div class="col-md-8">
<div class="card-body">
<h5 class="card-title">{{ member.name }}</h5>
{% if member.title %}
<h6 class="card-subtitle mb-2 text-muted">{{ member.title }}</h6>
{% endif %}
{% if member.email %}
<p class="card-text">email: <{{ member.email }}></p>
{% endif %}
{% if member.links %}
<p class="card-text"><small>{% for link in member.links %}{{ link }}{% unless forloop.last %} | {% endunless %}{% endfor %}</small></p>
{% endif %}
</div>
</div>
</div>
</div>

{% if member.bio %}
<p><small>{{ member.bio }}</small></p>
{% endif %}
{% if member.education %}
<ul style="overflow: hidden">
{% for edu_item in member.education %}
<li> {{ edu_item }} </li>
{% endfor %}
</ul>
{% endif %}
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Our alumni

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

<!-- Card -->
<div class="mb-3">
<h5 class="card-title">{{ member.name }}</h5>
{% if member.title %}
<p class="text-muted mb-1">{{ member.title }}</p>
{% endif %}
{% if member.links %}
<p class="card-text"><small>{% for link in member.links %}{{ link }}{% unless forloop.last %} | {% endunless %}{% endfor %}</small></p>
{% endif %}
</div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


## Our closest collaborators

{% assign number_printed = 0 %}
{% for member in site.data.collaborators %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

<!-- Card -->
<div class="mb-3">
<h5 class="card-title">{{ member.name }}</h5>
{% if member.title %}
<p class="text-muted mb-1">{{ member.title }}</p>
{% endif %}
{% if member.links %}
<p class="card-text"><small>{% for link in member.links %}{{ link }}{% unless forloop.last %} | {% endunless %}{% endfor %}</small></p>
{% endif %}
</div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## DEI Statement
Please check our [diversity, equity, and inclusiveness statement](../dei).

## Contact

The Axonlab is at the School of Engineering (HEI) of [HES-SO Valais-Wallis](https://www.hevs.ch), in Sion (Switzerland). <br />
Write to us at [{{ site.email }}](mailto:{{ site.email }}).

</div>