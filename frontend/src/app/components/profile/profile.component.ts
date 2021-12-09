import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {UserService} from "../../services/user/user.service";
import {AuthService} from "../../services/auth/auth.service";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  constructor(private route: ActivatedRoute, private userService: UserService, private router: Router, private authService: AuthService) {
  }

  // If profile is undefined, the user is on his own page.
  private profile: string | undefined

  data: any
  history: any
  basicData: any
  basicOptions: any
  isLoggedin: any
  loading = false; // Used only for loading next page, not initial loading
  displayedColumns: string[] = ['id', 'name', 'change', 'value', 'amount'];

  async ngOnInit() {
    this.isLoggedin = await this.isAuthorized()
    if(!this.isLoggedin) {
      await this.router.navigateByUrl('stock-list')
    }
    this.profile = this.route.snapshot.paramMap.get('id')!;
    if (this.profile) {
      this.data = JSON.parse((await this.userService.getProfile(this.profile)).body);
      this.data.username = "User " + this.data.username;
    } else {
      this.data = JSON.parse((await this.userService.getOwnUser()).body)
    }

    this.basicData = {
      labels: this.data.histories.keys,
      datasets: [
        {
          label: "Liquid Money",
          data: this.data.histories.liquid_money,
          fill: false,
          borderColor: '#B22222',
          tension: .1
        },
        {
          label: "Score",
          data: this.data.histories.score,
          fill: false,
          borderColor: '#550a8a',
          tension: .1
        },
        {
          label: "Stock Money",
          data: this.data.histories.stock_money,
          fill: false,
          borderColor: '#00ba00',
          tension: .1
        }
      ]
    }
  }

  updateOptions() {
    this.basicOptions = {
      plugins: {
        legend: {
          labels: {
            color: '#495057'
          }
        }
      },
      scales: {
        x: {
          ticks: {
            color: '#495057'
          },
          grid: {
            color: '#ebedef'
          }
        },
        y: {
          ticks: {
            color: '#495057'
          },
          grid: {
            color: '#ebedef'
          }
        }
      }
    };
  }

  async isAuthorized(): Promise<boolean> {
    const authStatus = await this.authService.isLoggedin()
    return authStatus.body != 'False';
  }

  async onRowClick(row: any) {
    await this.router.navigateByUrl('stock-detail/' + row.id)
  }

}
