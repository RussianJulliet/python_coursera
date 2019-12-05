import sys

print(
    len(
        list(
            filter(lambda x: x == '0', sys.stdin.read())
        )
    ) > 0
)
