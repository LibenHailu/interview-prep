class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        email_to_name = {}
        email_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = i
                    i += 1

        n = len(email_to_name)

        pars = [node for node in range(n)]
        ranks = [1 for i in range(n)]

        def find(n1):
            if n1 != pars[n1]:
                return find(pars[n1])

            return n1
#             while n1 != pars[n1]:
#                 n1 = pars[n1] = pars[pars[n1]]

#             return n1

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return False

            if ranks[r1] > ranks[r2]:
                pars[r2] = r1

            elif ranks[r2] > ranks[r1]:
                pars[r1] = r2

            else:
                pars[r2] = r1
                ranks[r1] += 1

            return True

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                union(email_to_id[acc[1]], email_to_id[email])

        components = collections.defaultdict(list)
        for email in email_to_name:
            components[find(email_to_id[email])].append(email)

        return [[email_to_name[v[0]]] + sorted(v) for k, v in components.items()]
