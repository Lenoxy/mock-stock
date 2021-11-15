import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../services/auth/auth.service";

@Component({
  selector: 'app-logout-button',
  templateUrl: './logout-button.component.html',
  styleUrls: ['./logout-button.component.scss']
})
export class LogoutButtonComponent implements OnInit {

  constructor(private authService: AuthService) { }
  isloggedIn = false
  async ngOnInit():Promise<void> {
    this.isloggedIn = await this.isAuthorized()
  }

  async isAuthorized(): Promise<boolean> {
    const authStatus = await this.authService.isLoggedin()
    return authStatus.body != 'False';
  }

  async logout(): Promise<void> {
    await this.authService.logout();
    await location.reload();
  }
}
