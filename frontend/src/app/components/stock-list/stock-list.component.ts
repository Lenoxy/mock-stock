import { Component, OnInit } from '@angular/core';
import {StockService} from '../../services/stock/stock.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-stock-list',
  templateUrl: './stock-list.component.html',
  styleUrls: ['./stock-list.component.scss']
})
export class StockListComponent implements OnInit {

  constructor(private stockService: StockService, private router: Router) { }

  stocks: any;
  displayedColumns: string[] = ['id', 'name', 'change', 'value'];

  async ngOnInit() {
    this.stocks = await this.stockService.getStockList(0, 20);
    console.log(this.stocks)
  }


  onRowClick(row: any) {
    console.log(row.id)
    this.router.navigateByUrl('stock-detail/' + row.id)
  }
}
