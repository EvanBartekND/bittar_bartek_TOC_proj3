Readme_KeoughKitch
Version 1 8/22/24


1.Team name: KeoughKitch

2.Names of all team members: Evan Bartek, Alex Bittar

3.Link to github repository:git@github.com:EvanBartekND/bittar_bartek_TOC_proj3.git

4.Which project options were attempted: Version 1, Problem 1 (NTM) as well as ktape problem.

5.Approximately total time spent on project: 15 hours about, with both of us working. 

6.The language you used, and a list of libraries you invoked: 
Python Language with csv library as well as argparse libraryfor out NTM code. The k-tape code uses python as well as csv in order to read from csv files.

7.How would a TA run your program (did you provide a script to run a test case?):
 They would run python3 code_name -h and it will tell them everything that they need to input in order to run the code for the NTM code. The k-tape code also goes in a similar format: python3 name of code file, path to test file, string to test.

8.A brief description of the key data structures you used, and how the program functioned. 
Lists were used to store the sequence and represent the tapes. Dictionaries are used to store transition functions, Tuples were used for the configuration of the Turing Machine. Same data structures are used for k-tape. We make a k-tape object to find objects inside. Also use sys. 


9.A discussion as to what test cases you added and why you decided to add them (what did they tell you about the correctness of your code). 
Where did the data come from? (course website, handcrafted, a data generator, other) We used the test cases provided under one of the announcemnets from the Canvas site. These were found on the shared google drive.The NTM machines were used as well as the equal number of 0s and 1s test. We made a 2tapeDTM.csv file for a machine that uses two tapes rather than one for our k-tape. This was added so that we had test cases for 1 and 2 tapes that go along with that code.


10.An analysis of the results, such as if timings were called for, which plots showed what? What was the approximate complexity of your program?

NTM machine complexity is exponetial as it depends on the degree of nondeterminism. The K-type problem has a simpler, more normal complexity as there is no Non-determinism involved. 


11.A description of how you managed the code development and testing.

Both worked on codes. We pushed to github and looked over problems with the codes and both debugged. We also both worked on trying to creat tests cases for the k-tape problem. Both analyzied some and did write-ups.


12.Did you do any extra programs, or attempted any extra test cases
 We tried to create different tests cases for k-tape problem as those were not provided in the google drive. Some inculded palindroimes and problems with letters rather than numbers, but we figured that an equal number of 0s and 1s was a good test. We also considered making a reset machine as the seconf code but decided to stick to k-tape as it was already approved on the document.
