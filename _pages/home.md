---
title: "The Axonlab :: Welcome"
layout: default
excerpt: "Welcome to the Axonlab!"
sitemap: false
permalink: /
---

<div id="homeid" class="col-sm-8">
<h1>Welcome to the Axonlab</h1>
We investigate the neuroimaging workflow to map out the brain's connectivity networks,
characterize the reliability, sensitivity and specificity of these methodologies (from
acquisition to formalization of network information) and apply them in the understanding
of the healthy and diseased developmental trajectories of the human brain.


<div markdown="0" id="carousel" class="carousel slide" data-ride="carousel" data-interval="5000" data-pause="hover" >
    <!-- Menu -->
    <ol class="carousel-indicators">
        <li data-target="#carousel" data-slide-to="0" class="active"></li>
        <li data-target="#carousel" data-slide-to="1"></li>
        <li data-target="#carousel" data-slide-to="2"></li>
        <li data-target="#carousel" data-slide-to="3"></li>
        <li data-target="#carousel" data-slide-to="4"></li>
        <li data-target="#carousel" data-slide-to="5"></li>
        <li data-target="#carousel" data-slide-to="6"></li>
    </ol>

    <!-- Items -->
    <div class="carousel-inner" markdown="0">

        <div class="item active">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/fmriprep-smoothing.png" alt="Slide 1" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/fmriprep-flowchart.png" alt="Slide 2" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/mriqc-carpetplot.png" alt="Slide 3" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/regseg-pixel.png" alt="Slide 4" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/ambizione-design.png" alt="Slide 5" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/templateflow-mosaic.png" alt="Slide 6" />
        </div>
         <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/mriqc-reports.png" alt="Slide 7" />
        </div>
    </div>
  <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>



To this end, we develop computational methods to extract structural and functional connectivity from a variety of MRI (magnetic resonance image) techniques and corresponding physiolgical information.
In particular, we use anatomical MR schemes (e.g., T1-weighted and T2-weighted), diffusion MRI for the structural connectivity, and BOLD (blood-oxygen-level-dependent) MRI for the functional connectivity.
We engage in open science and support community tooling.
In particular, The Axonlab is deeply involved in the development of the [*NeuroImaging PREProcessing toolS (NiPreps)*](https://nipreps.org).

We are part of [the Connectomics Lab](https://wp.unil.ch/connectomics/) at [Department of Radiology of the Lausanne University Hospital (CHUV)](https://www.chuv.ch/fr/rad/rad-home).

<!--
 **We are  looking for passionate new PhD students, Postdocs, and Master students to join the team** [(more info)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**
-->

The lab receives financial support from the SNSF Ambizione project *Uncovering the interplay of structure, function, and dynamics of brain connectivity using MRI* (grant number [185872](https://p3.snf.ch/project-185872)), and from the NIMH ([RF1MH121867](https://reporter.nih.gov/project-details/10260312), PIs: Poldrack, Esteban, Rokem, Satterthwaite, and Milham).
</div>

<div id="newsid" class="float-md-end col-sm-4" >
<div class="well">
<h4>Latest News</h4>
<p>(Find out more at the <a href="{{ site.url }}{{ site.baseurl }}/allnews.html">news page</a>.)</p>
<hr style="margin-top: 22px; margin-bottom: 8px;" />

{% for article in site.data.news limit:9 %}
<p>
<em>{{ article.headline }}</em> ({{ article.date }})</p>
{% unless forloop.last %}
<hr style="margin-top: 5px; margin-bottom: 8px;" />
{% endunless %}
{% endfor %}
</div>
</div>
