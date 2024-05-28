#include <iostream>
#include <unordered_map>
#include <cctype> // For std::isalpha

int main() {
    std::string input = "MAHHHHHHMGTLEAQTQGPGSMTDFYSLIPSAPKGRFDGIERAHTAEDVKRLRGSVEIKYSLAEMGANRLWKLIHEEDFVNALGALSGNQAMQMVRAGLKAIYLSGWQVAADANTASAMYPDQSLYPANAGPELAKRINRTLQRADQIETAEGKGLSVDTWFAPIVADAEAGFGGPLDAFEIMKAYIEAGAAGVHFEDQLASEKKCGHLGGKVLIPTAAHIRNLNAARLAADVMGTPTLIVARTDAEAAKLLTSDIDERDQPFVDYEAGRTAEGFYQVKNGIEPCIARAIAYAPYCDLIWMETSKPDLAQARRFAEAVHKAHPGKLLAYNCSPSFNWKKNLDDATIAKFQRELGAMGYKFQFITLAGFHQLNYGMFELARGYKDRQMAAYSELQQAEFAAEADGYTATKHQREVGTGYFDAVSLAITGGQSSTTAMKESTETAQFKPAAE";

    // Convert input to lowercase for case-insensitive counting
    for (char &c : input) {
        c = std::tolower(c);
    }

    // Create a map to store counts of each letter
    std::unordered_map<char, int> letter_counts;

    // Iterate over the input string and count occurrences of each letter
    for (char c : input) {
        // Check if the character is an alphabet letter
        if (std::isalpha(c)) {
            letter_counts[c]++;
        }
    }

    // Print the letter counts
    int count=0;
    for (const auto &pair : letter_counts) {
        count+=pair.second;
        std::cout << "Letter " << pair.first << " occurs " << pair.second << " times." << std::endl;
    }
    std::cout<<count<<std::endl;

    return 0;
}