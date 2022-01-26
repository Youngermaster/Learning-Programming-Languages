import { Injectable } from '@angular/core';
import { Geolocation } from '../models/geolocation.model';

@Injectable({
  providedIn: 'root',
})
export class GeolocationService {
  constructor() {}

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
    thisGeolocation.latitude = crd.latitude;
    thisGeolocation.longitude = crd.longitude;
    console.log('SAATTTTTTTTTTT 2');
    return thisGeolocation;
  }

  error(err: any) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
    return new Geolocation();
  }

  public async getLocation() {
    if (navigator.geolocation) {
      return await navigator.geolocation.getCurrentPosition(
        this.success,
        this.error,
        this.options
      );
    } else {
      alert('Geolocation is not supported by this browser.');
      return new Geolocation();
    }
  }
}
