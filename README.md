
**To re-order the transactions of a bank statement**

**Sample Input**
<br><br> 6
<br>01/01/2024, Narration 6, 0.0, 400.0, 10400.0
<br>01/01/2024, Narration 5, 300.0, 0.0, 10000.0
<br>01/01/2024, Narration 1, 100.0, 0.0, 9900.0
<br>01/01/2024, Narration 3, 200.0, 0.0, 9800.0
<br>01/01/2024, Narration 2, 0.0, 100.0, 10000.0
<br>01/01/2024, Narration 4, 0.0, 500.0, 10300.0

<br>

**Output for the above input**
<br>
<br>Date     Narration  Debit Amount  Credit Amount  Closing Balance
<br>0  01/01/2024  Narration 1         100.0           0.0           9900.0
<br>1  01/01/2024  Narration 2           0.0         100.0          10000.0
<br>2  01/01/2024  Narration 3         200.0           0.0           9800.0
<br>3  01/01/2024  Narration 4           0.0         500.0          10300.0
<br>4  01/01/2024  Narration 5         300.0           0.0          10000.0
<br>5  01/01/2024  Narration 6           0.0         400.0          10400.0
