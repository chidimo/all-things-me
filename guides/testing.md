# Mocha

## Loading test data with `psql`

```javascript
import { exec } from 'child_process';

const dump = 'psql -h localhost -d testdb -U postgres -f test/testdb.sql';
const connect = 'psql -h localhost -d testdb -U postgres -c';
const query = 'delete from loans;delete from repayments';
const clear = `${connect} "${query}"`;

before(done => {
    exec(dump, err => {
        if (err) {
            test_logger(`dump error: ${ err }`);
        }
        test_logger('****Database populated successfully.****');
        done();
    });
});

after(done => {
    test_logger('After hook start');
    exec(clear, err => {
        if (err) {
            test_logger(`Error clearing db ${err}`);
        }
    });
    test_logger('****Database cleared successfully.****');
    done();
});
```