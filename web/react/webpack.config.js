module.exports = {
	entry: "./static/src/main.jsx",
	output: {
	    path: "./static/js",
		filename: "bundle.js"
	},
	module: {
		loaders: [
			{ test: /\.css$/, loader: "style!css" },
			{ test: /\.jsx$/, loader: "jsx-loader?insertPragma=React.DOM&harmony" }
		]
	},
}
