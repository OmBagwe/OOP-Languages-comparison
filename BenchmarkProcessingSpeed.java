import java.time.Duration;
import java.time.Instant;
import com.google.gson.Gson;

public class BenchmarkProcessingSpeed {
    public static void main(String[] args) {
        Instant start = Instant.now();
        long result = 0;
        for (long i = 0; i < 10000000; i++) {
            result += i;
        }
        Instant end = Instant.now();
        long processingSpeed = Duration.between(start, end).toMillis();
        Gson gson = new Gson();
        System.out.println(gson.toJson(new Result(processingSpeed)));
    }

    static class Result {
        long processingSpeed;

        public Result(long processingSpeed) {
            this.processingSpeed = processingSpeed;
        }
    }
}
