# Election_Analysis

## Project Overview
A Colorado Board of Elections employee wishes to accomplish the following election audit of arecen local congressional election.

1. Sum the number of total votes cast.
2. List all candidates who received at least one vote.
3. Tally the votes per each candidate listed.
4. Compute the percentage of votes each candidate received as a portion of the total.
5. Determine the winner of the election based on popular vote. 

## Resources
- Data source: election_results.csv
- Software: Python 3.7.9

## Summary
The analysis of the election show (also find this in the output txt file): 

```
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
```
The winner is Diana DeGette with 73.8% of the popular vote. While not a "landslide," she won by a good margin!

# Election Challenge: Deliverable 3

## Overview of Election Audit

The purpose of the election audit was to determine a winner among the candidates and to determine voter turnout among the counties in the precinct. 

## Election-Audit Results
- How many votes were cast in this congressional election?
  ```
  Total Votes: 369,711
  ```
- Breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  ```
  County Votes:
  Jefferson: 10.5% (38,855)
  Denver: 82.8% (306,055)
  Arapahoe: 6.7% (24,801)
  ```

- Which county had the largest number of votes?
  ```
  Largest County Turnout: Denver
  ```
  
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  ```
  Charles Casper Stockham: 23.0% (85,213)
  Diana DeGette: 73.8% (272,892)
  Raymon Anthony Doane: 3.1% (11,606)
  ```

-Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  ```
  Winner: Diana DeGette
  Winning Vote Count: 272,892
  Winning Percentage: 73.8%
  ```
  
## Election-Audit Summary

I propose that this script can be used, with some modifications, for any election. Because niether the candidate names, nor the county names are hard-coded, the data can be read and utilized to deliver the desired results. With the addition of a data file containing the number of registered voters per county, an acutal turnout percentage could be calculated easily by comparing the count of votes per county to the registered voter count. Further, this script can be modified to show the results of ranked-choice voting. 

