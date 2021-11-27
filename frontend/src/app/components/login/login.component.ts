import {Component, OnInit} from '@angular/core';
import {AuthService} from "../../services/auth/auth.service";
import {Router} from "@angular/router";
import {MatSnackBar} from '@angular/material/snack-bar';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  username = ''
  password = ''


  constructor(private auth: AuthService,
              private router: Router,
              private snackBar: MatSnackBar) {
  }

  ngOnInit(): void {
  }

  async login() {
    try {
      await this.auth.login(this.username, this.password);
        await this.router.navigate(['/stock-list'])
        location.reload()
    } catch {
      this.snackBar.open("Check your inputs!")
    }

  }

  async redirectToRegister() {
    await this.router.navigate(['/register'])
  }
}
