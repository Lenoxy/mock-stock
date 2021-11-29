import {HttpClient, HttpResponse} from "@angular/common/http";
import {environment} from "../../../environments/environment";
import {Injectable} from "@angular/core";


@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(
    private http: HttpClient,
  ) {
  }

  public async me(): Promise<HttpResponse<any>> {
    return await this.http.get(environment.host + "me",
      {responseType: 'text', withCredentials: true, observe: "response"}).toPromise();
  }


}
