---
title: "The Axonlab :: Welcome"
layout: default
excerpt: "Welcome to the Axonlab!"
sitemap: false
permalink: /
---

# Welcome to the Axonlab

<div id="newsid" class="float-md-end col-sm-4" style="display:block" >
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

We investigate the neuroimaging workflow to map out the brain's connectivity networks,
characterize the reliability, sensitivity and specificity of these methodologies (from
acquisition to formalization of network information) and apply them in the understanding
of the healthy and diseased developmental trajectories of the human brain.

<!-- Carousel -->
<div id="home-carousel" class="carousel slide" data-bs-ride="true">
<div class="carousel-indicators">
<button type="button" data-bs-target="#home-carousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
<button type="button" data-bs-target="#home-carousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
<button type="button" data-bs-target="#home-carousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
</div>
<div class="carousel-inner">
<div class="carousel-item active">
<img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/fmriprep-smoothing.png" class="d-block w-100" alt="fMRIPrep & tools" />
</div>
<div class="carousel-item">
<img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/fmriprep-flowchart.png" class="d-block w-100" alt="fMRIPrep workflow">
</div>
<div class="carousel-item">
<img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/mriqc-carpetplot.png" class="d-block w-100" alt="QA/QC of MRI data & MRIQC">
</div>
<div class="carousel-item">
<img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/regseg-pixel.png" class="d-block w-100" alt="Neuroimaging methods development">
</div>
<div class="carousel-item">
<img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/ambizione-design.png" class="d-block w-100" alt="Reliabilty of MRI measurements">
</div>
<div class="carousel-item">
<img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/templateflow-mosaic.png" class="d-block w-100" alt="TemplateFlow -- neuroimaging templates and atlases">
</div>
<div class="carousel-item">
<img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/mriqc-reports.png" class="d-block w-100" alt="MRIQC -- Visual reports">
</div>
</div>
<button class="carousel-control-prev" type="button" data-bs-target="#home-carousel" data-bs-slide="prev">
<span class="carousel-control-prev-icon" aria-hidden="true"></span>
<span class="visually-hidden">Previous</span>
</button>
<button class="carousel-control-next" type="button" data-bs-target="#home-carousel" data-bs-slide="next">
<span class="carousel-control-next-icon" aria-hidden="true"></span>
<span class="visually-hidden">Next</span>
</button>
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
