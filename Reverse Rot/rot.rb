def reverse_rot()
    file = File.open('rot.in', 'r')
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    
    while (line = file.gets)
        white_space = line.index(' ')
        next if white_space.nil?
        n = line[0...white_space].to_i # Get the integer
        text_substring = line[(white_space + 1)..-1].strip
        reversed_substring = text_substring.reverse  # Reverse the substring
        # Rotate each character in the reversed substring
        rotated_text = reversed_substring.chars.map do |char|
            new_index = (alphabet.index(char) + n) % alphabet.length
            alphabet[new_index]
        end.join
        
        puts rotated_text  # Print the rotated text
    end
    file.close
end

reverse_rot()
