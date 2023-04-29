import {Component, Input, OnInit} from '@angular/core';
import {Commentary} from "../commentary";
import {ActivatedRoute} from "@angular/router";
import {VoucherService} from "../voucher.service";
import {Location} from '@angular/common';
import {FavouritesService} from "../favourites.service";
import {Voucher} from "../vouchers";
import {AppComponent} from "../app.component";

@Component({
  selector: 'app-voucher-detail',
  templateUrl: './voucher-detail.component.html',
  styleUrls: ['./voucher-detail.component.css']
})
export class VoucherDetailComponent implements OnInit {
  voucher: any;
  comments: Commentary[] = [];
  @Input() isLiked = false;
  @Input() favourites = false;
  addClick = false;
  updateClick = false;
  descriptionText = '';
  updatedDescription = '';
  id = 0;
  currentUserName = localStorage.getItem('username');

  constructor(
    private route: ActivatedRoute,
    private voucherService: VoucherService,
    private location: Location,
    private favouritesService: FavouritesService,
  ) {

  }

  ngOnInit(): void {
    this.getVoucher();

    const token = localStorage.getItem('token');
    if (token) {
      AppComponent.isLogged = true;
    }
  }
  get isLogged(): boolean {
    return AppComponent.isLogged;
  }
  getVoucher(): void {
    this.route.paramMap.subscribe((params) => {
      const id = params.get('id');
      if (id !== null) {
        this.voucherService.getVoucherDetail(id).subscribe((data) => {
          this.voucher = data;
        });
        this.voucherService.getComments(id).subscribe((data) => {
          console.log(data);
          this.comments = data;
        });
      }
    });
  }


  goBack(): void {
    this.location.back();
  }

  onClick(): void {
    if (!this.isLiked) {
      this.voucher.like += 1;
      this.isLiked = true;
    } else {
      this.voucher.like -= 1;
      this.isLiked = false;
    }

  }

  editButton(id: number): void {
    this.id = id;
    this.updateClick = true;
  }

  newComment(): void {
    if (!this.descriptionText) {
      this.addClick = false;
      return;
    }
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      const comment = new Commentary(this.currentUserName as string, id, this.descriptionText);
      this.voucherService.createComment(id, comment).subscribe((comment) => {
        this.getVoucher();
        this.addClick = false;
        this.descriptionText = '';
      });
    }
  }

  deleteButton(comment: Commentary): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.voucherService.deleteComment(id, comment.id).subscribe(() => {
        this.getVoucher();
      });
    }
  }

  updateButton(comment: Commentary): void {
    if (!this.updatedDescription) {
      this.updateClick = false;
      return;
    }
    comment.description = this.updatedDescription;
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.voucherService.updateComment(id, comment).subscribe(() => {
        this.updateClick = false;
        this.updatedDescription = '';
        this.getVoucher();
      });
    }
  }

  share(voucher: { name: any; }): void {
    window.alert(`The voucher ${this.voucher.name} has been shared!`);
    window.open(`https://t.me/share/url?url=http://localhost:4200/vouchers/${this.voucher.id}&text=Watch this voucher ${voucher.name} on the Journey Journal.`);
  }

  addToFavourites(voucher: Voucher) {
    this.favouritesService.addToFavourites(voucher).subscribe(() => {
      window.alert('Your product has been added to favourites!');
      this.favourites = true;
    }, error => {
      console.log('Error:', error);
      window.alert('Failed to add the product to favourites!');
    });
  }

}
