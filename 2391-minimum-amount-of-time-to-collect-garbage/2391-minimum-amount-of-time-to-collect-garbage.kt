
class Solution {
    fun garbageCollection(garbage: Array<String>, travel: IntArray): Int {
        
        var cnt = 0
        var arr : Array<Int> = arrayOf(0,0,0)
        for(i in 0 until garbage.size){
            if ("P" in garbage[i])
                arr[0] = i 
            
            if ("G" in garbage[i])
                arr[1] = i
            
            if ("M" in garbage[i])
                arr[2] = i
            
            cnt += garbage[i].length
        }
        
        for (i in arr)
            cnt += travel.slice(0..i-1).sum()
            
        return cnt
        
    }
}