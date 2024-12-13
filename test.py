from ensure import ensure_annotations


@ensure_annotations
def get_predict(x: int, y: int) -> int:
    return x * y


print(get_predict(2, 3))
print(get_predict(x=2, y="3"))