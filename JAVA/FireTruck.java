import java.util.List;

public class FireTruck {
    
    private Coordinate position;

    public int status;

    public int id;

    public int fire_id;

    private Coordinate destination;

    public FireTruck(GeoCoordinate coordinate, int status, int id){
        this.status = status;
        this.position = new Coordinate(coordinate);
        this.id = id;
    }

	public void assignFire(List<Fire> fires) {
        Double priority = 0.0;
        Double prio = 0.0;
        for(Fire fire : fires) {
            prio = fire.getIntensity() * (1 / fire.getCoordinate().getDistance(this.position));
            if(prio > priority) {
                priority = prio;
                this.fire_id = fire.getId();
                this.status = 1;
            }
        }
	}

    public String toString() {
        return "{\"id\":"+this.id+",\"statut\":"+this.status+",\"fire_id\":"+this.fire_id+"}";
    }

}
