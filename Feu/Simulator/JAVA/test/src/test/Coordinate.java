package test;

public class Coordinate {
    public double x;
    public double y;

    public Coordinate(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public Coordinate(GeoCoordinate coordinate) {
        this.x = (coordinate.lon  - GeoCoordinate.centerCoordinate[1]) / GeoCoordinate.centerScale[1];
        this.y = (coordinate.lat - GeoCoordinate.centerCoordinate[0]) / GeoCoordinate.centerScale[0];
    }

	public Double getDistance(Coordinate position) {

		return Math.sqrt(Math.pow(position.x - this.x, 2.0) + Math.pow(position.y - this.y, 2.0));
    }
    
    public String toString() {
        GeoCoordinate geo = new GeoCoordinate(this);
        
        return geo.lon + "," + geo.lat;
    }
}
