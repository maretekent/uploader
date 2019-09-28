var webpack = require("webpack");
const path = require("path");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const ENVIRONMENT = process.env.ENVIRONMENT ?
    process.env.ENVIRONMENT.toLowerCase() : "development";


let mode = null;
let watchFiles = null;

if (ENVIRONMENT === "development"){
    mode = "development";
    watchFiles = true;
} else {
    mode = "production";
    watchFiles = false;
}


const webPackConfig = {
    mode: mode,
    watch: watchFiles,
    watchOptions: {
        ignored: /node_modules/,
        poll: 1000
    },
    optimization: {
        minimizer: [
            new UglifyJsPlugin({
                cache: true,
                parallel: true,
                uglifyOptions: {
                    compress: true,
                    output: {
                        comments: false,
                        beautify: false
                    }
                },
                sourceMap: true
            })
        ]
    },
    entry: {
        "auto-logout": "./app_dir/portal/static/js/auto-logout/app.js"
    },
    output: {
        path: path.resolve("./app_dir/portal/static/dist/js"),
        filename: "[name].bundle.js"
    },
    module: {
        rules: [
            {
                test: /\.jsx?/,
                loader: "babel-loader",
                exclude: /node_modules/,
                options: { cacheDirectory: true }
            },
            {
                test: /\.(sa|sc|c)ss$/,
                use: ["style-loader", "css-loader", "sass-loader"]
            }
        ]
    },
    plugins: [
        new webpack.DefinePlugin({
            "process.env.NODE_ENV": JSON.stringify(ENVIRONMENT)
        })
    ],
    target: "web",
    devtool: "source-map"
};

module.exports = webPackConfig;

