import java.io.*
import java.math.BigInteger

fun matrixMultiply(mat1: Array<LongArray>, mat2: Array<LongArray>): Array<LongArray> {
    return arrayOf(
        longArrayOf(
            (mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % 1000000,
            (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % 1000000
        ), longArrayOf(
            (mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % 1000000,
            (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % 1000000
        )
    )
}

fun matrixPow(exponent: BigInteger, matrix: Array<LongArray>): Array<LongArray> {
    if (exponent.compareTo(BigInteger("1")) > 0) {
        val res = matrixPow(exponent.divide(BigInteger("2")), matrix)
        return if (exponent.mod(BigInteger("2")) == BigInteger("1")) {
            matrixMultiply(matrix, matrixMultiply(res, res))
        } else matrixMultiply(res, res)
    }
    return matrix
}

fun fibonacci(n: BigInteger): Long {
    val matrix = arrayOf(longArrayOf(1, 1), longArrayOf(1, 0))
    return matrixPow(n, matrix)[1][0]
}

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    bw.write(fibonacci(BigInteger(br.readLine())).toString())

    bw.flush()
    bw.close()
    br.close()
}