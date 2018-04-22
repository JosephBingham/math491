git:
	touch Papers/thesis.aux Papers/thesis.log Papers/thesis.synctex.gz
	rm Papers/thesis.aux Papers/thesis.log Papers/thesis.synctex.gz
	git add *
	git commit -m "working"
	git push origin master

thesis:
	pdflatex /Papers/thesis.tex
	rm /Papers/thesis.log	
	rm /Papers/thesis.aux

