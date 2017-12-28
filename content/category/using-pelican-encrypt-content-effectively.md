Title: Using Pelican encrypt content effectively with GitHubPages
Category: Blogs

# About
[pelican-encrypt-content](https://github.com/mindcruzer/pelican-encrypt-content) is a plugin for [Pelican](http://docs.getpelican.com/en/stable/) that allows you to encrypt certain files. 

# Issues
Now although the file is password protected and encrypted at the client end. But if you are sharing it using github pages you will still have to upload your content source file unencrypted on a publically available website. And github repo also has password written in plain text making it pointless to use encryption.

# Simple Hack
1. Agree that your files that you don't want to share publically will be named in a certain way and ignore them. For example:
```
	(venv) Prashants-MBP:pt247.github.io prashant$ tail -1 .gitignore
	*in-progress.md
	(venv) Prashants-MBP:pt247.github.io prashant$ 
```

2. Name file in content that ends with `in-progress.md` and it will be ignored however encrypted content will be added to output.

3. Once you are happy with the second pair of eyes or want to open up to public, just remove `in-progress` text from the name and remove password/encription from your markdown or rst file. 


    Note: Keep in mind you might want to delete your output periodically because it will have old renamed files as well. More about that in another blog.
