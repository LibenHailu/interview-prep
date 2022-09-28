

void solve()
{
    long long n, k;
    cin >> n >> k;
    vector<long long> a(n), ans(k);

    for (int i = 0; i < n; i++)
        cin >> a[i];

    for (int i = 0; i < n; i++)
    {
        ans[(i + 1) % k] = max(ans[(i + 1) % k], a[i]);
    }

    long long out = 0;

    for (int i = 0; i < k; i++)
        out += ans[i];

    cout << out << endl;
}

signed main()
{
    int tc = 1;
    cin >> tc;
    for (int i = 1; i <= tc; i++)
    {
        solve();
    }
}