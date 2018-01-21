tex:
	pdflatex thesis.tex
	rm *.log *.aux
	ghostscript thesis.pdf
git:
	git add *
	git commit
	git push origin master
