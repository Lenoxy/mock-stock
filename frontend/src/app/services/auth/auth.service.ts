import {HttpClient} from "@angular/common/http";
import {environment} from "../../../environments/environment";
import {Injectable} from "@angular/core";


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
   private http: HttpClient,

  ) {}

  public async register(username: string, password: string) : Promise<void> {
    let response
    try {
      response = await this.http.post(environment.host + "auth/register", {
        username,
        password
      })
      console.log(response);
    } catch {

    }
  }

}
