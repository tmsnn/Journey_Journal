import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {RouterModule} from "@angular/router";
import {FormsModule} from "@angular/forms";
import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {AppComponent} from './app.component';
import {VoucherListComponent} from './voucher-list/voucher-list.component';
import {TopBarComponent} from './top-bar/top-bar.component';
import {VoucherFilterComponent} from './voucher-filter/voucher-filter.component';
import {VoucherDetailComponent} from './voucher-detail/voucher-detail.component';
import {CategoryComponent} from './category/category.component';
import {LoginComponent} from './login/login.component';
import {AuthInterceptor} from "./AuthInterceptor";
import {RegisterComponent} from './register/register.component';
import {FilterPipe} from './voucher-list/pipes';
import { ReactiveFormsModule } from '@angular/forms';


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

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      {path: '', component: VoucherListComponent},
      {path: 'vouchers', component: VoucherListComponent},
      {path: 'vouchers/:id', component: VoucherDetailComponent},
      {path: 'categories/:id', component: CategoryComponent},
      {path: 'login', component: LoginComponent},
      {path: 'register', component: RegisterComponent},
    ]),
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    },
    HttpClientModule,
  ],
  exports: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
