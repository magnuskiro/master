#!/usr/bin/perl
    use strict;
    use warnings;

sub uniq {
    my %seen = ();
    my @r = ();
    foreach my $a (@_) {
        unless ($seen{$a}) {
            push @r, $a;
            $seen{$a} = 1;
        }
    }
    return @r;
}

#    my $file = 'financialTermSource.html';
    my $file = 'temp.html';

    open (FILE, $file) or die $!;
my $string = "";

while (my $line = <FILE>){ 
#  print $line;
	$string = $string . $line;
}

close(FILE);

$string =~ s/[\n\r\t]//g;
my @matches = ($string =~ /<b>(.{2,30})<\/b>/g );

my @res;
#print for @matches;
for my $term (@matches){
	$term =~ s/^[ ]+//g;
#	print $term."\n";
	push(@res, $term);
}
@res = uniq(@res);
@res = sort @res;

for my $term (@res){
	print $term."\n";
}
print scalar(@res) . "\n";

 
