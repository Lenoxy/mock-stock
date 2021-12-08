import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {UserService} from "../../services/user/user.service";

@Component({
  selector: 'app-leaderboard',
  templateUrl: './leaderboard.component.html',
  styleUrls: ['./leaderboard.component.scss']
})
export class LeaderboardComponent implements OnInit {

  constructor(private userService: UserService, private router: Router) { }

  leaderboard: any;
  displayedColumns: string[] = ['username', 'score', 'moneyInStocks'];


  async ngOnInit() {
    this.leaderboard = JSON.parse((await this.userService.getLeaderboard()).body);
  }

  async onRowClick(user: any) {
    await this.router.navigateByUrl('user/' + user.username)
  }
}
