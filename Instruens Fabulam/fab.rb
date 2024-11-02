# Function to parse input and return a list of tables
def parse_input(input_lines)
    tables = []
    current_table = []
  
    input_lines.each do |line|
      line.strip!
      if line == '*'
        tables << current_table unless current_table.empty?
        break
      elsif line.chars.all? { |ch| ['<', '=', '>'].include?(ch) }
        tables << current_table unless current_table.empty?
        current_table = [line.chars]
      else
        current_table << line.split('&').map(&:strip)
      end
    end
  
    tables
  end
  
  # Function to calculate the maximum width for each column
  def calculate_widths(table)
    table.transpose.map do |column|
      column.map(&:length).max
    end
  end
  
  # Function to format the table according to the specification
  def format_table(table)
    alignments = table[0]  # The first row contains the alignment markers
    widths = calculate_widths(table[1..])  # Calculate the widths excluding the alignment row
  
    # Define alignment mappings for left, center, and right
    align_map = { '<' => :ljust, '=' => :center, '>' => :rjust }
  
    # Format the header row
    header = '| ' + table[1].zip(alignments, widths).map do |text, align, width|
      text.strip.send(align_map[align], width)
    end.join(' | ') + ' |'
  
    # Create the top and bottom borders with appropriate lengths
    divider = '|' + widths.map { |width| '-' * (width + 2) }.join('+') + '|'
    top_border = '@' + '-' * (divider.length - 2) + '@'
  
    # Format each row of the table (after the header)
    rows = table[2..].map do |row|
      '| ' + row.zip(alignments, widths).map do |text, align, width|
        text.strip.send(align_map[align], width)
      end.join(' | ') + ' |'
    end
  
    # Return the formatted table as a string
    [top_border, header, divider, *rows, top_border].join("\n")
  end
  
  # Main function to read input, format tables, and output results
  def main
    # Read input file
    input_lines = File.readlines('fab.in').map(&:chomp)
  
    # Parse input
    tables = parse_input(input_lines)
  
    # Open output file for writing
    File.open('fab.out', 'w') do |output_file|
      tables.each_with_index do |table, i|
        formatted_table = format_table(table)
  
        # Print the formatted table without an automatic newline
        print formatted_table
        output_file.write(formatted_table)
  
        # Manually add a newline only between tables, but not after the last one
        if i < tables.size - 1
          print "\n"  # Newline for the console
          output_file.write("\n")  # Newline for the file
        end
      end
    end
  end
    
  # Call the main function
  main if __FILE__ == $PROGRAM_NAME
