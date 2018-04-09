git:
	git add *
	git commit -m "working"
	git push origin master

thesis:
	pdflatex thesis.tex
	rm thesis.log	
	rm thesis.aux

