import { Injectable } from '@angular/core';
import { Geolocation } from '../models/geolocation.model';

@Injectable({
  providedIn: 'root',
})
export class GeolocationService {
  constructor() {}

  public stuffShit: Geolocation = new Geolocation();

  options: any = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0,
  };

  success(pos: any): Geolocation {
    let crd = pos.coords;
    let thisGeolocation: Geolocation = new Geolocation();

    console.log('Your current position is:');
    console.log(`Latitude : ${crd.latitude}`);
    console.log(`Longitude: ${crd.longitude}`);
    console.log(`More or less ${crd.accuracy} meters.`);
    console.log('SAATTTTTTTTTTT');
    console.log(typeof crd.longitude);
    thisGeolocation.setLatitude = crd.latitude;
    thisGeolocation.setLongitude = crd.longitude;
    console.log('SAATTTTTTTTTTT 2');
    this.stuffShit.setLatitude = crd.latitude;
    this.stuffShit.setLongitude = crd.longitude;
    console.log('SAATTTTTTTTTTT 3');
    return thisGeolocation;
  }

  error(err: any) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
    return new Geolocation();
  }

  public getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        this.success,
        this.error,
        this.options
      );
      return this.stuffShit;
    } else {
      alert('Geolocation is not supported by this browser.');
      return new Geolocation();
    }
  }
}
