# 불리언(bool) : True, False
# 파이썬에서는 비어있는 값은 False로 평가된다.
# 0, 0.0, None, '', "", [], (), {}, set()
print("=== False ===")
print(f"{0}, {bool(0)}")
print(f"{0.0}, {bool(0.0)}")
print(f"{''}, {bool('')}")
print(f"{[]}, {bool([])}")
print(f"{()}, {bool(())}")
print(f"{ {}}, {bool({})}")
print(f"{set()}, {bool(set())}")
print(f"{None}, {bool(None)}")

print("=== True ===")
print(f"{1}, {bool(1)}")
print(f"{-1}, {bool(-1)}")
print(f"{0.12}, {bool(0.12)}")
print(f"{'num'}, {bool('num')}")
print(f"{[1]}, {bool([1])}")
print(f"{(1,)}, {bool((1,))}")
print(f"{{'a':1}}, {bool({'a':1})}")

