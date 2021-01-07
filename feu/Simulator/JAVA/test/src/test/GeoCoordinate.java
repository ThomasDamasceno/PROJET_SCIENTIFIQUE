package test;

public class GeoCoordinate {
    public double lon;
    public double lat;

    final double[] centerCoordinate = { 45.7571, 4.84540 };
    final double[] centerScale = { 0.0385, 0.06625 };

    public GeoCoordinate(double lon, double lat) {
        this.lon = lon;
        this.lat = lat;
    }

    public GeoCoordinate(Coordinate coordinate) {
        this.lon = coordinate.x * centerScale[1] + centerCoordinate[1];
        this.lat = coordinate.y * centerScale[0] + centerCoordinate[0];
    }
}
