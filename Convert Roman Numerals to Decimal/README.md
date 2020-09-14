This problem was recently asked by Twitter:
<br><br>
Given a Roman numeral, find the corresponding decimal value. Inputs will be between 1 and 3999.
<br><br>
<b>Example:
<br>Input:</b> IX
<br><b>Output:</b> 9
<br><br>
<b>Input:</b> VII
<br><b>Output:</b> 7
<br><br>
<b>Input:</b> MCMIV
<br><b>Output:</b> 1904
<br><br>
Roman numerals are based on the following symbols:
<br>I&ensp; &ensp;&ensp;&ensp;   1
<br>IV&ensp;   &ensp;&ensp;  4
<br>V &ensp;   &ensp;&ensp;  5
<br>IX&ensp;   &ensp;&ensp;  9 
<br>X &ensp;   &ensp;&ensp;  10
<br>XL &ensp;   &ensp; 40
<br>L  &ensp; &ensp; &ensp;50
<br>XC &ensp; &ensp;90
<br>C  &ensp; &ensp;   100
<br>CD&ensp;&ensp;400
<br>D  &ensp;  &ensp; 500
<br>CM  &ensp;   900
<br>M  &ensp;&ensp;    1000
<br><br>
Numbers are strings of these symbols in descending order. In some cases, subtractive notation is used to avoid repeated characters. The rules are as follows:
<br>1.) I placed before V or X is one less, so 4 = IV (one less than 5), and 9 is IX (one less than 10)
<br>2.) X placed before L or C indicates ten less, so 40 is XL (10 less than 50) and 90 is XC (10 less than 100).
<br>3.) C placed before D or M indicates 100 less, so 400 is CD (100 less than 500), and 900 is CM (100 less than 1000).
