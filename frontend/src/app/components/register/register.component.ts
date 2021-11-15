import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../services/auth/auth.service";
import {Router} from "@angular/router";


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  username = '';
  password = '';
  repeatPassword = '';
  responseMessage = '';
  dialogVisible = false;

  constructor(private authService: AuthService,
              private router: Router
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
      this.responseMessage = response.body
      if(response.status == 200) {
          await this.router.navigate(['/stock-list'])
      }
    } else {
      this.responseMessage = 'Check your inputs!'
    }


    this.dialogVisible = true;
    location.reload()
  }
}
