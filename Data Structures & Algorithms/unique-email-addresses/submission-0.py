class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        '''
        localname@domainname
        If periods are there in local name, remove dots, forward to same email address.
        everything in local name after the + sign is ignored.
        
        continue to loop until + sign is found, ignore rest until @, then append domain
        '''
        unique_emails = set()

        for email in emails:
            char_counter, simplified_email = 0, ""
            while email[char_counter] != '@' and email[char_counter] != '+':
                if email[char_counter] != '.':
                    simplified_email += email[char_counter]
                
                char_counter += 1
            
            #Only if you get +, ignore subsequent characters until @
            while email[char_counter]!= "@":
                char_counter += 1
            
            email_domain = email[char_counter+1:]
            simplified_email += email_domain
            unique_emails.add(simplified_email)
        
        return len(unique_emails)


