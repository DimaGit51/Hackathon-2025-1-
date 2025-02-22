import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Page1Component } from './page1/page1.component';
import { Page2Component } from './page2/page2.component';
import { Page3Component } from './page3/page3.component';
import { Page4Component } from './page4/page4.component';
import { Page5Component } from './page5/page5.component';
import { AuthGuard } from './auth/auth.guard';

const routes: Routes = [
  { path: 'page1', component: Page1Component },
  { path: 'page3', component: Page3Component, canActivate: [AuthGuard] },
  { path: 'page5/:id', component: Page5Component, canActivate: [AuthGuard] },
  { path: 'page4/:id/:directionName', component: Page4Component, canActivate: [AuthGuard] },
  { path: 'page2/:instituteId/:directionName/:subjectName', component: Page2Component, canActivate: [AuthGuard] },
  { path: '', redirectTo: '/page1', pathMatch: 'full' }, // Перенаправление на логин
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
