# **Question 1**

## *Study the enron scandal data and perform three useful analysis*

### **Analysis 1**
    
#### *Investigate the fradulent words usage in emails of top three convicts between 1999-2001*
    
- Read all the emails, present under each and every directory, of top three convicts
- Created a sample list containing majority of fradulent words used in scams worldwide
- Compared each fradulent word with every word present under email body of top three convicts
- Created a dictionary to store the fradulent words and count of number of times it has been used
- Displayed the top 5 most used fradulent words by top three convicts
- Created a graph to display the fradulent words usage in an intuitive manner

#### *Conclusion*
    
- There was a high usage of few fradulent words like **'investment', 'payment', and 'cover'**
- This clearly points to the fact that some discrepancy was going on among top level executives


### **Analysis 2**
    
#### *Investigate the number of emails that top three convicts sent to other employees*
    
- Read all the emails, present under each and every directory, of top three convicts
- Counted the number of emails each convict sent to other employees
- Created three dictionaries to store the employee emaild id and count of number of times they have received emails
- Displayed the top 5 employees to whom top three convicts sent the mail frequently
- Plotted a graph to display the collected information visually

#### *Conclusion*
    
- There was a high volume of email exchange between the top three convicts
- Analysis showed that out of top 5 employee that each exchanged emails with, the other two were present in top 5
- This is a conclusive evidence alongwith Analysis 1 that they were involved in some dirty business
    

### **Analysis 3**
    
#### *Investigate the emails that CEO received  from affected people due to scam*
    
- Read all the emails of the CEO Kenneth Lay
- Created a list containing words normally used in a request for a refund
- Tokenized the Subject in CEO's email and compared each word with plea word
- If 50% of the plea words are present in email subject then considered that mail as a plea request
- Displayed a sample list of 10 people containing names and emailids, who mailed CEO for refund

#### *Conclusion*
    
- Based on the email subject we can say that all section of the society was affected by this scam
- Analysis showed that majority of people who mailed have lost all of their money and are in very serious trouble




# **Question 2**

## *Fetch and Store the NYT data from NYT API  and perform three useful analysis*

### **Data Fetch and Data Storage**

- Prepared few lists of year, month and year_month for archive api
- Prepared few lists of article categories, most popular section for most popular api
- Created the directory hierarchy for archive and most popular api
- Created url to fetch data from archive and most popular api
- Stored the received response with json extension in the local path where the ipynb file resides.
- Moved the file to the respective directory hierarchies of archive and most popular api

### **Analysis 1**
    
#### *Analyze the content of NYT archive data from 1996-2016 and throw light on NYT publication trend*
    
- Analyzed each article and captured its publication category from past 20 years
- Stored all the categories alongwith its id, publication date and headline
- Calculated the category and count of number of times it has been published
- Printed the top ten article categories alongwith its frequency
- Plotted a graph to show captured information visually

#### *Conclusion*
    
- For the past 20 years the areas where NYT focussed more is Metropolitan News, Classified News, Sports News, Financial and Business news


### **Analysis 2**
    
#### *Analyze the relationship between emailing, sharing and viewing of most popular articles for past 30 days*
    
- Read all the emails, present under each and every directory, of top three convicts
- Counted the number of emails each convict sent to other employees
- Created three dictionaries to store the employee emaild id and count of number of times they have received emails
- Displayed the top 5 employees to whom top three convicts sent the mail frequently
- Plotted a graph to display the collected information visually

#### *Conclusion*
    
- About 24% of the articles were viewed and emailed
- About 29% of the articles were viewed and shared
- About 50% of the articles were emailed and shared
- About 15% of the articles were common to email, shared and viewed api articles
- It can be said that for the past 30 days there were very limited attracting articles worth viewing, sharing and emailing
    

### **Analysis 3**
    
#### *Analyze the number of articles NYT published related to terror activities for past 20 Years*
    
- Searched internet and created a list containing terror related words and countries with high rates of terrorism
- Analyzed each article under archive package and captured articles with terror related data from past 20 years
- Calculated frequency of terror related articles yearwise
- Printed the top ten year in which nyt published more terror related documents
- Plotted a graph to show captured information visually

#### *Conclusion*
    
- Based on the data captured, NYT reported high terror related activities around the globe in 2002, 2003, 2004, 2011 and 1997

    