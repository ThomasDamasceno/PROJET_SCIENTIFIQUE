public class Coordinate {
    public double x;
    public double y;

    public Coordinate(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public Coordinate(GeoCoordinate coordinate) {
        this.x = coordinate.lon / GeoCoordinate.centerScale[0] - GeoCoordinate.centerCoordinate[0];
        this.y = coordinate.lat / GeoCoordinate.centerScale[1] - GeoCoordinate.centerCoordinate[1];
    }

	public Double getDistance(Coordinate position) {

		return Math.sqrt(Math.pow(position.x - this.x, 2.0) + Math.pow(position.y - this.y, 2.0));
	}
}
