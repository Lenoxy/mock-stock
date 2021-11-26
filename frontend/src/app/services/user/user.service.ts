import {Injectable} from "@angular/core";
import {HttpClient, HttpResponse} from "@angular/common/http";
import {environment} from "../../../environments/environment";


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) {
  }

  async getUserMoney(): Promise<HttpResponse<any>> {
    return await this.http.get(environment.host + 'me',
      {withCredentials: true, observe: "response"}).toPromise()
  }
}
