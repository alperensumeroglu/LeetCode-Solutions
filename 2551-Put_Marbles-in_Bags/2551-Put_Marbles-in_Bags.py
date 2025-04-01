class Solution:
    def putMarbles(self, weights, k):
        """
        ------------------------------------------------------------
        🧠 Intuition:
        ------------------------------------------------------------
        We are given weights of marbles and asked to split them into k non-empty contiguous bags.
        The cost of each bag is the sum of its first and last element.
        The goal is to find the difference between the **maximum** and **minimum** total bag costs 
        over all possible valid k-partitions.

        ------------------------------------------------------------
        🧩 Approach:
        ------------------------------------------------------------
        - To divide into k contiguous bags, we must make (k-1) cuts between elements.
        - Each cut defines two new bag boundaries.
        - The only places cuts can be made are between adjacent weights (i and i+1).
        - We compute all adjacent pair sums: weights[i] + weights[i+1].
        - To get the **minimum total cost**, we choose the smallest (k-1) pair sums.
        - To get the **maximum total cost**, we choose the largest (k-1) pair sums.
        - Return the difference between these two total scores.

        ------------------------------------------------------------
        ⚠️ Edge Case Handling:
        ------------------------------------------------------------
        - If weights is empty or has only one element, result is always 0.
        - If k == 1, no cut is made → only one bag → difference is 0.
        - If k == len(weights), every marble is in its own bag → each bag's cost is weights[i] + weights[i] = 2 * weights[i]
          But since all configurations are the same, difference is 0.
        - If k > len(weights), it's invalid by definition – but if such input is given, we treat it safely.

        ------------------------------------------------------------
        ⏱️ Complexity:
        ------------------------------------------------------------
        Time Complexity  : O(n log n) – sorting the pair sums
        Space Complexity : O(n) – storing pair sums

        ------------------------------------------------------------
        🎙 Weekly Rewind is NOW LIVE! 🚀
        ------------------------------------------------------------
        🚀 What does it take to grow as a Computer Engineering student, build projects, and explore global innovation?  
        Weekly Rewind is my real-time documentary where I share what I’m working on, what I’ve learned,  
        and the challenges I’ve faced — from coding breakthroughs to lessons from different countries and cultures.

        💡 What is Weekly Rewind?  
        A behind-the-scenes look at real-world experiences, global insights, and hands-on learning. Each episode includes:  
        🔹 Inside My Coding & Engineering Projects  
        🔹 New Steps in My Entrepreneurial Journey  
        🔹 Cutting-Edge Tech & AI Trends  
        🔹 Global Innovation from 15+ Countries  
        🔹 Guest Conversations  
        🔹 University Life, Productivity & Growth  
        🔹 Lessons from My Journey

        🌍 True learning happens when you build real projects, step outside your comfort zone, and explore the world.

        🎧 Listen Now:  
        🔹 Spotify: https://open.spotify.com/show/3Lc5ofiXh93wYI8Sx7MFCK  
        🔹 YouTube: https://www.youtube.com/playlist?list=PLSN_hxkfsxbbd_qD87kn1SVvnR41IbuGc  
        📖 Medium: https://medium.com/@alperensumeroglu  
        💼 LinkedIn: https://www.linkedin.com/company/weekly-rewind-tech-ai-entrepreneurship-podcast/

        #WeeklyRewind #TechPodcast #BuildInPublic #GlobalTech #AIInsights
        ------------------------------------------------------------
        """

        n = len(weights)

        # Edge Case: Not enough marbles or invalid k
        if n <= 1 or k <= 1 or k > n:
            return 0

        # Step 1: Compute pair sums (adjacent elements)
        pair_sums = []
        for i in range(n - 1):
            pair_sums.append(weights[i] + weights[i + 1])

        # Step 2: Sort the pair sums
        pair_sums.sort()

        # Step 3: Compute min and max score using (k-1) smallest/largest pair sums
        min_score = sum(pair_sums[:k - 1])
        max_score = sum(pair_sums[-(k - 1):])

        # Step 4: Return the difference
        return max_score - min_score
