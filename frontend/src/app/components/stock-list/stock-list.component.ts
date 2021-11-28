import {Component, OnInit} from '@angular/core';
import {StockService} from '../../services/stock/stock.service';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-stock-list',
  templateUrl: './stock-list.component.html',
  styleUrls: ['./stock-list.component.scss']
})
export class StockListComponent implements OnInit {
  get page(): any {
    return this._page;
  }

  set page(value: any) {
    value > 1 ? this._page = value : this._page = 1;
  }

  constructor(private stockService: StockService, private router: Router, private route: ActivatedRoute) {
  }

  stocks: any;
  displayedColumns: string[] = ['id', 'name', 'change', 'value'];
  private _page: any = 1;

  async ngOnInit() {
    this.page = this.route.snapshot.paramMap.get('page') ? this.route.snapshot.paramMap.get('page') : 1;
    await this.loadTable()
  }

  async loadTable() {
    console.log((this.page - 1) * 25, ((this.page - 1) * 25) + 25)
    console.log("page is", this.page)
    this.stocks = await this.stockService.getStockList((this.page - 1) * 25, ((this.page - 1) * 25) + 24);
    console.log(this.stocks)
  }


  async onRowClick(row: any) {
    await this.router.navigateByUrl('stock-detail/' + row.id)
  }

  async gotoPrevious() {
    this.page--;
    await this.router.navigateByUrl('stock-list?page=' + this.page);
    await this.loadTable()
  }

  async gotoNext() {
    console.log(this.page)
    this.page++;
    await this.router.navigateByUrl('stock-list?page=' + this.page);
    await this.loadTable()
  }
}
