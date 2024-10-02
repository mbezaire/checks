#include "time_program.c"


int main(void) {
    time t1, t2;
    t1.hours = 11;
    t1.minutes = 11;
    t1.seconds = 0;

    t2.hours = 11;
    t2.minutes = 15;
    t2.seconds = 10;
    time diff = elapsed_time(t1, t2);
    printf("%02d:%02d:%02d\n", diff.hours, diff.minutes, diff.seconds); // 00:04:10
}
