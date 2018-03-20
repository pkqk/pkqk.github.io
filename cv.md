---
layout: hresume
style: default
title: <a id="name" href="http://pkqk.net" class="fn url">Adam Sven Johnson</a>
subtitle: I make internet things, and <a href="http://instagram.com/p/PgciyaAJlk/">I really like coffee</a>
description: The CV of Technical Lead and Full Stack Developer Adam Sven Johnson
footer: none
header: none
---

<aside>
<tt class="terminal"><pre>
$ whoami
pkqk
$ <span class="cursor">&#95;</span></pre>
</tt>
</aside>

<header>
  <h1>Adam Sven Johnson</h1>
  <p>Technical team lead & Senior developer</p>
</header>

<h2>About</h2>
<address class="contact vcard">
  <a href="{{ site.url }}" class="fn url">Adam Sven Johnson</a>
  <p><a class="email" href="m&#x61;&#x69;lto:hi&#64;pkqk.net">hi&#64;pkqk.net</a></p>
  <p><a class="tel" href="tel://&#x2B;&#x36;&#x34;&#x32;&#x32;&#x36;&#x32;&#x32;&#x39;&#x33;&#x32;">&#x2B;&#x36;&#x34;&#x20;&#x32;&#x32;&#x20;&#x36;&#x32;&#x32;&#x20;&#x39;&#x38;&#x33;&#x32;</a></p>
</address>

<section class="summary">
  <p>
    I'm a Technical team lead & Senior developer with over 10 years experience in a wide range of web development technologies.
  </p>
  <p>
    I focus mainly on the back end of the web stack, building APIs and robust services, and have done some work using modern front end web technologies.
  </p>
  <p>
    The current languages I have the most experience in are Ruby and Python and I'm also interested in newer languages like Go.
  </p>
  <p>
    Personal interests include coffee, fermentation and food of all sorts, cycling and maps.
  </p>
  <p>
    I'm a New Zealand citizen who has been working in the UK until recently.
  </p>
</section>
<h2 class="page-break">Employment history</h2>
<ul class="vcalendar">
  {% for job in site.experience reversed %}
  <li class="experience vevent vcard">
    <img class="logo" src="/img/experience/{{ job.logo }}.png" alt="">
    <p>
      <a class="fn org url" href="{{ job.link }}">{{ job.company }}</a>,
      <span class="adr"><span class="locality">{{ job.adr_locality }}</span>, <span class="country-name">{{ job.adr_country }}</span></span>
    </p>
    <p class="summary">
      <strong class="title">{{ job.title }}</strong>
    </p>
    <p>
      <span class="period">
        <abbr class="dtstart" title="{{ job.date_start }}">{{ job.date_start | date: "%B %Y" }}</abbr>
        &ndash;
        <abbr class="dtend" title="{{ job.date_end }}">{{ job.date_end | date: "%B %Y" }}</abbr>
      </span>
    </p>
    {% if job.content != blank %}
    <div class="description">
      {{ job.content }}
    </div>
    {% endif %}
  </li>
  {% endfor %}
</ul>
<h2>Education history</h2>
<ul class="vcalendar">
  {% for course in site.education %}
  <li class="education vevent vcard">
    <p>
      <strong class="summary">{{ course.course }}</strong>
      <span class="period">
        <abbr class="dtstart" title="{{ course.date_start }}"></abbr><abbr class="dtend" title="{{ course.date_end }}">{{ course.date_end | date: "%Y" }}</abbr>
      </span>      
    </p>
    <p>
      <a class="url fn org" href="{{ course.link }}">{{ course.instiution }}</a>
    </p>
  </li>
  {% endfor %}
</ul>
<h2>Skills</h2>

{% for skill in site.skills %}
<strong>{{ skill.name }} <small>({{ skill.strength }})</small></strong>
{{ skill.content }}
{% endfor %}

<p class="formats">
  <a class="pdf" title="Download as PDF" href="/pdf/adamsvenjohnson-cv.pdf"><img alt="PDF" src="/img/pdf.png"></a>
  <a rel="tag" title="Resumé marked up using microformats." href="http://microformats.org/wiki/hresume"><img alt="This page uses microformats" src="/img/microformats.png"></a>
  <a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nd/4.0/80x15.png" /></a>
</p>
