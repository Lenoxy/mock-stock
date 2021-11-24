import { Component, OnInit } from '@angular/core';
import {StockService} from "../../services/stock/stock.service";

@Component({
  selector: 'app-stock-detail',
  templateUrl: './stock-detail.component.html',
  styleUrls: ['./stock-detail.component.scss']
})
export class StockDetailComponent implements OnInit {

  basicData: any
  basicOptions: any
  stock: any
  constructor(private stockservice: StockService) { }

 async ngOnInit(): Promise<void> {
    this.stock = JSON.parse((await this.stockservice.getStock()).body)
   const historyValues = Object.values(this.stock.history)
   const historyKeys = Object.keys(this.stock.history)
    this.basicData = {
      labels: [...historyKeys],
      datasets: [
        {
          label: this.stock.name,
          data: [...historyValues],
          fill: false,
          borderColor: '#42A5F5',
          tension: .1
        }
      ]
    }
  }

  updateOptions() {
    this.basicOptions = {
      plugins: {
        legend: {
          labels: {
            color: '#495057'
          }
        }
      },
      scales: {
        x: {
          ticks: {
            color: '#495057'
          },
          grid: {
            color: '#ebedef'
          }
        },
        y: {
          ticks: {
            color: '#495057'
          },
          grid: {
            color: '#ebedef'
          }
        }
      }
    };



  }

}
