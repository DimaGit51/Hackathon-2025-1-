
import { Component } from '@angular/core';
import { CourseService } from '../services/course.service'; 
import { ActivatedRoute, Router } from '@angular/router';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-page2',
  standalone: false,
  templateUrl: './page2.component.html',
  styleUrls: ['./page2.component.css']
})
export class Page2Component {
 
  reviews: any[] = [];
  str_fff = "";
  isFormVisible = false;
  isSubmitted = false;
  directionName = ""; 
  login='';
  newReview = {
    text: '',
    rating: 0,
    teacher_name: '',
    direction: this.str_fff,
    login:''
  };


  toggleReviewForm() {
    this.isFormVisible = !this.isFormVisible;
  }
  // deleteReview(index: number, reviewText: string) {
  //   if (this.userRole < 1) {  // Если роль меньше 1, запрещаем удаление
  //     alert("У вас нет прав для удаления этого отзыва!");
  //     return;
  //   }
  //   if (!confirm("Вы уверены, что хотите удалить этот отзыв?")) return;
  
  //   this.http.delete(`http://localhost:5000/delete_review`, {
  //     body: { text: reviewText }  // Передаём текст отзыва
  //   }).subscribe({
  //     next: () => {
  //       alert("Отзыв удалён!");
  //     },
  //     error: () => {
  //       alert("Ошибка при удалении отзыва!");
  //     }
  //   });
  // }
  
  submitReview() {
    
    console.log("dir");
    console.log(this.str_fff);
    if (!this.newReview.teacher_name || !this.newReview.text || this.newReview.rating <= 0) {
      
      alert("Заполните все поля и выберите рейтинг!");
      return;
    }
    console.log(this.newReview.teacher_name);
    console.log(this.newReview.text);
    console.log(this.newReview.rating);
    console.log(this.str_fff);
    
    // Перед отправкой устанавливаем direction
  this.newReview.direction = this.directionName;
  const reviewToSend = { ...this.newReview };
  console.log("Отправляем данные на сервер:", reviewToSend);

  this.http.post('http://localhost:5000/add_reviews', reviewToSend).subscribe({
    next: (response: any) => {
      alert('Спасибо за отзыв!');
      this.reviews.push({ ...reviewToSend });
      this.isSubmitted = true;
      this.newReview.rating = 0;
      this.newReview.teacher_name = "";
      this.newReview.text = "";
      setTimeout(() => {
        this.isSubmitted = false;
        this.isFormVisible = false;
      }, 5000);
    },
    error: () => {
      alert('Ошибка при отправке отзыва');
    }
  });

}

         
  userRole: number = 0;
  constructor(
    private http: HttpClient,
    private route: ActivatedRoute,
    private router: Router,
    private courseService: CourseService 
  ) {}
  ngOnInit(){
    this.directionName = String(this.route.snapshot.paramMap.get('subjectName'));
    this.str_fff = this.directionName; // Устанавливаем str_fff при загрузке
    window.scrollTo(0,0);
    const userData = localStorage.getItem('user');
    if (userData) {
      const user = JSON.parse(userData);
      this.userRole = user.prefix;
      this.login = user.login;  // Устанавливаем логин
      this.newReview.login = this.login;  // Передаем в newReview
    }
    this.loadReviews();
  }


  loadReviews() {
    this.courseService.getReviews(this.directionName).subscribe(
      (data) => {
        console.log("Загруженные отзывы:", data); // Проверяем, какие данные приходят с сервера
        
        this.reviews = data.map(review => ({
          teacher_name: review.teacher_name || "Неизвестный преподаватель",
          text: review.text || "Отзыв отсутствует",
          rating: review.rating || 0
        }));
  
        console.log("После обработки:", this.reviews);
      },
      (error) => {
        console.error("Ошибка при загрузке отзывов:", error);
      }
    );
  }


  getStars(rating: number) {
    return new Array(rating);
  }

  closeToast() {
    this.isSubmitted = false;  // Закрыть Toast вручную
  }
}
