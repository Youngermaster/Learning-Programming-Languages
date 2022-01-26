import { Component } from '@angular/core';
import { Geolocation } from './models/geolocation.model';
import { GeolocationService } from './services/geolocation.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'geolocation_example';
  name = 'Angular';
  public location?: Geolocation;

  constructor() {}

  public ngOnInit(): void {
    this.obtainLocation();
  }

  public obtainLocation() {
    this.location = new GeolocationService().getLocation();
    console.log('Obtaining...');
  }
}
