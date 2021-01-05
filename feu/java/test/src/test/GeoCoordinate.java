package test;

public class GeoCoordinate {
    public double lon;
    public double lat;

    final double[] centerCoordinate = { 45.75712817735117, 4.845404902039024 };
    final double[] centerScale = { 0.03856182704762, 0.06625824299175 };

    public GeoCoordinate(double lon, double lat) {
        this.lon = lon;
        this.lat = lat;
    }

    public GeoCoordinate(Coordinate coordinate) {
        this.lon = coordinate.x * centerScale[1] + centerCoordinate[1];
        this.lat = coordinate.y * centerScale[0] + centerCoordinate[0];
    }
}
