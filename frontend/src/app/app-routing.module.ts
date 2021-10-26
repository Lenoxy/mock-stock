import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {RegisterComponent} from "./register/register.component";
import {LeaderboardComponent} from "./leaderboard/leaderboard.component";
import {LoginComponent} from "./login/login.component";
import {ProfileComponent} from "./profile/profile.component";
import {StockListComponent} from "./stock-list/stock-list.component";
import {StockDetailComponent} from "./stock-detail/stock-detail.component";
import {PurchaseComponent} from "./purchase/purchase.component";
import {SellComponent} from "./sell/sell.component";

const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'user/:id', component: ProfileComponent },
  { path: 'stock-list', component: StockListComponent },
  { path: 'stock-detail/:id', component: StockDetailComponent },
  { path: 'leaderboard', component: LeaderboardComponent },
  { path: 'purchase/:id', component: PurchaseComponent },
  { path: 'sell/:id', component: SellComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
