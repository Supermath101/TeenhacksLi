var path = require('path');

module.exports = {
    module: {
    rules: [
        {
          test: /\.m?jsx$/,
          exclude: /(node_modules|bower_components)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-react', '@babel/preset-env']
            }
          }
        }
      ]
    },
  mode: 'development',
  entry: './src/web/main.jsx',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'main.bundle.js'
  }
};
