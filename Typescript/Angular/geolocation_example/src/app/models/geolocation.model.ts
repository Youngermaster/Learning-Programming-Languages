export class Geolocation {
  private latitude?: number;
  private longitude?: number;

  Geolocation(lat: number, lng: number) {
    this.latitude = lat;
    this.longitude = lng;
  }

  public get getLatitude(): number {
    if (this.latitude != null) {
      return this.latitude;
    }
    return 0;
  }

  public get getLongitude(): number {
    if (this.longitude != null) {
      return this.longitude;
    }
    return 0;
  }

  public set setLatitude(lat: number) {
    this.latitude = lat;
  }

  public set setLongitude(lng: number) {
    this.longitude = lng;
  }
}
