#!/usr/bin/perl
use strict;
use CGI;
use POSIX;

my $time=strftime("%F %T", localtime);
my $q=CGI->new;
print $q->header;
print "<p>hello world</p>";
print "<p>it's now: $time</p>";
