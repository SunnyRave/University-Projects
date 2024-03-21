#include <stdio.h>
#include <string.h>

int main() {
    int n, i, m, s, j, k;
    printf("Size of network: ");
    scanf("%d", &n);

    char stationnamesArray1[n][17];
    int transfertimes[n];

    for (i = 0; i < n; i++)
    {
        scanf("%16s", stationnamesArray1[i]);
        scanf("%d", &transfertimes[i]);
    }

    printf("Number of timetables: ");
    scanf("%d", &m);

    int stopsPerTimetable[m]; // Keep track of the number of stops per timetable
    char stationnamesArray2[m][100][17]; // Assume max 100 stops per timetable
    char stationtime[m][100][5]; // Assume max 100 stops per timetable

    for (i = 0; i < m; i++)
    {
        printf("Number of stops: ");
        scanf("%d", &s);
        stopsPerTimetable[i] = s;
        for (j = 0; j < s; j++)
        {
            scanf("%16s", stationnamesArray2[i][j]);
            scanf("%4s", stationtime[i][j]);
        }
    }
    printf("\n");
    while (1)
    {
        char fromstation[17], tostation[17];
        char arrivaltime[5];
        printf("From: ");
        scanf("%16s", fromstation);
        printf("To: ");
        scanf("%16s", tostation);
        printf("Arrive at or before: ");
        scanf("%4s", arrivaltime);
        if (strcmp(fromstation, "done") == 0)
        {
            break;
        }
        for (i = 0; i < m; i++)
        {
            for (j = 0; j < stopsPerTimetable[i]; j++)
            {
                if (strcmp(stationnamesArray2[i][j], fromstation) == 0 && strcmp(stationtime[i][j], arrivaltime) >= 0)
                {
                    k = j;
                    while (1)
                    {
                        printf("%s %s\n", stationtime[i][k], stationnamesArray2[i][k]);
                        k = k + 1;
                        if (k == stopsPerTimetable[i] || strcmp(stationnamesArray2[i][k], tostation) == 0)
                        {
                            break;
                        }
                    }
                }
            }
        }
    }
    for (i = 0; i < n; i++)
    {
        printf("%s - Transfer time: %d\n", stationnamesArray1[i], transfertimes[i]);
    }

    // Print all station names and stop times for all timetables
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < stopsPerTimetable[i]; j++)
        {
            printf("%s %s\n", stationtime[i][j], stationnamesArray2[i][j]);
        }
    }
    return 0;
}
