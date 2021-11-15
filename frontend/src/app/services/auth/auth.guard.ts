import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree} from "@angular/router";
import {Injectable} from "@angular/core";
import {AuthService} from "./auth.service";
import {from, Observable} from "rxjs";
import {map} from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private router: Router,
              private authService: AuthService
              ) {}

  loggedIn = false

   canActivate(next: ActivatedRouteSnapshot,
               state: RouterStateSnapshot
   ): Observable<any>{
    return from(this.authService.isLoggedin()).pipe(
      map(resp => {
        if (resp.body === 'False') {
          return true;
        }
        this.router.navigate(['/stock-list']);
        return false;
      })
    );
  }

}
