<!--
MIT License

Copyright (c) 2024 The Axon Lab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-->
# AGENTS instructions

This repository's purpose is to maintain the static website of the Axon Lab.
The website is published through GitHub's `gh-pages`, deployed with its default Jekyll platform.

## Building
To build the project, ensure a ruby setup with Jekyll installed and run:

```
bundle exec jekyll build --baseurl "/"
```

## Codex instructions

- Always plan first
- Think harder in the planning phase
- When proposing tasks, highlight potential critical points that could lead to side effects.

## Commits, branches, and PRs

- Commit messages should follow the semantic commit conventions, and at least, contain one line with the following format: `<type-code>: <message>` where `<type-code>` indicates the type of comment. Type of comments can be fixes and bugfixes (`fix:`), enhancements and new features (`enh:`), style (`sty:`), documentation (`doc:`), maintenance (`mnt:`), etc.
- Feature branches' names should also start with the semantic commit type, followed by a slash and a name: `enh/new-feature-added`, or `fix/378` (where 378 is an issue reporting a bug), or `fix/378-typo-in-publications` (e.g., an issue with some keywords).
- PR titles should also be semantic, and use the same Type codes but in all caps (e.g., `FIX:`, `ENH:`, `STY:`, `DOC:`, `STY:`, `MNT:`)
