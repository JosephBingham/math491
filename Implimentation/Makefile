make: Stegogram.cpp
	g++ Stegogram.cpp -o Stegogram -O3 -Wall -lm -g -I/usr/local/opt/opencv@2/include
	rm -rf Stegogram.d*

test: test.cpp
	g++ test.cpp -o test  -Wall -lm -g -I/usr/local/opt/opencv@2/include
	rm -rf test.d*

clean:
	touch test Stegogram
	rm test Stegogram
