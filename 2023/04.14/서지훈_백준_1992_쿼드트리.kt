import java.io.*

lateinit var video: Array<IntArray>
var bw: BufferedWriter? = null

fun recursion(N: Int, x: Int, y: Int) {
    val check = video[y][x]
    for (i in y until y + N) {
        for (j in x until x + N) {
            if (check != video[i][j]) {
                bw!!.write("(")
                recursion(N / 2, x, y)
                recursion(N / 2, x + N / 2, y)
                recursion(N / 2, x, y + N / 2)
                recursion(N / 2, x + N / 2, y + N / 2)
                bw!!.write(")")
                return
            }
        }
    }
    if (check == 0) bw!!.write("0") else bw!!.write("1")
}

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    bw = BufferedWriter(OutputStreamWriter(System.out))
    val N = br.readLine().toInt()
    video = Array(N) { IntArray(N) }
    for (i in 0 until N) {
        val str = br.readLine()
        for (j in 0 until N) {
            video[i][j] = str[j].code - '0'.code
        }
    }
    recursion(N, 0, 0)
    bw!!.flush()
    bw!!.close()
    br.close()
}