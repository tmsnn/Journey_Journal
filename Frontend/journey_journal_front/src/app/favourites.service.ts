
import { Voucher} from "./vouchers";
import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import { Observable } from 'rxjs';
import {Favorite} from "./favorites";
import {HttpHeaders} from "@angular/common/http";

/* . . . */
@Injectable({
  providedIn: 'root'
})
export class FavouritesService {

  BASE_URL = 'http://localhost:8000';
  constructor(
    private client: HttpClient,

  ) {}


  getFavoritesByUser(): Observable<Favorite[]> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      })
    };

    return this.client.get<Favorite[]>(`${this.BASE_URL}/api/favorites/`, httpOptions);
  }

  addToFavourites(voucher: Voucher, userId: string): Observable<any> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      })
    };
    const newFavorite = { user: userId, voucher: voucher.id };
    return this.client.post(`${this.BASE_URL}/api/favorites/`, newFavorite, httpOptions);
  }


  deleteFavorite(id: number) {
    return this.client.delete<Favorite[]>(`${this.BASE_URL}/api/favorite/voucher/${id}/`);
  }





}
