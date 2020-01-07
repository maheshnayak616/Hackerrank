class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_list = set()
        for x in emails:
            actual_user_name, domain = x.split("@")
            user = actual_user_name.split("+")[0].replace(".", "")
            email_list.add(user + "@" + domain)
        return len(email_list)

if __name__ == '__main__':
    s = Solution()
    s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])