# This make file compiles the C/C++ executables used by examples/Example5.java
# and examples/Example6.java.
#
# This make file assumes it is being run on a Unix-like environment with GCC
# and Make installed.  Windows users can install MinGW/MSYS or Cygwin.
#
# Run 'make' to build all files

CXX = mpiCC
CXXFLAGS = -c -Wall -g
INC = -I /opt/boost/1.54.0/include
LIBS = -lm
UNAME_S = $(shell uname -s)

ifneq (, $(findstring SunOS, $(UNAME_S)))
    LIBS += -lnsl -lsocket -lresolv
endif

all: lake

lake: lake.o moeaframework.o 
	$(CXX) lake.o moeaframework.o -o lake

moeaframework.o: ./moeaframework.c ./moeaframework.h
	$(CXX) $(CXXFLAGS) ./moeaframework.c

lake.o: lake.cpp ./moeaframework.h ./boostutil.h 
	$(CXX) $(CXXFLAGS) $(INC) lake.cpp -o lake.o
 

