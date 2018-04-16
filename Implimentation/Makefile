make: Stegogram.cpp
	g++ Stegogram.cpp -o Stegogram -O2 -Wall -lm -g
	rm -rf Stegogram.d*

test: test.cpp
	g++ test.cpp -o test -O2 -Wall -lm -g
	rm -rf test.d*

clean:
	touch test Stegogram
	rm test Stegogram
