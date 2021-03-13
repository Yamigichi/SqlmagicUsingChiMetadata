import ibm_db
import ibm_db_sa

dsn_hostname = "dashdb-txn-sbox-yp-dal09-14.services.dal.bluemix.net"
dsn_uid = "wbf09333"        
dsn_pwd = "gr9-xt3g97f61r5x"      

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"           
dsn_port = "50000"               
dsn_protocol = "TCPIP" 

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)
print(dsn)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )
    
%load_ext sql
%sql ibm_db_sa://wbf09333:gr9-xt3g97f61r5x@dashdb-txn-sbox-yp-dal09-14.services.dal.bluemix.net:50000/BLUDB

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
