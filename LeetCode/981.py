class TimeMap:

    def __init__(self):
        self.time_map = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((timestamp, value))
        else:
            self.time_map[key] = [(timestamp, value)] 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        values_list = self.time_map[key]
        value_at_timestamp = self.search_timestamp(values_list, timestamp, 0, len(values_list) - 1)
        return value_at_timestamp[1]

    def search_timestamp(self, values_list, timestamp, left, right):
        if left >= right:
            if values_list[right][0] <= timestamp:
                
                return values_list[right]
            else:
                if left == len(values_list) - 1 and left > 0:
                    if timestamp > values_list[left][0]:
                        return values_list[left]
                    else:
                        return values_list[left-1]
                if right > 0:
                    return values_list[right - 1]
                else: 
                    return (timestamp, "")
        
        mid = (left + right) // 2

        if values_list[mid][0] == timestamp:
            return values_list[mid]
        elif values_list[mid][0] > timestamp:
            return self.search_timestamp(values_list, timestamp, left, mid - 1)
        else:
            return self.search_timestamp(values_list, timestamp, mid + 1, right)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)