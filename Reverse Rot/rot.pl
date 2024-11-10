#!/usr/bin/perl
use strict;
use warnings;

sub reverse_rot {
    my $filename = 'rot.in';
    open(my $fh, '<', $filename) or die "Could not open file '$filename' $!";

    my $alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.";
    my $result = "";

    while (my $line = <$fh>) {
        chomp($line);  # Remove trailing newline
        my $white_space = index($line, ' ');  # Find the first space

        if ($white_space == -1) {
            next;  # Skip lines without a space
        }

        my $n = substr($line, 0, $white_space);  # Get the integer
        my $plain_text = substr($line, $white_space + 1);  # Get the text part
        my $reversed_s = reverse($plain_text);  # Reverse the string

        last if $n == 0;  # Exit the loop if n is 0

        foreach my $c (split //, $reversed_s) {
            my $x = index($alphabet, $c);
            $result .= substr($alphabet, ($x + $n) % length($alphabet), 1);
        }
        $result .= "\n";
    }

    close($fh);
    print $result;
}

reverse_rot();
