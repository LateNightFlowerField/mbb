over=0.5
opts='pattern=crosshatch, pattern color=white, line width=.3mm'
python bridge.py -t bailey -s 7 -o $over -O "$opts" > figures/bailey7.tex
python bridge.py -t bailey -s 6 -o $over -O "$opts" > figures/bailey6.tex
python bridge.py -t bailey -s 5 -o $over -O "$opts" > figures/bailey5.tex
python bridge.py -t bailey -s 4 -o $over -O "$opts" > figures/bailey4.tex
python bridge.py -t warren -s 7 -o $over -O "$opts" > figures/warren7.tex
python bridge.py -t warren -s 6 -o $over -O "$opts" > figures/warren6.tex
python bridge.py -t warren -s 5 -o $over -O "$opts" > figures/warren5.tex
python bridge.py -t warren -s 4 -o $over -O "$opts" > figures/warren4.tex
python bridge.py -t howe -s 6 -o $over -O "$opts" > figures/howe6.tex
python bridge.py -t howe -s 4 -o $over -O "$opts" > figures/howe4.tex
python bridge.py -t pratt -s 6 -o $over -O "$opts" > figures/pratt6.tex
python bridge.py -t pratt -s 4 -o $over -O "$opts" > figures/pratt4.tex
python bridge.py -t k -s 6 -o $over -O "$opts" > figures/k6.tex
python bridge.py -t k -s 4 -o $over -O "$opts" > figures/k4.tex
