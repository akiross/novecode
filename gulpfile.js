var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var minifyCSS = require('gulp-minify-css');
var rename = require('gulp-rename');

gulp.task('default', ['sass']);

gulp.task('sass', function() {
    gulp.src('./assets/scss/main.scss')
        .pipe(sass({
            includePaths: ['./node_modules/foundation-sites/scss']
        }))
        .pipe(sourcemaps.init())
        .pipe(minifyCSS())
        .pipe(sourcemaps.write())
        .pipe(rename('style.css'))
        .pipe(gulp.dest('./static/css/'))
});

gulp.task('watch', function() {
    gulp.watch('./assets/scss/***.scss', ['sass']);
});
