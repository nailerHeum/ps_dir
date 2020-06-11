class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_dict = {}
        answer = []
        a_arr, b_arr = (nums1, nums2) if len(nums1) <= len(nums2) else (nums1, nums2)
        for n in a_arr:
            if n in num_dict:
                num_dict[n] += 1
                continue
            num_dict[n] = 1
        for n in b_arr:
            if n in num_dict and num_dict[n] > 0:
                num_dict[n] -= 1
                answer.append(n)
        return answer
