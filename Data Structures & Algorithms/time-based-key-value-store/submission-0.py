class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value = self.dic.get(key, [])
        left, right = 0, len(value) - 1
        while left <= right:
            mid = (left + right) // 2
            if value[mid][1] <= timestamp:
                res = value[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res