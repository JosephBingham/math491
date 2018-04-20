git:
	git add *
	git commit -m "working"
	git push origin master

thesis:
	pdflatex /Papers/thesis.tex
	rm /Papers/thesis.log	
	rm /Papers/thesis.aux

