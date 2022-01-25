import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'geolocation_example';
  name = 'Angular';
  public lat: any;
  public lng: any;

  public ngOnInit(): void {
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
    console.log(crd.latitude);
    this.lat = crd.latitude;
    this.lng = crd.longitude;
  }

  error(err: any) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
  }

  getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        this.success,
        this.error,
        this.options
      );
    } else {
      alert('Geolocation is not supported by this browser.');
    }
  }
}
