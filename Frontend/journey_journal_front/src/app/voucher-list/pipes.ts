import {Pipe, PipeTransform} from '@angular/core';

@Pipe({
  name: 'filter'
})

export class FilterPipe implements PipeTransform {
  transform(items: any[], searchText: string): any[] {
    if (items && items.length) {
      return items.filter(item => {
        return !(searchText &&
          item.name.toLowerCase().indexOf(searchText.toLowerCase()) === -1);
      });
    } else {
      return items;
    }
  }
}
