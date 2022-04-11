## Add your own custom Makefile targets here

gh-deploy:
# deploy documentation on gh-pages branch 
# this target is run by the build-deploy-documentation workflow
# it differs from the deploy target by not running gen-project (i.e., it only builds docs)
# note: requires documentation is in docs dir
	$(RUN) mkdocs gh-deploy 

gh-deploy-remote:
# deploy documentation on gh-pages  on remote gh-pages branch
# this target is run locally and the docs are pushed the remote gh-pages branch
# note: requires documentation is in docs dir
	$(RUN) mkdocs gh-deploy --remote-branch gh-pages --force --theme readthedocs

gh-deploy-remote:
# deploy documentation on gh-pages  on remote gh-pages branch USING readthedocs theme
# this target is run locally and the docs are pushed the remote gh-pages branch
# note: requires documentation is in docs dir
	$(RUN) mkdocs gh-deploy --remote-branch gh-pages --force --theme readthedocs