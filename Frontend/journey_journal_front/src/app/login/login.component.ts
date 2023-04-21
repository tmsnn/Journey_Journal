import {Component, OnInit} from '@angular/core';
import {Router} from "@angular/router";
import {LoginService} from "../login.service";
import {Location} from '@angular/common';
import {AppComponent} from "../app.component";
import {FormBuilder, FormGroup} from "@angular/forms";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  form !: FormGroup;

  constructor(private router: Router,
              private loginService: LoginService,
              private location: Location,
              private http: HttpClient,
              private formBuilder: FormBuilder,
  ) {
  }

  username = '';
  password = '';

  ngOnInit(): void {

    this.form = this.formBuilder.group({
      username: '',
      password: ''
    });
  }

  goBack(): void {
    this.location.back();
  }

  loginFunc(): void {
    this.http.post('http://localhost:8000/api/login', this.form.getRawValue(), {
      withCredentials: true
    }).subscribe(() => this.router.navigate(['/']));
    AppComponent.isLogged = true;
  }
}
