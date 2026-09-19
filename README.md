# Career-Compass
Career guidance tool built in 3 stages, shaped by real user testing (10 survey responses, 6 testers)

A career-guidance tool to help students explore different careers, compare them side by side,
and track skills needed for a chosen path. Built in three stages as I learned more.

## Why I built it
I wanted to make something that could have helped me when I was choosing A Levels and thinking
about apprenticeships vs university — a lot of career advice online is generic, so I wanted
something that let you directly compare options and see what skills you actually need.

## Versions

**v1 — first CLI prototype**
A menu-driven command line program with a fixed list of careers, each with a skills "roadmap"
and links to learning resources. My first attempt at structuring data with nested dictionaries.

**v2 — CLI with user research**
I tested v1 with 6 people and ran a 10-response questionnaire on what people actually wanted
from a tool like this. Based on that feedback I rebuilt it: added a proper compare-two-careers
feature (the most requested feature), favourites, and a notes section (which testers said they
missed when it wasn't there). Careers are now compared field-by-field instead of just listed.

**v3 — first GUI attempt**
Started rebuilding the CLI as a Tkinter desktop app to make it easier to use — buttons for the
main careers, a search bar, and a results panel. Still early: the buttons show a placeholder
result rather than the full comparison data yet.

## How to run
