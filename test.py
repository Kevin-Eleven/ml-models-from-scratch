"""
void solve() {
  int n;
  cin >> n;
  string s;
  cin >> s;
  vi ops(n+1,0),ops2(n+1,0);

  int i = 0;

  while(s[i] != '1')i++;
  int d = 1;
  int j = i+1;
  while(j < n){
    if(s[j] == '0'){
      ops[d]++;
      d++;
    }else{
      d = 1;
    }
    j++;
  }
  j = 0;
  while(j < i){
    if(s[j] == '0'){
      ops[d]++;
      d++;
    }else{
      d = 1;
    }
    j++;
  }
  d=1;
  j = i-1;
  while(j >= 0){

    if(s[j] == '0'){
      ops2[d]++;
      d++;
    }else{
      d = 1;
    }
    j--;
  }

  j = n-1;
  while( j > i){
    if(s[j] == '0'){
      ops2[d]++;
      d++;
    }else{
      d = 1;
    }
    j--;
  }

  int k = 0;
  int ans = 0;
  for(int i = 1; i<=n;i++){
    if(ops[i] > 0){
      ans += (i-k)>0?1:0;
      k++;
    }
  }
  k = 0;
  int ans2 = 0;
   for(int i = 1; i<=n;i++){
    if(ops2[i] > 0){
      ans2 +=(i-k)>0?1:0;
      k++;
    }
  }

 cout << min(ans, ans2) << endl;

}

cpp sol
"""

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = input()

    i = 0
    while s[i] != "1":
        i += 1

    print(i)
