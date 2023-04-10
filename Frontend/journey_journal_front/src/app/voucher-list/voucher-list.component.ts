import { Component, OnInit } from '@angular/core';
import { Voucher } from '../vouchers';
import { VoucherService } from '../voucher.service';

@Component({
  selector: 'app-voucher-list',
  templateUrl: './voucher-list.component.html',
  styleUrls: ['./voucher-list.component.css']
})

export class VoucherListComponent implements OnInit {
  vouchers: Voucher[] = [];
  searchText: any = '';

  constructor(private voucherService: VoucherService) { }

  ngOnInit(): void {
    this.voucherService.getVouchers().subscribe(
      vouchers => {
        this.vouchers = vouchers;
      },
      error => {
        console.log(error);
      }
    );
  }

}
