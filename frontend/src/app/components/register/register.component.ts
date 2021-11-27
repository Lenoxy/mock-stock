import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../services/auth/auth.service";
import {Router} from "@angular/router";
import {MatSnackBar} from '@angular/material/snack-bar';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  username = '';
  password = '';
  repeatPassword = '';

  constructor(private authService: AuthService,
              private router: Router,
              private snackBar: MatSnackBar
  ) { }

  ngOnInit(): void {
  }

 async isPasswordMatch(): Promise<boolean> {
    return this.password.trim() === this.repeatPassword.trim()
      && this.password.trim() != null && this.password.length >= 8;
  }

  async register(): Promise<void> {
    if(await this.isPasswordMatch()) {
      const response = await this.authService.register(this.username, this.password);
      if(response.status == 200) {
          await this.router.navigate(['/stock-list'])
          location.reload();
      }
    } else {
      this.snackBar.open("Your credentials are invalid")
    }

  }
}
