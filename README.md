# The Axonlab Website

This repository contains the source code for the Axonlab web site.

## Mission

We investigate the neuroimaging workflow to map the brain's connectivity networks and characterize the reliability, sensitivity, and specificity of these methods. Our goal is to apply such analyses to understand healthy and diseased developmental trajectories of the human brain while promoting open science and community tooling.

## Build prerequisites

1. Install Ruby and Bundler.
2. Run `bundle install` to install the dependencies.
3. Start the local server with `bundle exec jekyll serve`.

## Contribution and Credits

The web site is based on code from [the Allan Lab](https://github.com/mpa139/allanlab). Contributions are welcome through pull requests and issues.


## Development

Use Ruby 3.4 or later. Install dependencies with:

```bash
bundle install
```

## Deployment

The site is built and deployed with a [GitHub Actions](https://github.com/features/actions) workflow defined in `.github/workflows/jekyll.yml`. It installs dependencies, runs `jekyll build`, and publishes the generated site to GitHub Pages on each push to `main`.
