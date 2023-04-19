#! /bin/sh
# $Id: MKkey_defs.sh,v 1.22 2022/02/05 20:38:31 tom Exp $
##############################################################################
# Copyright 2019-2020,2022 Thomas E. Dickey                                  #
# Copyright 2001-2013,2017 Free Software Foundation, Inc.                    #
#                                                                            #
# Permission is hereby granted, free of charge, to any person obtaining a    #
# copy of this software and associated documentation files (the "Software"), #
# to deal in the Software without restriction, including without limitation  #
# the rights to use, copy, modify, merge, publish, distribute, distribute    #
# with modifications, sublicense, and/or sell copies of the Software, and to #
# permit persons to whom the Software is furnished to do so, subject to the  #
# following conditions:                                                      #
#                                                                            #
# The above copyright notice and this permission notice shall be included in #
# all copies or substantial portions of the Software.                        #
#                                                                            #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,   #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL    #
# THE ABOVE COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING    #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER        #
# DEALINGS IN THE SOFTWARE.                                                  #
#                                                                            #
# Except as contained in this notice, the name(s) of the above copyright     #
# holders shall not be used in advertising or otherwise to promote the sale, #
# use or other dealings in this Software without prior written               #
# authorization.                                                             #
##############################################################################
#
# MKkey_defs.sh -- generate function-key definitions for curses.h
#
# Author: Thomas E. Dickey 2001
#
# Extract function-key definitions from the Caps file
#
: ${AWK-awk}

test $# = 0 && set Caps

data=data$$
pass1=pass1_$$
pass2=pass2_$$
pass3=pass3_$$
pass4=pass4_$$
trap 'rm -f $data pass[1234]_$$; exit 1' 1 2 3 15
trap 'rm -f $data pass[1234]_$$' 0

# change repeated tabs (used for readability) to single tabs (needed to make
# awk see the right field alignment of the corresponding columns):
if sort -k 6 "$@" >$data 2>/dev/null
then
	# POSIX
	sed -e 's/[	][	]*/	/g' "$@" |sort -n -k 6 >$data
elif sort -n +5 "$@" >$data 2>/dev/null
then
	# SunOS (and SVr4, marked as obsolete but still recognized)
	sed -e 's/[	][	]*/	/g' "$@" |sort -n +5 >$data
else
	echo "Your sort utility is broken.  Please install one that works." >&2
	exit 1
fi

# add keys that we generate automatically:
cat >>$data <<EOF
key_resize	kr1	str	R1	KEY_RESIZE	+	NCURSES_EXT_FUNCS 	Terminal resize event
EOF

THIS=./`basename $0`

cat <<EOF
/*
 * These definitions were generated by $THIS $*
 */
EOF

# KEY_RESET
maxkey=345

for pass in 1 2 3 4
do

output=pass${pass}_$$

${AWK-awk} >$output <$data '
function print_cols(text,cols) {
	printf "%s", text
	len = length(text);
	while (len < cols) {
		printf "	"
		len += 8;
	}
}
function decode(keycode) {
	result = 0;
	if (substr(keycode, 1, 2) == "0x") {
		digits="0123456789abcdef";
	} else if (substr(keycode, 1, 1) == "0") {
		digits="01234567";
	} else {
		digits="0123456789";
	}
	while (length(keycode) != 0) {
		digit=substr(keycode, 1, 1);
		keycode=substr(keycode, 2);
		result = result * length(digits) + index(digits, digit) - 1;
	}
	return result;
}

BEGIN	{
	maxkey='$maxkey';
	pass='$pass';
	key_max=1;
	bits=1;
	while (key_max < maxkey) {
		bits = bits + 1;
		key_max = (key_max * 2) + 1;
	}
	octal_fmt = sprintf ("%%0%do", (bits + 2) / 3 + 1);
}

/^$/		{next;}
/^#/		{next;}
/^capalias/	{next;}
/^infoalias/	{next;}
/^used_by/	{next;}
/^userdef/	{next;}

$5 != "-" && $6 != "-" {
		if ($6 == "+") {
			if (pass == 1 || pass == 2)
				next;
			thiskey=maxkey + 1;
		} else {
			if (pass == 3)
				next;
			thiskey=decode($6);
		}
		if (thiskey > maxkey)
			maxkey = thiskey;
		if (pass == 2 || pass == 3) {
			showkey=sprintf(octal_fmt, thiskey);
			ifdef = 0;
			if (index($7,"NCURSES_") == 1) {
				ifdef = 1;
				printf "\n";
				printf "#ifdef %s\n", $7;
			}
			if ($5 == "KEY_F(0)" ) {
				printf "#define "
				print_cols("KEY_F0", 16);
				print_cols(showkey, 16);
				print "/* Function keys.  Space for 64 */";
				printf "#define "
				print_cols("KEY_F(n)", 16);
				print_cols("(KEY_F0+(n))", 16);
				print "/* Value of function key n */"
			} else {
				printf "#define "
				print_cols($5, 16);
				print_cols(showkey, 16);
				printf "/*"
				for (i = 8; i <= NF; i++)
					printf " %s", $i
				print " */"
			}
			if (ifdef != 0) {
				printf "#endif\n";
			}
		}
	}
END	{
		if (pass == 1) {
			print maxkey;
		} else if (pass == 4) {
			print "";
			printf "#define ";
			print_cols("KEY_MAX", 16);
			result = sprintf (octal_fmt, key_max);
			print_cols(result, 16);
			printf "/* Maximum key value is ";
			printf octal_fmt, maxkey;
			print " */";
		}
	}
'
if test $pass = 1 ; then
	maxkey=`cat $pass1`
fi

done

cat $pass2
cat $pass3
cat $pass4
