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
  public location?: Promise<void | Geolocation>;

  constructor(private geolocationService: GeolocationService) {
    this.location = new GeolocationService().getLocation();
  }

  public ngOnInit(): void {}
}
