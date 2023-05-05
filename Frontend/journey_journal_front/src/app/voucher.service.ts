import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Voucher} from './vouchers';
import {Commentary} from "./commentary";

@Injectable({
  providedIn: 'root'
})
export class VoucherService {
  constructor(private client: HttpClient) {
  }


  BASE_URL = 'http://127.0.0.1:8000';

  getVouchers(): Observable<Voucher[]> {
    return this.client.get<Voucher[]>(`${this.BASE_URL}/vouchers/`);
  }

  getVoucherDetail(id: any): Observable<Voucher> {
    return this.client.get<Voucher>(`${this.BASE_URL}/vouchers/${id}/`);
  }

  getVoucherByCategoryId(id: any): Observable<Voucher[]> {
    return this.client.get<Voucher[]>(`${this.BASE_URL}/categories/${id}/`);
  }

  getComments(id: string): Observable<Commentary[]> {
    return this.client.get<Commentary[]>(`${this.BASE_URL}/vouchers/${id}/comments/`);
  }

  createComment(id: number, comment: Commentary): Observable<any> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      })
    };
    return this.client.post(`${this.BASE_URL}/vouchers/${id}/comments/`, comment, httpOptions);
  }

  updateComment(id: string, comment: Commentary): Observable<any> {
    return this.client.put(`${this.BASE_URL}/vouchers/${id}/comments/${comment.id}/`, comment);
  }

  deleteComment(id: string, commentId: number): Observable<any> {
    return this.client.delete(`${this.BASE_URL}/vouchers/${id}/comments/${commentId}/`);
  }
}
