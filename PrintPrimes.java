public class PrintPrimes {
    public static void main(String[] args) {
        int limit = 100;
        System.out.println("Prime numbers up to " + limit + ":");

        for (int number = 2; number <= limit; number++) {
            if (isPrime(number)) {
                System.out.print(number + " ");
            }
        }
    }

    private static boolean isPrime(int value) {
        if (value <= 1) {
            return false;
        }
        for (int i = 2; i * i <= value; i++) {
            if (value % i == 0) {
                return false;
            }
        }
        return true;
    }
}
