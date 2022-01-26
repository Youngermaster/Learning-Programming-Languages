import { Component } from '@angular/core';
import { GeolocationService } from './services/geolocation.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'geolocation_example';
  name = 'Angular';
  public lat: number;
  public lng: number;

  constructor(private geolocationService: GeolocationService) {
    this.lat = 0;
    this.lng = 0;
    this.getLocation();
  }

  public ngOnInit(): void {
    this.getLocation();
  }
}
