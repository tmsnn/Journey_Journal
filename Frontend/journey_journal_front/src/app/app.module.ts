import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {RouterModule} from "@angular/router";
import {FormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {AppComponent} from './app.component';
import {VoucherListComponent} from './voucher-list/voucher-list.component';
import {TopBarComponent} from './top-bar/top-bar.component';
import {VoucherFilterComponent} from './voucher-filter/voucher-filter.component';
import {VoucherDetailComponent} from './voucher-detail/voucher-detail.component';
import {CategoryComponent} from './category/category.component';
import {LoginComponent} from './login/login.component';
import {RegisterComponent} from './register/register.component';
import {FilterPipe} from './voucher-list/pipes';
import { ReactiveFormsModule } from '@angular/forms';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { FavouritesComponent } from './favourites/favourites.component';

@NgModule({
  declarations: [
    AppComponent,
    VoucherListComponent,
    VoucherDetailComponent,
    CategoryComponent,
    VoucherFilterComponent,
    RegisterComponent,
    LoginComponent,
    FilterPipe,
    TopBarComponent,
    FavouritesComponent,

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    FontAwesomeModule,
    RouterModule.forRoot([
      {path: '', component: VoucherListComponent},
      {path: 'vouchers', component: VoucherListComponent},
      {path: 'vouchers/:id', component: VoucherDetailComponent},
      {path: 'categories/:id', component: CategoryComponent},
      {path: 'login', component: LoginComponent},
      {path: 'register', component: RegisterComponent},
      {path: 'favourite', component: FavouritesComponent},
    ]),
  ],
  providers: [
    HttpClientModule,
  ],
  exports: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
