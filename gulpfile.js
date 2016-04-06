'use strict';

const gulp        =   require('gulp'),
    apidoc = require('gulp-apidoc'),
    livereload = require('gulp-livereload');

const 	scripts = ['**/*.js', '!./node_modules/*'];

// ---------------------------------------

// ---------------------------------------
//Сборка документации
gulp.task('apidoc', function(){
        apidoc({
            src: "api-docs/",
            dest: "public/",
            debug: true,
            includeFilters: [ ".*\\.py$" ]
        },livereload.reload)
});

gulp.task('copyjson', function() {
   gulp.src('api-docs/**/*.json')
   .pipe(gulp.dest('public/json-data'));
});

gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('api-docs/**/**/*.py', ['apidoc']);
});

// ---------------------------------------
// По умолчанию
gulp.task('default', ['apidoc']);

// ---------------------------------------
// Обработка ошибок
gulp.on('err', function(gulpErr) {
    if (gulpErr.err) {
        // cause
        console.error("Gulp error details", [gulpErr.err.message, gulpErr.err.stack, gulpErr.err.errors].filter(Boolean));
    }
});

process.on('uncaughtException', function(err) {
    console.error(err.message, err.stack, err.errors);
    process.exit(255);
});