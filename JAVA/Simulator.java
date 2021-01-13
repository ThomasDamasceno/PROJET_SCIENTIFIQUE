import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import org.json.simple.parser.ParseException;

/**
 * Created on 2020-12-11 by Damasceno Thomas
 */

class Simulator {

    public static void main(String[] args) throws InterruptedException, IOException, ParseException {
        List<Fire> fires = new ArrayList<Fire>();
        WebService eth = new WebService();
        Random rand = new Random();
        List<FireTruck> trucks = null;

        while (true) {
            trucks = eth.getFireTrucks();

            if (rand.nextDouble() < 0.01) {
                fires.add(new Fire());
            }

            for (Fire fire : fires) {
                fire.spread();
            }

            for(FireTruck truck : trucks) {
                if(truck.status == 1) {
                    if(truck.hasArrived()) {
                        truck.extinguish();
                    } else {
                        truck.move();
                    }
                }
            }
         
            if (!fires.isEmpty())
                eth.JsonRequest("POST", "http://0.0.0.0:8080/feu/FEU/enregistre.php", fires.toString());

            if(!trucks.isEmpty())
                eth.JsonRequest("POST", "http://0.0.0.0:8080/feu/FEU/update-position.php", trucks.toString());

            Thread.sleep(10000);
        }
    }

}