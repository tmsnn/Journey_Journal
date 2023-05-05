import {HttpEvent, HttpHandler, HttpInterceptor, HttpRequest} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const token = localStorage.getItem('token');
    if (token) {
      console.log('Token found in local storage:', token);
      const newReq = req.clone({
        headers: req.headers.append('Authorization', `JWT ${token}`)
      });
      console.log('Request with Authorization header:', newReq);
      return next.handle(newReq);
    }
    console.log('No token found in local storage');
    return next.handle(req);
  }
}
