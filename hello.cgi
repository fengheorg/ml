#!/usr/bin/perl
use strict;
use CGI;

my $q=CGI->new;
print $q->header;
print "<p>hello world</p>";
