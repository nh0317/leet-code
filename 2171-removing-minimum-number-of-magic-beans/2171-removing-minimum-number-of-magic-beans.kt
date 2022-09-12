import kotlin.math.*

class Solution {
    fun minimumRemoval(beans: IntArray): Long {
        
        beans.sort()
        var n = beans.size
        var summ : Long = 0L
        for (bean in beans){
            summ += bean.toLong()
        }
        var minn = Long.MAX_VALUE
        
        for (i in 0 until n){
            val outs = summ - (beans[i].toLong() * (n - i).toLong())
            if (outs >= 0)
                minn = min(outs, minn)
        }
        return minn
    }
}