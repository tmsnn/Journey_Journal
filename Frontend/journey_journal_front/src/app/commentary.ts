export class Commentary {
  static cnt = 0;
  id: number;
  username: string;
  voucher: number;
  description: string;

  constructor(username: string, voucher: number, description: string) {
    this.id = Commentary.cnt++;
    this.username = username;
    this.voucher = voucher;
    this.description = description;
  }
}
