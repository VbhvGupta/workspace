class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len = prices.size();
        int profit = 0;
        int i=0 ;
        while(i+1 < len)
        {
            if(prices[i] < prices[i+1])
            {
                profit += prices[i+1] - prices[i] ;
            }
            i+=1;
        }
        return profit;
    }
};
