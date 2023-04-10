import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Category} from './categories';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {
  constructor(private client: HttpClient) {
  }

  BASE_URL = 'http://localhost:8000';

  getCategory(id: any): Observable<Category> {
    return this.client.get<Category>(`${this.BASE_URL}/categories/${id}/`);
  }

  getCategories(): Observable<Category[]> {
    return this.client.get<Category[]>(`${this.BASE_URL}/categories/`);
  }

}
