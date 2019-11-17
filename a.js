const Observable = rxjs.Observable;
const fromEvent = rxjs.fromEvent;
const operators = rxjs.operators;

const map = operators.map;
const retry = operators.retry;
const filter = operators.filter;
const switchMap = operators.switchMap
const throttleTime = operators.throttleTime;
const distinctUntilChanged = operators.distinctUntilChanged;
const $ = jQuery;
console.log(operators)

const box = document.querySelector('#textbox');
const area = document.querySelector('#textarea');
const links = document.querySelector('#links');
const error = document.querySelector('#error');

const keyPresses = fromEvent(box, 'keypress');
// keyPresses.forEach(kp => {
//     console.log(kp.keyCode, kp.target.value)
// })

const searchWiki = term => {
	const encoded = encodeURIComponent(term)
	const url = `https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=${encoded}&callback=?`
	$.getJSON(url, data => {
		console.log('return data', data);
	})
}

// adapt search API to an observable
const searchObservable = term => {
	return new Observable(subscriber => {
		let cancelled = false;
		const encoded = encodeURIComponent(term)
		const url = `https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=${encoded}&callback=?`

		try {
			$.getJSON(url, data => {
				if (!cancelled) {
					subscriber.next(data);
				} else {
					subscriber.complete();
				}
			})
		} catch (err) {
			subscriber.error(err);
		}

		return unsubscribe = () => {
			cancelled = true;
		}
	})
}

// const s = searchWiki('super eagles')
// s.subscribe({
//     next: data => console.log(data),
//     complete: console.log('I am done'),
//     error: err => console.log('error', err)
// })

const searchResultSet = keyPresses
.pipe(
	throttleTime(250),
	map(key => key.target.value),
	distinctUntilChanged(),
	// don't send empty search
	filter(term => term.trim().length > 0),
	map(term => {
		console.log(term)
		return searchObservable(term)
	}),
	retry(2),
);

searchResultSet.forEach(results => {
	results.subscribe({
		next: data => {
			console.log(data)
			area.value = data[1].join('\n');

			links.innerHTML = ''; // reset the links div
			data[3].forEach(link => {
				const p = document.createElement('p');
				const a = document.createElement('a');
				a.href = link;
				a.target = '_blank';
				a.textContent = link;
				p.appendChild(a);
				links.appendChild(p);
			})
			// console.log(data);
		},
		complete: console.log('I am done'),
		error: err => {
			console.log('error', err);
			error.textContent = err.info;
		}
	})
})

// searchResultSet.subscribe({
// 	next: data => {
// 		results.value = data[1];
// 		const l = data[3]
// 		l.forEach(link => {
// 			const p = document.createElement('p');
// 			const a = document.createElement('a');
// 			a.href = link;
// 			a.textContent = link;
// 			console.log(a)
// 			p.appendChild(a);
// 			links.appendChild(p);
// 		})
// 		// console.log(data);
// 	},
// 	complete: console.log('I am done'),
// 	error: err => console.log('error', err)
// })
