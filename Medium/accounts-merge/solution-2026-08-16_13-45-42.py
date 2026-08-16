class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        email_to_name = {}
        parents = {}

        def find(p):
            if parents[p] != p:
                parents[p] = find(parents[p])
            return parents[p]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parents[root_x] = root_y

        for a in accounts:
            name = a[0]
            first_email = a[1]
            emails = a[1:]

            for email in emails:
                email_to_name[email] = name
                if email not in parents:
                    parents[email] = email
                root = find(email)
                union(root, first_email)
        
        groups = defaultdict(list)
        for kid in parents:
            root = find(kid)
            groups[root].append(kid)
        
        res = []
        for parent, kids in groups.items():
            res.append([email_to_name[parent]] + sorted(kids))
        
        return res