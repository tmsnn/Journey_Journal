import {Component, OnInit} from '@angular/core';
import {Category} from "../categories";
import {CategoryService} from "../category.service";

@Component({
  selector: 'app-voucher-filter',
  templateUrl: './voucher-filter.component.html',
  styleUrls: ['./voucher-filter.component.css']
})
export class VoucherFilterComponent implements OnInit {
  categories: Category[] = [];

  constructor(private categoriesService: CategoryService) {
  }

  ngOnInit(): void {
    this.getCategories();
  }

  getCategories(): void {
    this.categoriesService.getCategories().subscribe((data) => {
      console.log(data);
      this.categories = data;
    });
  }
}
