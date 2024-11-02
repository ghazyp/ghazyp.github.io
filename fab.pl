#!/usr/bin/perl
use strict;
use warnings;

# Function to format a row with proper alignment
sub format_row {
    my ($entries, $alignments, $col_widths) = @_;
    my @formatted;

    for my $i (0 .. $#{$entries}) {
        my $entry = $entries->[$i];
        my $width = $col_widths->[$i];

        # Align the text based on alignment characters '<', '=', '>'
        if ($alignments->[$i] eq '<') {
            push @formatted, sprintf("%-*s", $width, $entry);  # Left align
        } elsif ($alignments->[$i] eq '>') {
            push @formatted, sprintf("%*s", $width, $entry);   # Right align
        } elsif ($alignments->[$i] eq '=') {
            my $padding = $width - length($entry);
            my $left_pad = int($padding / 2);
            my $right_pad = $padding - $left_pad;
            push @formatted, (' ' x $left_pad) . $entry . (' ' x $right_pad);  # Center align
        }
    }

    return "| " . join(" | ", @formatted) . " |";
}

# Function to create a divider row with correct intersections
sub divider_row {
    my ($col_widths, $intersect, $left_corner, $right_corner) = @_;
    my @divider;

    foreach my $width (@{$col_widths}) {
        push @divider, '-' x ($width + 2);  # Width + 2 to account for padding
    }

    return $left_corner . join($intersect, @divider) . $right_corner;
}

# Open input and output files
open(my $input, '<', 'fab.in') or die "Cannot open input file: $!";
open(my $output, '>', 'fab.out') or die "Cannot open output file: $!";

# Parse the input file
my @lines = <$input>;
chomp @lines;

my $first_table = 1;  # Flag to handle newlines between tables

while (@lines) {
    my $header = shift @lines;

    last if $header eq '*';  # End of file marker

    my @alignments = split(//, $header);
    my @table_data;

    # Collect the table data
    while (@lines && $lines[0] !~ /^\*$/ && $lines[0] !~ /^[<=>]/) {
        push @table_data, [split /&/, shift @lines];
    }

    my $col_count = scalar @alignments;
    my @col_widths = (0) x $col_count;

    # Determine the maximum column widths (based on header and content)
    for my $row (@table_data) {
        for my $i (0 .. $#{$row}) {
            my $entry = $row->[$i];
            $entry =~ s/^\s+|\s+$//g;  # Trim spaces
            my $entry_length = length($entry);
            $col_widths[$i] = $entry_length if $entry_length > $col_widths[$i];  # Set max column width
        }
    }

    # Adjust the column widths based on headers if needed
    for my $i (0 .. $#alignments) {
        my $header_length = length($alignments[$i]);
        $col_widths[$i] = $header_length if $header_length > $col_widths[$i];
    }

    # Avoid extra newline between tables
    if (!$first_table) {
        # Ensure there is no newline after a table but only before a new one
        print $output "\n";  # Add a newline before a new table except for the first one
    }
    $first_table = 0;  # Mark that the first table has been processed

    # Output the top border with '@' corners
    print $output divider_row(\@col_widths, '-', '@', '@') . "\n";

    # Format and output each row
    for my $i (0 .. $#table_data) {
        print $output format_row($table_data[$i], \@alignments, \@col_widths) . "\n";
        if ($i == 0) {
            # Output the title divider with '+' intersections
            print $output divider_row(\@col_widths, '+', '|', '|') . "\n";
        }
    }

    # Output the bottom border with '@' corners
    print $output divider_row(\@col_widths, '-', '@', '@');
}

# Close the files
close($input);
close($output);