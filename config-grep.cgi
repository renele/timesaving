#!/usr/bin/perl -w
use strict;
use CGI qw/:standard/;

my($s, $c, $f, $e)=(param('q')//'', "body{white-space: nowrap;FONT-FAMILY: verdana; FONT-SIZE:12px;}", sub{font({-color=>'red'}, shift)}, 'enter a search string');
print header(), start_html(-title=>"syslog $s", -head=>[style({type=>'text/css'}, $c)]),
        start_form({-style=>"position:fixed; top:1px;right:1px;"}), input({-name=>'q'}), submit(-label=>"search"), end_form(),
        join(br(), map{s/($s)/$f->($1)/ieg if $s!~/^(\.)*$/; $_} $s ? split(/\n/, `grep "$s" /config/*.txt`) : ($f->($e))), end_html();
