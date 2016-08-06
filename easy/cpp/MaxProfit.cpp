class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        if (prices.size() < 2) return 0;
        
        int ttb = 0;
        int tts = 0;
        int cttb = ttb;
        int ctts = tts;
        for (int i = 1; i < prices.size(); i++){
            if (prices[i] < prices[cttb])
            {   
                cttb = i;
                ctts = i;
            }
            else if (prices[ctts] < prices[i] )
                ctts = i;
            if (prices[tts] - prices[ttb] < prices[ctts] - prices[cttb]){
                tts = ctts;
                ttb = cttb;
            }
           
        }
        return (prices[tts] - prices[ttb] > 0)? prices[tts] - prices[ttb] : 0;
    }
};