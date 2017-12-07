# illumio

## Coding Challenge

Hello! I enjoyed thinking about this coding challenge, and unfortunately spent too much time thinking about what I *could* have done instead of doing things. However, I was able to implement a naive solution that works - at the cost of performance. If you run the program with the included csv file, it will take ~4 minutes to complete. While I understand that this does not mimic real world performance at all, if I had longer, I would use a scalable probabilistic data structure such as a Bloom Filter which would significantly improve efficiency. I also recognize that my current solution can be tweaked without changing the core algorithm to improve runtime.

Essentially, a generative solution like mine is not the ideal way to approach a problem like this. I understand this and would fix it if I had longer than 60mins. I don't think there is a portion of the code that requires explicit explanation, but I would've also done a better job of documentation and variable naming if I had more time.

Another thing that I did not do as well is testing. I ran a few cases (including the edge case where both ports and IPs are ranges) but I realized that building a larger csv file would take longer.

Thank you. I hope this is a good enough solution though!

Vivek
