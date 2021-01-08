package test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;


/**
 * Created on 2020-12-11 by Damasceno Thomas
 */

class Simulator {

    public static void main(String[] args) throws InterruptedException, IOException {
        List<Fire> fires = new ArrayList<Fire>();
        WebService eth = new WebService();
        Random rand = new Random();

        while (true) {

            if (rand.nextDouble() < 0.1) {
                fires.add(new Fire());
            }

            for (Fire fire : fires) {
                fire.spread();
            }

            if (!fires.isEmpty())
                eth.JsonRequest("POST", "http://localhost/Feu/Simulator/BACKEND/enregistre.php", fires.toString());
            Thread.sleep(10000);
        }
    }

}