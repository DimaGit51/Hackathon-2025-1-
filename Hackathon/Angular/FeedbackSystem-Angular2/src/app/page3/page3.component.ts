import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-page3',
  standalone: false,
  templateUrl: './page3.component.html',
  styleUrl: './page3.component.css'
})
export class Page3Component {
  institutes = [
    { id: 1, name: "ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", image: "assets/faclogo1.png" },
    { id: 2, name: "ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", image: "assets/faclogo4.png" },
    { id: 3, name: "ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", image: "assets/faclogo6.png" },
    { id: 4, name: "СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", image: "assets/faclogo8.png" },
    { id: 5, name: "ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", image: "assets/faclogo5.png" },
    { id: 6, name: "ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", image: "assets/faclogo2.png" },
    { id: 7, name: "ЮРИДИЧЕСКИЙ ИНСТИТУТ", image: "assets/faclogo7.png" },
  ];

  constructor(private router: Router) {}

  goToSubjects(instituteId: number) {
    this.router.navigate(['/page5', instituteId]);
  }

  ngOnInit(){
    window.scrollTo(0,0);
  }
}

