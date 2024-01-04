import java.io.*;
import java.math.BigInteger;

public class Main {
    public static long[][] matrix_multiply(long[][] mat1, long[][] mat2){
        return new long[][]{{(mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % 1000000,
                (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % 1000000},
                {(mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % 1000000,
                        (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % 1000000}};
    }

    public static long[][] matrix_pow(BigInteger exponent, long[][] matrix){
        if (exponent.compareTo(new BigInteger("1")) > 0){
            long[][] res = matrix_pow(exponent.divide(new BigInteger("2")), matrix);
            if (exponent.mod(new BigInteger("2")).equals(new BigInteger("1"))){
                return matrix_multiply(matrix, matrix_multiply(res, res));
            }
            return matrix_multiply(res, res);
        }
        return matrix;
    }

    public static long fibonacci(BigInteger n){
        long [][] matrix = {{1, 1}, {1, 0}};
        return matrix_pow(n, matrix)[1][0];
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        bw.write(Long.toString(fibonacci(new BigInteger(br.readLine()))));

        bw.flush();
        bw.close();
        br.close();
    }
}
