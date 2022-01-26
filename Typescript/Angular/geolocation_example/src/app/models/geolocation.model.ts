export class Geolocation {
  latitude?: number;
  longitude?: number;

  Geolocation(lat: number, lng: number) {
    this.latitude = lat;
    this.longitude = lng;
  }
}
