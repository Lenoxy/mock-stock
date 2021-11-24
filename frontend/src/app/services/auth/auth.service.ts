import {HttpClient, HttpResponse} from "@angular/common/http";
import {environment} from "../../../environments/environment";
import {Injectable} from "@angular/core";


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http: HttpClient,
  ) {
  }

  public async register(username: string, password: string): Promise<HttpResponse<any>> {

    return await this.http.post(environment.host + "auth/register", {
      username,
      password
    }, {responseType: 'text', withCredentials: true, observe: "response"}).toPromise();
  }


  public async logout(): Promise<HttpResponse<any>> {
    return await this.http.post(environment.host + "auth/logout", {}, {
      responseType: 'text',
      withCredentials: true,
      observe: "response"
    }).toPromise()
  }

  public async isLoggedin(): Promise<HttpResponse<any>> {
    return await this.http.get(environment.host + 'auth/isloggedin',{responseType: 'text',
      withCredentials: true,
      observe: "response"}).toPromise()
  }

  public async login(username: string, password: string): Promise<HttpResponse<any>> {
    return await this.http.post(environment.host + 'auth/login',
      {username, password},
      {responseType: 'text', withCredentials: true, observe: "response"}).toPromise();
  }

}
