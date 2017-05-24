#!/usr/bin/perl
use strict;
use CGI;
use POSIX;

my $q=CGI->new;
my $time=strftime("%F %T", localtime);
my $ip = $q->remote_addr;

print $q->header;
print "<p>welcome from: $ip</p>";
print "<p>time now: $time</p>";
