# https://leetcode.com/problems/subdomain-visit-count/description/
# Easy

from collections import defaultdict

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = defaultdict(int)
        for count, domain in (d.split(" ") for d in cpdomains):
            parts = domain.split('.')
            for i in range(len(parts)):
                counts['.'.join(parts[i:])] += int(count)
        return [str(count) + " " + domain for domain, count in counts.items()]