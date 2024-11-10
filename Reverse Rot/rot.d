import std.stdio;
import std.string : indexOf, strip;
import std.conv : to;
import std.algorithm : map;
import std.range : retro;
import std.array : array;

void main() {
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.";
    string line;
    string[] results;

    // Read the input until a line with '0' is encountered
    while ((line = readln().strip()) !is null && line != "0") {
        auto white_space = line.indexOf(" ");
        if (white_space == -1) {
            continue; // Skip lines without a space
        }

        int n = to!int(line[0 .. white_space]); // Convert the rotation number to an integer
        string plain_text = line[white_space + 1 .. $]; // Extract the string to be encoded
        string reversed = plain_text.retro.array.to!string; // Reverse the string

        string result = "";
        foreach (char c; reversed) {
            size_t newIndex = (alphabet.indexOf(c) + n) % alphabet.length;
            result ~= alphabet[newIndex]; // Append the rotated character to the result string
        }
        results ~= result; // Store the result in the results array
    }

    // Output all results, each on a new line
    foreach (res; results) {
        writeln(res);
    }
}