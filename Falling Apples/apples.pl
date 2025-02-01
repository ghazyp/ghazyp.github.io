use strict;
use warnings;

sub read_input {
    my ($file) = @_;
    open my $fh, '<', $file or die "Cannot open file: $!";
    my ($rows, $cols) = split ' ', <$fh>;
    my @grid;
    for (1..$rows) {
        chomp(my $line = <$fh>);
        push @grid, [split //, $line];
    }
    close $fh;
    return (\@grid, $rows, $cols);
}

sub simulate_falling_apples {
    my ($grid, $rows, $cols) = @_;
    for my $col (0..$cols-1) {
        my $empty_row = $rows - 1;
        for my $row (reverse 0..$rows-1) {
            if ($grid->[$row][$col] eq 'a') {
                if ($row != $empty_row) {
                    $grid->[$empty_row][$col] = 'a';
                    $grid->[$row][$col] = '.';
                }
                $empty_row--;
            } elsif ($grid->[$row][$col] eq '#') {
                $empty_row = $row - 1;
            }
        }
    }
    return $grid;
}

sub print_grid {
    my ($grid) = @_;
    for my $row (@$grid) {
        print join('', @$row), "\n";
    }
}

my $file = 'apples.in';
my ($grid, $rows, $cols) = read_input($file);
$grid = simulate_falling_apples($grid, $rows, $cols);
print_grid($grid);