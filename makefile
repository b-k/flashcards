
cards:
	python ./go.py

clean:
	rm -f *.aux *.log *.pdf counts tmp.* odes.out

all:
	for i in *tex; do \
	   	if [ $$i != tikzlibrarycd.code.tex ]; then \
			pdflatex $$i; \
		fi; done;

