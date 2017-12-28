#!/bin/bash
rm -rf *.html author category pages pdfs theme output/*
fab build 
fab serve
cp -r output/* . 
git add . 
git commit 
git push 
fab gh_pages
