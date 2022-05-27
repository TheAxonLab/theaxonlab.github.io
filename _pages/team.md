---
title: "AxonLab :: About us"
layout: gridlay
excerpt: "AxonLab -- Team members"
sitemap: false
permalink: /team/
---

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
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  {% if member.title %}
  <p><i>{{ member.title }}</i></p>
  {% endif %}
  {% if member.email %}
  <p>email: <{{ member.email }}></p>
  {% endif %}

  {% if member.links %}
  <p>{% for link in member.links %}{{ link }}{% unless forloop.last %} | {% endunless %}{% endfor %}</p>
  {% endif %}

  {% if member.bio %}
  <p>{{ member.bio }}</p>
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

## Our closest collaborators

{% assign number_printed = 0 %}
{% for member in site.data.collaborators %}

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
  {% if member.email %}
  <p>email: <{{ member.email }}></p>
  {% endif %}

  {% if member.links %}
  <p>{% for link in member.links %}{{ link }}{% unless forloop.last %} | {% endunless %}{% endfor %}</p>
  {% endif %}

  {% if member.bio %}
  <p>{{ member.bio }}</p>
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

## DEI Statement
Please check our [diversity, equity, and inclusiveness statement](../dei).

## Contact

<div class="row">
<div id="rc7-map" style="width: 450px; float: left; margin-right: 10px">
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d544.7472556620913!2d6.6322377091752225!3d46.52089443349025!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x478c2e323448c0d7%3A0x264ddc873ca0e2f9!2sRue%20Centrale%207%2C%201003%20Lausanne!5e0!3m2!1sen!2sch!4v1653639078668!5m2!1sen!2sch" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>

Our offices are located in the center of Lausanne, on the 4th floor of [Rue Centrale 7](https://goo.gl/maps/CHgoqQK18h3b1AFC6).
*For post contact, please address us at*:

<div class="well" style="margin-left: 460px">
Oscar Esteban<br />
Service de radiodiagnostic et radiologie interventionnelle<br />
RC07/04/040<br />
Rue Bugnon 21<br />
CH-1011 Lausanne (Switzerland)
</div>
</div>
