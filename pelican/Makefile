PY?=/home/tammy/.pyenv/shims/python
PELICAN?=/home/tammy/.pyenv/shims/pelican
RM?=/bin/rm
CP?=/bin/cp
GIT?=/usr/bin/git
DIRNAME?=/usr/bin/dirname

PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(HOME)/projects/tammymakesthings.github.io
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

GITHUB_PAGES_BRANCH=master

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make post                           create a new post                  '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

post:
	$(PY) $(BASEDIR)/helpers/new_post.py

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	$(RM) $(OUTPUTDIR)/*.html
	$(RM) $(OUTPUTDIR)/*.xml
	$(RM) $(OUTPUTDIR)/CNAME $(OUTPUTDIR)/robots.txt
	$(RM) -r $(OUTPUTDIR)/20* \
			 $(OUTPUTDIR)/author \
			 $(OUTPUTDIR)/category \
			 $(OUTPUTDIR)/contact \
			 $(OUTPUTDIR)/feeds \
			 $(OUTPUTDIR)/images  \
			 $(OUTPUTDIR)/projects \
			 $(OUTPUTDIR)/tag \
			 $(OUTPUTDIR)/theme

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

serve-global:
ifdef SERVER
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b $(SERVER)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b 0.0.0.0
endif

devserver:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

stylesheet: $(BASEDIR)/themes/tcflex/static/stylesheet/style.less
	lessc $(BASEDIR)/themes/tcflex/static/stylesheet/style.less > $(BASEDIR)/themes/tcflex/static/stylesheet/style.css
	yui-compressor $(BASEDIR)/themes/tcflex/static/stylesheet/style.css > $(BASEDIR)/themes/tcflex/static/stylesheet/style.min.css

publish: stylesheet
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	$(CP) $(INPUTDIR)/extra/* $(OUTPUTDIR)

github: publish
	git add $(OUTPUTDIR)
	git commit -m "Snapshot for publish to github at `date`"
	git push origin $(GITHUB_PAGES_BRANCH)


.PHONY: post html help clean regenerate serve serve-global devserver publish github
