import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../services/auth/auth.service";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  username = '';
  password = '';
  repeatPassword = '';

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
  }

 async isPasswordMatch(): Promise<boolean> {
    return this.password === this.repeatPassword;
  }

  async register(): Promise<void> {
    if(await this.isPasswordMatch()) {
      await this.authService.register(this.username, this.password);
    } else {
      console.log("false")
    }
  }
}
