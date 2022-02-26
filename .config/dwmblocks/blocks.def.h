//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/ /*Command*/	        /*Update Interval*/	/*Update Signal*/
	{"", "echo ''", 	                    0,              	0},
	{"", "pacupdates",	                    3600,              	0},
	{"", "memory",	                        10,	                0},
	{"", "temperature",                     10,	                0},
	{"", "volume",                          10,	                10},
	{"", "date '+%I:%M %P - %a %d %b'",		30,	                0},
	{"", "echo ''", 	                    0,              	0},
};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = " | ";
static unsigned int delimLen = 5;
