import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CourseService } from '../services/course.service'; 

@Component({
  selector: 'app-page4',
  standalone: false,
  templateUrl: './page4.component.html',
  styleUrl: './page4.component.css'
})
export class Page4Component {
  instituteId!: number;
  directionId!: number;
  directionName = "";
  subjectName="";
  subjects: any[] = [];
  selectedCourse = "1 курс";
  userRole: number = 0;
  courses = ["1 курс", "2 курс", "3 курс", "4 курс", "Магистратура"];
  // directions = [
  //   { id: 1, name: "Программная инженерия", instituteId: 6 },
  //   { id: 2, name: "Информационная безопасность", instituteId: 6 },
  //   { id: 3, name: "Машиностроение", instituteId: 1 },
  //   { id: 4, name: "Цифровой инжинеринг", instituteId: 1 },
  //   { id: 5, name: "Авиационные двигатели", instituteId: 2 },
  // ];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private courseService: CourseService 
  ) {}

  ngOnInit() {
    window.scrollTo(0, 0);
    
    const userData = localStorage.getItem('user');
    if (userData) {
      const user = JSON.parse(userData);
      this.userRole = user.prefix;
    }
  
    this.instituteId = Number(this.route.snapshot.paramMap.get('id'));
    this.directionName = String(this.route.snapshot.paramMap.get('directionName'));
    console.log(this.instituteId);
    console.log(this.directionName);
    console.log(this.directionId);
    // const direction = this.directions.find(d => d.id === this.directionId);
    // if (direction) {
    //   this.directionName = direction.name;
    // }
    
    // console.log(this.directionName);
    this.loadSubjects();
  }

  loadSubjects() {
    const institutes = [
      { id: 1, name: "ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ" },
      { id: 2, name: "ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК" },
      { id: 3, name: "ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ" },
      { id: 4, name: "СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ" },
      { id: 5, name: "ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК" },
      { id: 6, name: "ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ" },
      { id: 7, name: "ЮРИДИЧЕСКИЙ ИНСТИТУТ" }
    ];
    //
    const institute = institutes.find(inst => inst.id === this.instituteId);
    console.log(institute);
    if (!institute) return;
//"Программирование и информационные технологии"
    //this.courseService.getCourses(institute.name, "Программирование и информационные технологии").subscribe(
    this.courseService.getCourses(institute.name, this.directionName).subscribe(
      (data) => {
         
        this.subjects = data.map(course => ({
          id: course.id,
          name: course.directions,
          course: `${course.year} курс`,

        })
        
      );
      // console.log("Дисциплины:", this.subjects);
    
      },
      (error) => {
        console.error("Ошибка при загрузке курсов:", error);
      }
    );
  }

  get filteredSubjects() {
    return this.subjects.filter(s => s.course === this.selectedCourse);
  }

  goToProfessors(subjectName: string) {
    this.router.navigate(['/page2', this.instituteId, this.directionName, subjectName]);
  }

  openDisciplineForm = false;
newDiscipline = { id: 0, name: "", course: this.selectedCourse };

openAddDisciplineForm() {
  this.newDiscipline = { id: this.subjects.length + 1, name: "", course: this.selectedCourse };
  this.openDisciplineForm = true;
}
closeDisciplineForm() {
  this.openDisciplineForm = false;
}

addDiscipline() {
  if (!this.newDiscipline.name.trim()) {
    alert("Введите название дисциплины!");
    return;
  }
}
}
