class Solution:
    def reformatDate(self, date: str) -> str:
        months = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        day, month, year = date.split(" ")
        day = "".join(filter(str.isdigit, day))

        month = str(months.index(month) + 1)
        month = ("0" if len(month) == 1 else "") + month

        day = ("0" if len(day) == 1 else "") + day

        return f"{year}-{month}-{day}"
