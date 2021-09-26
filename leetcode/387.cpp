class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, pair<int,int>> mp;
        for(int i =0; i<s.size(); i++)
        {
            if(mp[s[i]].first > 0) 
            {
                mp[s[i]].second = INT_MAX;
            }
            else 
            {
                mp[s[i]]=make_pair(1,i);
            }
        }
        int min = INT_MAX;
        for(auto i:mp)
        {
            if(i.second.second < min)
                min = i.second.second;
        }
    return min==INT_MAX ? -1 : min;
    }
};