import {Injectable} from "@angular/core";
import {HttpClient, HttpResponse} from "@angular/common/http";
import {environment} from "../../../environments/environment";


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) {
  }

  public async getOwnUser(): Promise<HttpResponse<any>> {
    return await this.http.get(environment.host + 'me',
      {responseType: 'text', withCredentials: true, observe: "response"}).toPromise()
  }

  public async getLeaderboard(): Promise<HttpResponse<any>> {
    return await this.http.get(environment.host + "users" ,
      {responseType: 'text', withCredentials: true, observe: "response"}).toPromise();
  }

  public async getProfile(username: string): Promise<HttpResponse<any>> {
    return await this.http.get(environment.host + "users/" + username ,
      {responseType: 'text', withCredentials: true, observe: "response"}).toPromise();
  }
}
