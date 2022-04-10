## Add your own custom Makefile targets here

gh-deploy:
# deploy documentation on gh-pages branch (note: requires documentation is in docs dir)
	$(RUN) mkdocs gh-deploy 