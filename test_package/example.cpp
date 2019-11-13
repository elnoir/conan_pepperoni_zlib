#include <iostream>
#include <minizip/zip.h>

int main() {
	auto zf = zipOpen("asdqwe.zip", APPEND_STATUS_CREATE);
	zipClose(zf, "closing test file");
}
