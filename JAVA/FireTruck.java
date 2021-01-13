import java.io.IOException;
import java.util.List;

import org.json.simple.parser.ParseException;

public class FireTruck {

    private Coordinate position;

    public int status;

    public int id;

    public int fire_id;

    private Coordinate destination;

    public FireTruck(GeoCoordinate coordinate, int status, int id) {
        this.status = status;
        this.position = new Coordinate(coordinate);
        this.id = id;
    }

    public void assignFire(List<Fire> fires) {
        Double priority = 0.0;
        Double prio = 0.0;
        for (Fire fire : fires) {
            prio = fire.getIntensity() * (1 / fire.getCoordinate().getDistance(this.position));
            if (prio > priority) {
                priority = prio;
                this.fire_id = fire.getId();
                this.status = 1;
            }
        }
    }

    public String toString() {
        return "{\"id\":" + this.id + ",\"statut\":" + this.status + ",\"fire_id\":" + this.fire_id + "}";
    }

    public void setDestination(Coordinate coordinate) {
        this.destination = coordinate;
    }

    public void move() throws IOException, ParseException {
        WebService eth = new WebService();
        GeoCoordinate geo = eth.getNextNode(this.position, this.destination);

        this.position = new Coordinate(geo);
    }

	public boolean hasArrived() {
		return this.position.getDistance(this.destination) < 0.01;
    }
    
    public void extinguish(List<Fire> fires) {
        for (Fire fire : fires) {
            if(fire.getCoordinate().getDistance(this.position) < 0.01) {
                fire.extinguish();
            }   
        }
    }

}
