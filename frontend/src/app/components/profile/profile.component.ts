import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {UserService} from "../../services/user/user.service";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  constructor(private route: ActivatedRoute, private userService: UserService) {
  }

  // If profile is undefined, the user is on his own page.
  private profile: string | undefined

  data: any
  basicData: any
  basicOptions: any

  async ngOnInit() {
    this.profile = this.route.snapshot.paramMap.get('id')!;
    if (this.profile) {
      this.data = JSON.parse((await this.userService.getProfile(this.profile)).body);
      this.data.username = "User " + this.data.username;
    } else {
      this.data = JSON.parse((await this.userService.getOwnUser()).body)
    }

    this.basicData = {
      labels: [],
      datasets: [
        {
          label: "History",
          data: [],
          fill: false,
          borderColor: '#B22222',
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

}
