import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class WebService {

    public void request(String method, String address, byte[] body) throws IOException {     
        HttpURLConnection http = (HttpURLConnection) (new URL(address)).openConnection();
        
        http.setRequestMethod(method); 
        http.setDoOutput(true);

        http.setFixedLengthStreamingMode(body.length);
        http.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
        http.connect();
        try(OutputStream os = http.getOutputStream()) {
            os.write(body);
        }
    }

    public void JsonRequest(String method, String address, String body) throws IOException  {
        request(method, address, body.getBytes(StandardCharsets.UTF_8));
    }

}