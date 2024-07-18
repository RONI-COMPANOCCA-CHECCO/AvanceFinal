// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CursosComponent } from './components/cursos/cursos.component';
import { AnotherComponentComponent } from './components/another-component/another-component.component';
import { CursosService } from './services/cursos.service';

@NgModule({
  declarations: [
    AppComponent,
    CursosComponent,
    AnotherComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [CursosService],
  bootstrap: [AppComponent]
})
export class AppModule { }
