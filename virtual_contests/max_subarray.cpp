int best = 0, sum = 0;
int array = []
for (int k = 0; k < n; k ++){
    sum = max(array[k],sum + array[k]);
    best = max(best,sum);
}
cout << best << "\n";