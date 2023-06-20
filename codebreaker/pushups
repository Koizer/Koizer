#include <algorithm>
#include <cstring>
#include <stdio.h>
#include <vector>
using namespace std;
typedef long long ll;

const int INF = 1e6;
vector<int> segTree, a;

int build(int idx, int l, int r) {
    if (l == r) {
        segTree[idx] = a[l];
        return segTree[idx];
    }

    int mid = (l + r) / 2;
    return segTree[idx] = max(build(idx * 2, l, mid), build(idx * 2 + 1, mid + 1, r));
}

int query(int idx, int l, int r, int x, int y) {
    if (r < x || l > y) return 0;
    if (l >= x && y >= r) return segTree[idx];

    int mid = (l + r) / 2;
    return max(query(idx * 2, l, mid, x, y), query(idx * 2 + 1, mid + 1, r, x, y));
}

int main() {
    int t; scanf("%d", &t);
    a = vector<int>(INF + 2, 0);
    segTree = vector<int>(4 * INF + 2);

    for (int i = 1; i <= INF; i++)
        for (int j = i; j <= INF; j += i)
            a[j] += i;

    build(1, 1, INF);

    while (t--) {
        int n; scanf("%d", &n);
        printf("%d\n", query(1, 1, INF, 1, n));
    }
}
