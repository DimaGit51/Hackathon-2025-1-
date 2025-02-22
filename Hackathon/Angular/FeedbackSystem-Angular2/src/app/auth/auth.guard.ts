import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(private router: Router) {}

  canActivate(): boolean {
    
    const userData = localStorage.getItem('user');

    if (userData) {
      const user = JSON.parse(userData);
      
      // Если у пользователя нет роли, считаем его гостем (prefix = 0)
      if (user.prefix === undefined) {
        user.prefix = 0;
      }
      
      return true;
    } else {
      this.router.navigate(['/login']);
      return false;
    }
    
  }
}

