---
title: "AxonLab :: About us"
layout: gridlay
excerpt: "AxonLab: Team members"
sitemap: false
permalink: /team/
---

<!--
**We are  looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**
Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors).
-->

# Our team

{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  {% if member.title %}
  <p><i>{{ member.title }}</i></p>
  {% endif %}
  <p>email: <{{ member.email }}></p>

  {% if member.education %}
  <ul style="overflow: hidden">
  {% for edu_item in member.education %}
  <li> {{ edu_item }} </li>
  {% endfor %}
  </ul>
  {% endif %}

  {% if member.bio %}
  <p>{{ member.bio }}</p>
  {% endif %}

  {% if member.links %}
  <p>
      {% for link in member.links %}
      {{ link }}{% unless forloop.last %} | {% endunless %}
      {% endfor %}
  </p>
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
