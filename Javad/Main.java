import java.util.Arrays;
import java.util.Random;

public class SearchComparison {
    public static void main(String[] args) {
        int arraySize = 1000000;
        int[] arr = new int[arraySize];
        Random rand = new Random();

        for (int i = 0; i < arraySize; i++) {
            arr[i] = rand.nextInt(1000000);
        }
        
        Arrays.sort(arr);
        
        int target = rand.nextInt(1000000);

        long startTime = System.nanoTime();
        linearSearch(arr, target);
        long linearTime = System.nanoTime() - startTime;

        startTime = System.nanoTime();
        binarySearch(arr, target);
        long binaryTime = System.nanoTime() - startTime;

        System.out.println("زمان جستجوی معمولی: " + (linearTime / 1_000_000_000.0) + " ثانیه");
        System.out.println("زمان جستجوی باینری: " + (binaryTime / 1_000_000_000.0) + " ثانیه");
    }

    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}
