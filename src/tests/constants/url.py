class URL(object):
    BASE_URL = 'https://uatapi.nimbbl.tech/api'
    ORDER_URL = "/orders"
    
    AUTHURL = "v2/generate-token";
	
    ORDER_CREATE = "v2/create-order";
    ORDER_GET = "v2/get-order";
    ORDER_LIST = "orders/many?f=&pt=yes";
	
    LIST_QUERYPARAM1 = "f";
    LIST_QUERYPARAM2 = "pt";
    NO = "no";
    Empty = "";
	
    USER_CREATE = "users/create";
    USER_GET = "users/one";
    USER_LIST = "users/many?f=&pt=yes";
	
    Transaction_CREATE = "transactions/create";
    Transaction_GET = "transactions/one";
    Transaction_LIST = "transactions/many?f=%sandpt=no";
	
    ACCESS_KEY = "access_key";
    SECRET_KEY = "access_secret";
    TOKEN = "token";
    Bearer = "Bearer ";
