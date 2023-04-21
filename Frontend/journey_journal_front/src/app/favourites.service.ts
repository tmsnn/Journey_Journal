
import { Voucher} from "./vouchers";
import { Injectable } from '@angular/core';
/* . . . */
@Injectable({
  providedIn: 'root'
})
export class FavouritesService {
  items: Voucher[] = [];
  constructor(
  ) {}



  addToFavourites(voucher: Voucher) {
    if (!(this.items.some(v => v.id === voucher.id ))) {
      this.items.push(voucher);
    }
  }

  getItems() {
    return this.items;
  }

  clearFavourites() {
    this.items = [];
    return this.items;
  }
}
