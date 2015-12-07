// main.jsx
var React = require('react');
var ReactDOM = require('react-dom');

var Hello = React.createClass({
	displayName: 'Hello react',
	
	render: function() {
		return <div>Hello React</div>
	}
});

ReactDOM.render(
	<Hello />,
	document.getElementById('content')
)