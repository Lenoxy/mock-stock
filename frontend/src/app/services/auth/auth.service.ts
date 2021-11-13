import {HttpClient} from "@angular/common/http";
import {environment} from "../../../environments/environment";
import {Injectable} from "@angular/core";
import {Observable, Subscription} from "rxjs";


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
   private http: HttpClient,
  ) {}

  public async register(username: string, password: string) : Promise<void> {
    let response

      response = await this.http.post(environment.host + "auth/register", {
        username,
        password
      }, {responseType: 'text', withCredentials: true}).toPromise()

    console.log(response)


  }

}
