import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import com.google.gson.Gson;

public class BenchmarkEfficiency {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < 1000000; i++) {
            list.add(random.nextInt(1000000));
        }
        Instant start = Instant.now();
        Collections.sort(list);
        Instant end = Instant.now();
        long efficiency = Duration.between(start, end).toMillis();
        Gson gson = new Gson();
        System.out.println(gson.toJson(new Result(efficiency)));
    }

    static class Result {
        long efficiency;

        public Result(long efficiency) {
            this.efficiency = efficiency;
        }
    }
}
