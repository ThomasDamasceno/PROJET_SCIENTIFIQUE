import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.json.simple.parser.ParseException;

/***
 * 2021-01-06
 */

public class EmergencyManager {
    public static void main(String[] args) throws InterruptedException, IOException, ParseException {
        WebService eth = new WebService();
        List<Fire> fires = new ArrayList<Fire>();
        List<FireTruck> trucks = new ArrayList<FireTruck>();

        while (true) {
            Object[] a = eth.getFireTrucks();
            fires = (List<Fire>) a[0];
            trucks = (List<FireTruck>) a[1];

            for (FireTruck truck : trucks) {
                if(truck.status == 0) {
                    truck.assignFire(fires);
                }                
            }          
            
            System.out.println(trucks.toString());
            Thread.sleep(10000);
        }
    }
}
