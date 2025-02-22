import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-page1',
  standalone: false,
  templateUrl: './page1.component.html',
  styleUrl: './page1.component.css'
})
export class Page1Component {
  login: string = '';
  password: string = '';

  constructor(private http: HttpClient, private router: Router) {}

  login_func() {
    const loginData = { login: this.login, password: this.password };
    this.http.post('http://localhost:5000/auth', loginData).subscribe({
      
      next: (response: any) => {
        // Проверяем, если login пользователя совпадает с 'user', устанавливаем prefix в 3
        if (response.login === 'user') {
          response.prefix = 3;
        }

        localStorage.setItem('user', JSON.stringify({ login: response.login, prefix: response.prefix}));
        this.router.navigate(['/page3']);
      },
      error: () => {
        alert('Неверные данные');
      }
    });
  }

  // login_func() {
  
  //     let userRole = 0; // По умолчанию гость
    
  //     if (this.login === 'admin' && this.password === '123') {
  //       userRole = 2; // Админ
  //     } else if (this.login === 'moder' && this.password === '123') {
  //       userRole = 1; // Модератор
  //     } else if (this.login === 'user' && this.password === '123') {
  //       userRole = 3; // Гость
  //     } else {
  //       alert('Неверные данные');
  //       return;
  //     }
    
  //     // Сохраняем логин и роль в localStorage
  //     localStorage.setItem('user', JSON.stringify({ login: this.login, prefix: userRole }));
      
  //     this.router.navigate(['/page3']); 
  // }
  loginAsGuest() {
    localStorage.setItem('user', JSON.stringify({ login: 'guest', prefix: 0 }));
    this.router.navigate(['/page3']);
  }

  ngOnInit(){
    window.scrollTo(0,0);
  }
}
