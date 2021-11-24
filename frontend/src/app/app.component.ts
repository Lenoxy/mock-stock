import {Component, OnInit} from '@angular/core';
import {PrimeNGConfig} from "primeng/api";
import {MenuItem} from 'primeng/api';
import {AuthButtonComponent} from "./components/auth-button/auth-button.component";
import {AuthService} from "./services/auth/auth.service";


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'mockstock';
  menuItems: MenuItem[] = [{}];
  isLoggedIn= false;

  constructor(private primengConfig: PrimeNGConfig) {}

  async ngOnInit() {
    this.primengConfig.ripple = true;

    this.menuItems= [
      {
        label: 'Stocks',
        icon: 'pi pi-fw pi-file',
      },
      {
        label:'Leaderboard',
        icon:'pi pi-fw pi-pencil',
      },
      {
        label:'Profile',
        icon:'pi pi-fw pi-user',
      }
    ];
  }



}
