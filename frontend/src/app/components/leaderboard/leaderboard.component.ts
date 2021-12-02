import { Component, OnInit } from '@angular/core';
import {ProfileService} from '../../services/profile/profile.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-leaderboard',
  templateUrl: './leaderboard.component.html',
  styleUrls: ['./leaderboard.component.scss']
})
export class LeaderboardComponent implements OnInit {

  constructor(private profileService: ProfileService, private router: Router) { }

  leaderboard: any;
  displayedColumns: string[] = ['username', 'score', 'moneyInStocks'];


  async ngOnInit() {
    this.leaderboard = JSON.parse((await this.profileService.leaderboard()).body);
    console.log(this.leaderboard)

  }

  async onRowClick(user: any) {
    await this.router.navigateByUrl('user/' + user.username)
  }
}
