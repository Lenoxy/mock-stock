import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {RegisterComponent} from "./components/register/register.component";
import {LeaderboardComponent} from "./components/leaderboard/leaderboard.component";
import {LoginComponent} from "./components/login/login.component";
import {ProfileComponent} from "./components/profile/profile.component";
import {StockListComponent} from "./components/stock-list/stock-list.component";
import {StockDetailComponent} from "./components/stock-detail/stock-detail.component";
import {PurchaseComponent} from "./components/purchase/purchase.component";
import {SellComponent} from "./components/sell/sell.component";

const routes: Routes = [
  { path: '', redirectTo: '/register', pathMatch: 'full' },
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
