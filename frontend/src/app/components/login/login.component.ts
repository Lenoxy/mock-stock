import {Component, OnInit} from '@angular/core';
import {AuthService} from "../../services/auth/auth.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  username = ''
  password = ''
  dialogVisible = false;
  responseMessage = 'Check your inputs!'


  constructor(private auth: AuthService,
              private router: Router) {
  }

  ngOnInit(): void {
  }

  async login() {
    try {
      await this.auth.login(this.username, this.password);
        await this.router.navigate(['/stock-list'])
        location.reload()
    } catch {
      this.dialogVisible = true;
    }

  }

  async redirectToRegister() {
    await this.router.navigate(['/register'])
  }
}
