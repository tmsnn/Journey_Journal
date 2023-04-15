import { Component, OnInit } from '@angular/core';
import { Voucher } from '../vouchers';
import { VoucherService } from '../voucher.service';
import {HttpClient, HttpResponse} from "@angular/common/http";

@Component({
  selector: 'app-voucher-list',
  templateUrl: './voucher-list.component.html',
  styleUrls: ['./voucher-list.component.css']
})

export class VoucherListComponent implements OnInit {
  vouchers: Voucher[] = [];
  searchText: any = '';
  message = ''

  constructor(
    private voucherService: VoucherService,
    private http: HttpClient
  ) { }

  ngOnInit(): void {
    this.voucherService.getVouchers().subscribe(
      vouchers => {
        this.vouchers = vouchers;
      },
      error => {
        console.log(error);
      }
    );
    this.http.get('http://localhost:8080/api/user', {withCredentials: true}).subscribe(
      (res: any) => {
        this.message = `Hello, traveler!`
      },
      err => {
        this.message = 'You are not logged in';
      }
    );
  }

}
