
import { Voucher} from "./vouchers";
import { Injectable } from '@angular/core';
import {AppComponent} from "./app.component";
import {HttpClient} from "@angular/common/http";
import { switchMap } from 'rxjs/operators';
import { Observable } from 'rxjs';
import {Favorite} from "./favorites";
import { map } from 'rxjs/operators';
/* . . . */
@Injectable({
  providedIn: 'root'
})
export class FavouritesService {
  private id: number = 0;
  BASE_URL = 'http://localhost:8000';
  constructor(
    private client: HttpClient,

  ) {}


  getFavoritesByUser(): Observable<Favorite[]> {
    return this.client.get<Favorite[]>(`${this.BASE_URL}/api/favorites/${this.getId()}/`);
  }
  addToFavourites(voucher: Voucher): Observable<any> {
    const newFavorite = { user: this.getId(), voucher: voucher.id };
    return this.client.post(`${this.BASE_URL}/api/favorites/`, newFavorite);
  }

  deleteFavorite(id: number) {
    return this.client.delete<Favorite[]>(`${this.BASE_URL}/api/favorite/voucher/${id}/`);
  }


  setId(id: number): void {
    this.id = id;
  }

  getId(): number {
    return this.id;
  }


}
