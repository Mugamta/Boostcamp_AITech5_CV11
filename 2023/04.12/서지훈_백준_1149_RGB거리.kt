import java.io.*
import java.util.StringTokenizer

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val N = br.readLine().toInt()

    var prev_house_R_min_cost = 0
    var prev_house_G_min_cost = 0
    var prev_house_B_min_cost = 0

    for(i in 1..N){
        val st = StringTokenizer(br.readLine());
        val R = st.nextToken().toInt()
        val G = st.nextToken().toInt()
        val B = st.nextToken().toInt()

        val R_cost = R + Integer.min(prev_house_G_min_cost, prev_house_B_min_cost)
        val G_cost = G + Integer.min(prev_house_R_min_cost, prev_house_B_min_cost)
        val B_cost = B + Integer.min(prev_house_R_min_cost, prev_house_G_min_cost)

        prev_house_R_min_cost = R_cost
        prev_house_G_min_cost = G_cost
        prev_house_B_min_cost = B_cost
    }

    bw.write(Integer.min(prev_house_R_min_cost, 
        Integer.min(prev_house_G_min_cost, prev_house_B_min_cost)).toString())

    bw.flush()
    bw.close()
    br.close()
}