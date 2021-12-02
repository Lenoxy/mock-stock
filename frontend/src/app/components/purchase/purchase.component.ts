import { Component, OnInit } from '@angular/core';
import {StockService} from "../../services/stock/stock.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-purchase',
  templateUrl: './purchase.component.html',
  styleUrls: ['./purchase.component.scss']
})
export class PurchaseComponent implements OnInit {

  id = ''

  constructor(private stockService: StockService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.id = this.route.snapshot.paramMap.get('id')!;
  }

  async buyStock(): Promise<void> {
    await this.stockService.buyStock(this.id)
    location.reload()
  }

}
