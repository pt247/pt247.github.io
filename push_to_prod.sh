#!/bin/bash
fab build 
fab serve
cp -r output/* . 
git add . 
git commit 
git push 
fab gh_pages
