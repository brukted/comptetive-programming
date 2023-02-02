class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        results = []

        for idx, log in enumerate(logs):
            identifier, content = log.split(" ", 1)
            is_digit_log = content[0].isdigit()

            results.append(
                [int(is_digit_log), idx if is_digit_log else content, identifier, log]
            )

        results.sort()
        return list(map(lambda x: x[-1], results))
