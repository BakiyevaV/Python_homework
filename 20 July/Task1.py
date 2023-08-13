def get_diag_words(input):
    if len(input) > 0:    
        word1 = ""
        word2 = ""
        sentence = []
        for i in range(len(input)):
            word1 += input[i][i]
        sentence.append(word1)

        for i in range(len(input)):
            if i == 0:
                word2 += input[i][-1]
            else:
                word2 += input[i][(len(input[i])-1) - i]
        sentence.append(word2)
        result = " ".join(sentence)
        return result
    else:
        return ""

def test_get_diag_words():
    input = [['ж','ф','л'],
             ['р','и','а'],
             ['с','з','л']]
    expect = "жил лис"
    assert get_diag_words(input) == expect

    input = [['б','ф','л','т',']','в'],
             ['р','е','а','о','о','щ'],
             ['е','и','л','р','э','к'],
             ['г','ы','о','а','ф','о'],
             ['н','н','а','а','я','ч'],
             ['а','з','л','ц','в',' ']]
    expect = "белая  ворона"
    assert get_diag_words(input) == expect

    input = []
    expect = ""
    assert get_diag_words(input) == expect

test_get_diag_words()