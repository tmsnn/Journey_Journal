import { Component } from '@angular/core';
import {FavouritesService} from "../favourites.service";
import {Favorite} from "../favorites";
import {Voucher} from "../vouchers";
import {VoucherService} from "../voucher.service";
@Component({
  selector: 'app-favourites',
  templateUrl: './favourites.component.html',
  styleUrls: ['./favourites.component.css']
})
export class FavouritesComponent {
  favorites: Favorite[] = [];
  vouchers: Voucher[] = [];
  searchText: any = '';
  constructor(
    private favoriteService: FavouritesService,
    private voucherService: VoucherService,
  ) {}
  ngOnInit() {
    this.favoriteService.getFavoritesByUser().subscribe((data: Favorite[]) => {
      this.favorites = data;
      this.favorites.forEach((favorite) => {
        this.voucherService.getVoucherDetail(favorite.voucher).subscribe((data: Voucher) => {
          this.vouchers.push(data);
        });
      });
    });

  }
  deleteButton(id:number){

      this.favoriteService.deleteFavorite(id).subscribe(() => {
        window.alert('Your product has been deleted from favourites!');
      }, error => {
        console.log('Error:', error);
        window.alert('Failed to delete the voucher from favourites!');
      });

  }
}
