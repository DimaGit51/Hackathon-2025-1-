import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-page5',
  standalone: false,
  templateUrl: './page5.component.html',
  styleUrl: './page5.component.css'
})
export class Page5Component {
  instituteId!: number;
  instituteName = "";
  instituteLogo = "";
  directions: { id: number; name: string }[] = [];
  // directions = [
  //   { id: 1, name: "Программная инженерия", instituteId: 6 },
  //   { id: 2, name: "Информационная безопасность", instituteId: 6 },
  //   { id: 3, name: "Машиностроение", instituteId: 1 },
  //   { id: 4, name: "Цифровой инжинеринг", instituteId: 1 },
  //   { id: 5, name: "Авиационные двигатели", instituteId: 2 },
  //   // Добавь свои направления
  // ];

  constructor(private http: HttpClient, private route: ActivatedRoute, private router: Router) {}

  ngOnInit() {
    window.scrollTo(0,0);
    this.instituteId = Number(this.route.snapshot.paramMap.get('id'));
    const institutes = [
      { id: 1, name: "ИНСТИТУТА АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", image: "assets/faclogo1.png" },
      { id: 2, name: "ИНСТИТУТА ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", image: "assets/faclogo4.png" },
      { id: 3, name: "ИНСТИТУТА ЭКОНОМИКИ И УПРАВЛЕНИЯ", image: "assets/faclogo6.png"},
      { id: 4, name: "СОЦИАЛЬНО-ГУМАНИТАРНОГО ИНСТИТУТА", image: "assets/faclogo8.png"},
      { id: 5, name: "ИНСТИТУТА ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", image: "assets/faclogo5.png"},
      { id: 6, name: "ИНСТИТУТА ИНФОРМАТИКИ И КИБЕРНЕТИКИ", image: "assets/faclogo2.png" },
      { id: 7, name: "ЮРИДИЧЕСКОГО ИНСТИТУТА", image: "assets/faclogo7.png"},
    ];
    
    const institute = institutes.find(inst => inst.id === this.instituteId);
    if (institute) {
      this.instituteName = institute.name;
      this.instituteLogo = institute.image;
    }

    this.http.get<{ id: number; name: string }[]>(`http://localhost:5000/directions/${this.instituteId}`)
    .subscribe({
      next: (data) => {
        // Фильтруем данные, оставляя только элементы с четными id
        this.directions = data.filter(direction => direction.id % 2 === 0);
        // console.log(this.directions); // Выводим отфильтрованные данные
      },
      error: (err) => {
        console.error("Ошибка при получении направлений:", err);
      }
    });
  }

  goToSubjects(directionName: string) {
    console.log(directionName);
    this.router.navigate(['/page4', this.instituteId, directionName]);
   
  }
 

}

