class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        grouped = []
        i = 0
        digits = list(map(int, str(num)))[::-1]

        while i < len(digits):
            grouped += [digits[i : i + 3]] if i + 2 < len(digits) else [digits[i:]]
            i += 3

        grouped = grouped[::-1]

        ones = [
            None,
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        teens = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            None,
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        powers = [None, "Thousand", "Million", "Billion", "Trillion", "Quadrillion"]

        def numberToWordsRec(digits):
            if len(digits) == 1:
                if digits[0] == 0:
                    return []
                else:
                    return [ones[digits[0]]]

            elif len(digits) == 2:
                if digits[0] == 0:
                    return numberToWordsRec(digits[1:])
                else:
                    if digits[0] == 1:
                        return [teens[digits[1]]]
                    else:
                        return [tens[digits[0]]] + numberToWordsRec(digits[1:])

            elif len(digits) == 3:
                if digits[0] == 0:
                    return numberToWordsRec(digits[1:])
                else:
                    return [ones[digits[0]], "Hundred"] + numberToWordsRec(digits[1:])

        ans = []
        for idx, group in enumerate(grouped):
            group = group[::-1]
            three = numberToWordsRec(group)
            n = powers[len(grouped) - idx - 1]
            if three:
                ans += three
                if n is not None:
                    ans.append(n)

        return " ".join(ans)
