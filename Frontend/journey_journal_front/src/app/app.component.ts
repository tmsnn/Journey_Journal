import {Component, OnInit} from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  static isLogged: boolean;
  static id: 0;
  constructor(public router: Router) {
    AppComponent.isLogged = false;
    AppComponent.id = 0;
  }
  title = 'journey_journal_front';

  ngOnInit(): void {
  }
}
