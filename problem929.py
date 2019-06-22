#problem 929 /Unique Email Addresses
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        elist = {}
        for n,email in enumerate(emails):
            i = 0
            while i < len(email):
                if email[i] == '.':
                    email = email[:i]+email[i+1:]
                if email[i] == '+':
                    email = email[:i]+email[email.find('@'):]
                if email[i] == '@':
                    break
                i = i+1
            if email not in elist:
                elist[email] = n
        print(elist)
        return len(elist)

#approach 2 using string functions -- .split / .replace / .index
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        elist = {}
        for i,email in enumerate(emails):
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.','')
            total = local+'@'+domain
            elist[total] = i
        return len(elist)