import java.util.Random;

public class Fire {
    
    /** Attributes */

    private int id;

    private int intensity;

    private Coordinate position;

    private Random rand = new Random();

    /** Public methods */

    public Fire(Coordinate pos) {
        this.position = pos;
        this.intensity = rand.nextInt(50);
    }

    public Fire(GeoCoordinate pos, int intensite, int id) {
        this.position = new Coordinate(pos);
        this.intensity = intensite;
        this.id = id;
    }

    public Fire() {
        this.position = randomPos(new Coordinate(0,0), 1);
        this.intensity = rand.nextInt(50);
    }

    public Fire spread() {

        Fire ret = null;

        if (intensity < 255) {
            this.intensity += this.rand.nextInt(3);
        } else {
            if(this.rand.nextDouble() <= 0.1/100)
                ret = new Fire(randomPos(this.position, 0.1));
        }

        return ret;
    }

    /**Private methods */

    private Coordinate randomPos(Coordinate center, double radius) {
        rand = new Random();

        double t = 2*Math.PI*rand.nextDouble();
        double u = rand.nextDouble()+rand.nextDouble();
        double r = (u>1 ? 2-u : u) * radius;

        return new Coordinate(r*Math.cos(t) + center.x, r*Math.sin(t) + center.y);
    }

    public Coordinate getCoordinate() {
        return this.position;
    }

    public String toString() {
        GeoCoordinate geo = new GeoCoordinate(this.position);
        return "{\"lo\":\"" + geo.lon +"\",\"la\":\"" + geo.lat + "\",\"in\":\"" + this.intensity + "\"}";
    }

	public int getIntensity() {
		return this.intensity;
	}

	public int getId() {
		return this.id;
	}

}
