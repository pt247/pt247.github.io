#!/bin/bash
cd /Users/prashant/work/pt247.github.io
pelican content -o output -s pelicanconf.py && ghp-import output && git push origin gh-pages
git push git@github.com:pt247/pt247.github.io.git gh-pages:master
