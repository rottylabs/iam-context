/*
 * Copyright (c) 2019 JD Williams
 *
 * This file is part of Firefly, a Python SOA framework built by JD Williams. Firefly is free software; you can
 * redistribute it and/or modify it under the terms of the GNU General Public License as published by the
 * Free Software Foundation; either version 3 of the License, or (at your option) any later version.
 *
 * Firefly is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
 * implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
 * Public License for more details. You should have received a copy of the GNU Lesser General Public
 * License along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * You should have received a copy of the GNU General Public License along with Firefly. If not, see
 * <http://www.gnu.org/licenses/>.
 */


const path = require('path');
const webpack = require('webpack');
const HtmlWebPackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const DuplicatePackageCheckerPlugin = require("duplicate-package-checker-webpack-plugin");
const CopyPlugin = require('copy-webpack-plugin');
const WebpackWatchPlugin = require('webpack-watch-files-plugin').default;

module.exports = {
  entry: {
    iam: [
        "./src/iam_web/app.py",
        "./src/iam_web/styles.scss"
    ]
  },
  output: {
    filename: "[name].js",
    library: "[name]",
    // libraryTarget: "umd",
    // globalObject: "this",
  },
  devServer: {
    overlay: true,
    hotOnly: true,
  },
  resolve: {
    extensions: ['.js', '.jsx', '.ts', '.tsx', '.py'],
    modules: [
        path.resolve(__dirname, 'node_modules'),
        'node_modules',
    ],
  },
  optimization: {
    minimize: false
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.py$/,
        loader: "transcrypt-loader",
        options: {
          command: '. venv/bin/activate && python3 -m transcrypt',
          arguments: [
              '--nomin',
              '--map',
              '--fcall',
              '--verbose',
          ]
        }
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          {
            loader: "postcss-loader",
            options: {
              ident: "postcss",
              plugins: [
                  require("tailwindcss"),
                  require("autoprefixer"),
              ],
            },
          },
          "sass-loader",
        ],
      },
      {
        test: /\.tsx?$/,
        loader: "ts-loader",
        exclude: /node_modules/,
      },
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "styles.scss",
      chunkFilename: "styles.css"
    }),
    new HtmlWebPackPlugin({
      filename: "index.html",
      template: path.resolve(__dirname, 'src/iam_web/index.html'),
      excludeChunks: ["serviceWorker"]
    }),
    new DuplicatePackageCheckerPlugin(),
    new WebpackWatchPlugin({
      files: [
        './src/**/*.py'
      ]
    }),
    new webpack.HotModuleReplacementPlugin(),
  ]
};
