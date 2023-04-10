import {Component, OnInit} from '@angular/core';
import {Voucher} from "../vouchers";
import {Category} from "../categories";
import {ActivatedRoute, Router} from "@angular/router";
import {VoucherService} from "../voucher.service";
import {CategoryService} from "../category.service";

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  vouchers: Voucher[] = [];
  category: Category | undefined;
  searchText: any = '';

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private vouchersService: VoucherService,
    private categoriesService: CategoryService
  ) {
  }

  ngOnInit(): void {
    this.getCategory();
    this.getVouchers();
  }

  getVouchers(): void {
    this.route.paramMap.subscribe((params) => {
      const id = params.get('id');
      if (id !== null) {
        this.vouchersService.getVoucherByCategoryId(id).subscribe((data) => {
          this.vouchers = data;
          console.log(data);
        });
      }
    });
  }

  getCategory(): void {
    this.route.paramMap.subscribe((params) => {
      const id = params.get('id');
      if (id !== null) {
        this.categoriesService.getCategory(id).subscribe((data) => {
          this.category = data;
          console.log(data);
        });
      }
    });
  }
}
