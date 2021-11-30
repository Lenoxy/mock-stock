import {Injectable} from "@angular/core";
import {HttpClient, HttpResponse} from "@angular/common/http";
import {environment} from "../../../environments/environment";


@Injectable({
  providedIn: 'root'
})
export class StockService {

  constructor(private http: HttpClient) {
  }

  public async getStock(id: string): Promise<HttpResponse<any>> {
    return await this.http.get(environment.host + 'stocks/' + id,
      {responseType: 'text', observe: "response"}).toPromise();
  }

  public async getStockList(skip: number, top: number): Promise<HttpResponse<any>>{
    return JSON.parse(<string>(await this.http.get(environment.host + 'stocks?skip=' + skip + '&top=' + top,
      {responseType: 'text', observe: "response"}).toPromise()).body);
  }
}
