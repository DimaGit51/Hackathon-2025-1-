import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CourseService {
  private apiUrl = 'http://127.0.0.1:5000/courses'; // Flask API
  private apiUrl2 = 'http://127.0.0.1:5000/reviews';

  constructor(private http: HttpClient) {}

  getCourses(institute: string, direction: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}?institute=${institute}&direction=${direction}`);
  }

  getReviews(direction: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl2}?direction=${direction}`);
  }
}
