class SegmentTree:
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None
        self.value = 0
def build_segment_tree(st, arr, l, r):
    if l == r:
        st.value = arr[l]
    else:
        st.left = SegmentTree(st.index*2)
        build_segment_tree(st.left, arr, l, (l+r) >> 1)
        st.right = SegmentTree(st.index*2 + 1)
        build_segment_tree(st.right, arr, ((l+r) >> 1) + 1, r)
        if st.left and st.right is not None:
            st.value = max(st.left.value, st.right.value)
    return st

def rmq(st, l, r, i, j):
    if l >= i and r <= j:
        return st.value
    t1 = rmq(st.left, l, (l+r) >> 1, i, j)
    t2 = rmq(st.right, ((l+r) >> 1) + 1, r, i, j)
    return max(t1, t2)
def rmq_caller(i, j):
    return rmq(st, 0, n - 1, i, j)
n, q = map(int, input().split())
a = list(map(int, input().split()))
frequency = [a.count(i) for i in a]
st = SegmentTree(1)
st = build_segment_tree(st, frequency, 0, n - 1)
for _ in range(q):
    a, b = map(int, input().split())
    res = rmq_caller(a, b)
    print(res)