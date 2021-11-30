import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {ProfileService} from '../../services/profile/profile.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  constructor(private route: ActivatedRoute, private profileService: ProfileService) {
  }

  // If profile is undefined, the user is on his own page.
  private profile: string | undefined

  data: any

  async ngOnInit() {
    this.profile = this.route.snapshot.paramMap.get('id')!;
    console.log("Viewing: ", this.profile)

    this.data = JSON.parse((await this.profileService.me()).body)
    console.log(this.data)

  }

}
