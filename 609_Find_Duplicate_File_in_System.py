# https://leetcode.com/problems/find-duplicate-file-in-system/description/
# Medium

class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        # dictionary of content to list of file paths
        content_to_file_path = {}
        for info in paths:
            parts = info.split(" ")
            root = parts[0]
            for file in parts[1:]:
                endOfFileName = file.index('(')
                filename = file[:endOfFileName]
                content = file[endOfFileName+1:-1]
                if content not in content_to_file_path:
                    content_to_file_path[content] = []
                content_to_file_path[content].append(root + "/" + filename)

        return [content_to_file_path[content] 
                    for content in content_to_file_path 
                    if len(content_to_file_path[content]) > 1]