import { Component } from '@angular/core';
import {FavouritesService} from "../favourites.service";

@Component({
  selector: 'app-favourites',
  templateUrl: './favourites.component.html',
  styleUrls: ['./favourites.component.css']
})
export class FavouritesComponent {
  items = this.favouritesService.getItems();

  constructor(
    private favouritesService: FavouritesService,
  ) {}

  delete(): void {
    this.items = this.favouritesService.clearFavourites();
    console.warn('Your favorites list has been cleared');
  }
}
