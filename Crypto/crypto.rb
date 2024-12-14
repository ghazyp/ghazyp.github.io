require 'base64'

# Problem 1: Convert hex to base64 and back
def hex_to_base64(hex_str)
  # Convert hex string to bytes, then encode to Base64
  bytes_data = [hex_str].pack('H*') # 'H*' packs the hex string to binary data
  Base64.strict_encode64(bytes_data)
rescue StandardError => e
  puts "Error converting hex to Base64: #{e.message}"
end

def base64_to_hex(base64_str)
  # Decode Base64 to bytes, then convert to hex
  bytes_data = Base64.decode64(base64_str)
  bytes_data.unpack1('H*') # 'H*' unpacks binary data to hex string
rescue StandardError => e
  puts "Error converting Base64 to hex: #{e.message}"
end

# Problem 2: Fixed XOR
def fixed_xor(hex_str1, hex_str2)
  # XOR two hexadecimal strings of the same length
  bytes1 = [hex_str1].pack('H*')
  bytes2 = [hex_str2].pack('H*')

  raise 'Inputs must have equal length' unless bytes1.length == bytes2.length

  xor_result = bytes1.bytes.zip(bytes2.bytes).map { |a, b| a ^ b }.pack('C*')
  xor_result.unpack1('H*')
rescue StandardError => e
  puts "Error performing XOR: #{e.message}"
end

# Problem 3: Single-character XOR Cipher
def single_char_xor_cipher(hex_str)
  bytes_data = [hex_str].pack('H*')
  best_score = nil
  best_result = nil
  best_key = nil

  (0..255).each do |key|
    decoded = bytes_data.bytes.map { |b| b ^ key }.pack('C*')
    score = score_text(decoded)
    if best_score.nil? || score > best_score
      best_score = score
      best_result = decoded
      best_key = key
    end
  end

  { key: best_key, message: best_result }
rescue StandardError => e
  puts "Error in single-character XOR cipher: #{e.message}"
end

def score_text(text)
  # Scoring based on English letter frequency
  frequency = {
    'a' => 0.0651738, 'b' => 0.0124248, 'c' => 0.0217339, 'd' => 0.0349835, 'e' => 0.1041442, 'f' => 0.0197881,
    'g' => 0.0158610, 'h' => 0.0492888, 'i' => 0.0558094, 'j' => 0.0009033, 'k' => 0.0050529, 'l' => 0.0331490,
    'm' => 0.0202124, 'n' => 0.0564513, 'o' => 0.0596302, 'p' => 0.0137645, 'q' => 0.0008606, 'r' => 0.0497563,
    's' => 0.0515760, 't' => 0.0729357, 'u' => 0.0225134, 'v' => 0.0082903, 'w' => 0.0171272, 'x' => 0.0013692,
    'y' => 0.0145984, 'z' => 0.0007836, ' ' => 0.1918182
  }
  text.downcase.chars.sum { |char| frequency.fetch(char, 0) }
end

# Main execution
if __FILE__ == $PROGRAM_NAME
  begin
    # Problem 1: Hex to Base64
    hex_str = File.read('hex_input.txt').strip
    base64_str = hex_to_base64(hex_str)
    File.write('base64_output.txt', base64_str)
    File.write('hex_output.txt', base64_to_hex(base64_str))
    puts 'Problem 1 completed.'

    # Problem 2: Fixed XOR
    hex_str1 = File.read('xor_input1.txt').strip
    hex_str2 = File.read('xor_input2.txt').strip
    xor_result = fixed_xor(hex_str1, hex_str2)
    File.write('xor_output.txt', xor_result)
    puts 'Problem 2 completed.'

    # Problem 3: Single-character XOR Cipher
    hex_str = File.read('single_char_xor_input.txt').strip
    result = single_char_xor_cipher(hex_str)
    File.write('single_char_xor_output.txt', "Key: #{result[:key]}\nMessage: #{result[:message]}")
    puts 'Problem 3 completed.'
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end
end