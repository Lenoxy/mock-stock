import { Component, OnInit } from '@angular/core';
import {StockService} from "../../services/stock/stock.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-sell',
  templateUrl: './sell.component.html',
  styleUrls: ['./sell.component.scss']
})
export class SellComponent implements OnInit {

  id = ''
  constructor(private stockService: StockService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.id = this.route.snapshot.paramMap.get('id')!;
  }


  async sellStock(): Promise<void> {
    await this.stockService.sellStock(this.id)
    location.reload()
  }
}
