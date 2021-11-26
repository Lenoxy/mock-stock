import {Component, OnInit} from '@angular/core';
import {PrimeNGConfig} from "primeng/api";
import {MenuItem} from 'primeng/api';
import {AuthButtonComponent} from "./components/auth-button/auth-button.component";
import {AuthService} from "./services/auth/auth.service";
import {UserService} from "./services/user/user.service";


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'mockstock';
  menuItems: MenuItem[] = [{}];
  isLoggedIn= false;
  money = 0

  constructor(private primengConfig: PrimeNGConfig,
              private userService: UserService,
              private authService: AuthService) {}

  async ngOnInit() {
    this.isLoggedIn = await this.isAuthorized()
    await this.getUserMoney();
    this.primengConfig.ripple = true;

    this.menuItems = [
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

  async getUserMoney(): Promise<void> {
    if(await this.isAuthorized()) {
      let response = (await this.userService.getUserMoney()).body
      this.money = response.money_liquid;
      console.log(response.money_liquid)
      localStorage.setItem('money', this.money.toString())
    }
  }

  async isAuthorized(): Promise<boolean> {
    const authStatus = await this.authService.isLoggedin()
    return authStatus.body != 'False';
  }
}
