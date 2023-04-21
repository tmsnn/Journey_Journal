import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {VoucherListComponent} from "./voucher-list/voucher-list.component";
import {VoucherDetailComponent} from "./voucher-detail/voucher-detail.component";
import {CategoryComponent} from "./category/category.component";
import {RegisterComponent} from "./register/register.component";
import {LoginComponent} from "./login/login.component";
import {FavouritesComponent} from "./favourites/favourites.component";

const routes: Routes = [
  {path: '', redirectTo: '/vouchers', pathMatch: 'full', component: VoucherListComponent},
  {path: 'vouchers/:id', component: VoucherDetailComponent},
  {path: 'categories/:id', component: CategoryComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'login', component: LoginComponent},
  {path: 'favourite', component: FavouritesComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
