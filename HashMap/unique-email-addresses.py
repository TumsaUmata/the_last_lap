class Solution:
    def numUniqueEmails(self, emails) -> int:
        emails_set = set()
        for email in emails:
            name, domain = email.split("@")
            local = name.split("+")[0].replace('.', '')
            emails_set.add(local + "@" + domain)
        return len(emails_set)
