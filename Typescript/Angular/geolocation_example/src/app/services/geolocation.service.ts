import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class GeolocationService {
  private latitude: number;
  private longitude: number;

  constructor() {
    this.latitude = 0;
    this.longitude = 0;
    this.getLocation();
  }

  options: any = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0,
  };

  success(pos: any) {
    var crd = pos.coords;

    console.log('Your current position is:');
    console.log(`Latitude : ${crd.latitude}`);
    console.log(`Longitude: ${crd.longitude}`);
    console.log(`More or less ${crd.accuracy} meters.`);
    console.log('SAATTTTTTTTTTT');
    console.log(crd.longitude);
    console.log(typeof crd.longitude);
    console.log(crd.latitude);
    this.latitude = crd.latitude;
    this.longitude = crd.longitude;
    console.log('SAATTTTTTTTTTT');
  }

  error(err: any) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
  }

  async getLocation() {
    if (navigator.geolocation) {
      await navigator.geolocation.getCurrentPosition(
        this.success,
        this.error,
        this.options
      );
    } else {
      alert('Geolocation is not supported by this browser.');
    }
  }
}
