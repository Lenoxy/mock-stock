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
  loading = false; // Used only for loading next page, not initial loading
  displayedColumns: string[] = ['id', 'name', 'change', 'value'];
  private _page: any = 1;

  async ngOnInit() {
    this.route.queryParams
      .subscribe(params => {
          this.page = params.page;
        }
      );
    await this.loadTable()
  }

  async loadTable() {
    this.loading = true;
    this.stocks = await this.stockService.getStockList((this.page - 1) * 25, 24);
    this.loading = false;
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
    this.page++;
    await this.router.navigateByUrl('stock-list?page=' + this.page);
    await this.loadTable()
  }
}
