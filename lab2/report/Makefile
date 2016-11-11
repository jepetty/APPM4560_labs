# note: we run pdflatex three times on purpose:
# it stupidly requires multiple passes to properly prepare cross-references

default:
	pdflatex report.tex
	pdflatex report.tex
	pdflatex report.tex
clean:
	rm _TZ_* *.aux *.log *.pdf
