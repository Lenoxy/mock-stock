import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../services/auth/auth.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-auth-button',
  templateUrl: './auth-button.component.html',
  styleUrls: ['./auth-button.component.scss']
})
export class AuthButtonComponent implements OnInit {

  constructor(private authService: AuthService,
              private router: Router) { }
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
    localStorage.clear();
    await location.reload();
  }

  async redirectToLogin() {
    await this.router.navigate(['/login'])
  }
}
