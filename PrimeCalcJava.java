public class PrimeCalcJava {
    public static long max_range = 100000;

    public static void main(String[] args) {
        long count = 0;

        for (long dividend = 1; dividend < max_range + 1; dividend++) {

            boolean is_prime = true;
            for (long divisor = 2; divisor < dividend; divisor++) {
                if (dividend % divisor == 0)  {
                    is_prime = false;
                    break;
                }
            }

            if (!is_prime) {
                continue;
            }
            count++;

        }
        System.out.println(count);
}
}

