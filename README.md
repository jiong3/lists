# Lists

License: [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/).

## avTextbook
Under the assumption that textbooks introduce important words early and less important words later on this list was created. It represents the average order of words in textbooks, based on most textbooks available at [skritter](http://www.skritter.com) at this time (around 30).
Each word got points:
- For each textbook: (number of words in book - position of word) / number of words
- For old HSK: 5 - hsk level of word
- For new HSK: 9 - hsk level of word

The result is in avTextbookSimpWords.tsv. From this the avTextbookSimpChars.tsv was created.

#### Todo
Create traditional version from sourcefiles, skritter api?

## Keywords

### pinyinHanzi
For each sound in pinyin there is an example traditional character given along with the tone this character uses. Those keywords are also found in the pinyinChart.

#### Todo
Try to find characters which are not used in regular decompositions in order to reduce possibility for confusion when both are used in mnemonics.

### tradHanziToDe
For around 3500 traditional characters a German keyword is given (like in the Heisig books). This was done completely independent of any books using only the HanDeDic dictionary.
Each item consists of:
1. Primary keyword (mandatory)
2. Primary tag (optional)
3. Secondary keyword (if necessary)
4. Secondary tag (necessary if sec. keyword)

The primary keyword should convey the main/most useful/most common meaning of the character. If two or more character share the same primary keyword a secondary keyword is introduced for each of them. The combination of both keywords must be unique. The secondary keyword must carry a tag, for the primary keyword this is optional and not used very often.

The following tags are used:
 
The keyword
- w word: conveys the meaning of a word which contains the character
- f fantasy: is more or less made up
- p position: indicates the position of this character in a (key)word, Ab or aB
- g glyph: describes the glyph, e.g. simp or trad variants
- a alternative: conveys a different meaning of the character
- d definition: provides more detail for the primary keyword
- n name: gives a name which contains the character

#### Qualität (German)
Aufgrund der großen Anzahl an Schriftzeichen konnte auf jedes Zeichen nur wenig Zeit verwendet werden. Diese Liste enthält somit noch Fehler, die hoffentlich während des Gebrauchs auffallen und korrigiert werden können. Verbesserungen auch gerne per E-Mail.

#### Todo
If the character has more than one definition with different pronunciations, add the pronunciation which refers to the meaning of the keyword
