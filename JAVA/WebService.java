import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class WebService {

    public String request(String method, String address, byte[] body) throws IOException {
        HttpURLConnection http = (HttpURLConnection) (new URL(address)).openConnection();

        http.setRequestMethod(method);
        http.setDoOutput(true);

        if (body != null)
            http.setFixedLengthStreamingMode(body.length);

        http.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
        http.connect();

        if (body != null)
            try (OutputStream os = http.getOutputStream()) {
                os.write(body);
            }

        if (http.getResponseCode() != 200)
            return null;

        BufferedReader br = new BufferedReader(new InputStreamReader((http.getInputStream())));
        StringBuilder sb = new StringBuilder();
        String output;
        while ((output = br.readLine()) != null) {
            sb.append(output);
        }

        return sb.toString();
    }

    public String JsonRequest(String method, String address, String body) throws IOException {
        return request(method, address, body != null ? body.getBytes(StandardCharsets.UTF_8) : null);
    }

    public Object[] getFireTrucks() throws ParseException, IOException {
        String response = this.JsonRequest("GET", "http://0.0.0.0:8080/liste.php", null);
        List<Fire> fires = new ArrayList<Fire>();
        List<FireTruck> trucks = new ArrayList<FireTruck>();
        JSONObject jo = null;

        JSONArray ja = (JSONArray) new JSONParser().parse(response);

        jo = (JSONObject) ja.get(0);
        JSONArray jaFires = (JSONArray) jo.get("feux");
        jo = (JSONObject) ja.get(1);
        JSONArray jaTrucks = (JSONArray) jo.get("camions");

        for (int i = 0; i < jaTrucks.size(); i++) {
            JSONObject obj = (JSONObject) jaTrucks.get(i);
            GeoCoordinate coor = new GeoCoordinate(Double.parseDouble((String) obj.get("lon")), Double.parseDouble((String) obj.get("lat")));
            FireTruck truck = new FireTruck(coor, Integer.parseInt((String) obj.get("statut")), Integer.parseInt((String) obj.get("id")));
            trucks.add(truck);
        }

        for (int i = 0; i < jaFires.size(); i++) {
            JSONObject obj = (JSONObject) jaFires.get(i);
            GeoCoordinate coor = new GeoCoordinate(Double.parseDouble((String) obj.get("lon")), Double.parseDouble((String) obj.get("lat")));
            Fire fire = new Fire(coor, Integer.parseInt((String) obj.get("intensite")), Integer.parseInt((String) obj.get("id")));
            fires.add(fire);
        }

        Object[] array = { (Object) fires, (Object) trucks };

        return array;
    }

}