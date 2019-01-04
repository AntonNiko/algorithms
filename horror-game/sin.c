#include <stdio.h>
#include <stdlib.h>

/* 
IMPROTANT: This program is intended to demonstrate a very ugly form of programming that can be implemented, specifically go-to statements

    GOTO GOTO GOTO GOTO        GOTO GOTO       GOTO GOTO GOTO GOTO        GOTO GOTO
   GOTO             GOTO    GOTO       GOTO            GOTO            GOTO       GOTO
   GOTO             GOTO    GOTO       GOTO            GOTO            GOTO       GOTO
   GOTO                     GOTO       GOTO            GOTO            GOTO       GOTO
   GOTO                     GOTO       GOTO            GOTO            GOTO       GOTO
   GOTO       GOTO GOTO     GOTO       GOTO            GOTO            GOTO       GOTO
   GOTO            GOTO     GOTO       GOTO            GOTO            GOTO       GOTO
    GOTO GOTO GOTO GOTO        GOTO GOTO               GOTO               GOTO GOTO

   -> THE HORROR GAME

*/

int main(int argc, char *argv[]){
    goto return_0;    

    intro: printf("This is the BEST coding program EVER :) /s\n");
    goto return_1;

    greeting: printf("Welcome to this horror game. GOTO HORROR\n");
    goto return_2;

    prompt_1: printf("You are kidnapped by a mad Computer Science proffessor\nwho fell into a violent long-term episode when you accidentally added a go-to statement in your last C assignment.\n\nYou're in a random computer lab, which you can only guess is located in the Engineering Wing. You've just become conscious after a brief period of time, and are seated at a computer. You note a letter that reads:\n");
    goto return_3;

    prompt_2: printf("\nHello there,\nI challenge you to write a program all in go-to statements, because you think you're such a special snowflake...\n");
    goto return_4;

    prompt_3: printf("Do you accept the challenge?? [Y/n]\n");

    end_worst: printf("    GOTO GOTO GOTO GOTO        GOTO GOTO       GOTO GOTO GOTO GOTO        GOTO GOTO\n   GOTO             GOTO    GOTO       GOTO            GOTO            GOTO       GOTO\n   GOTO             GOTO    GOTO       GOTO            GOTO            GOTO       GOTO\n   GOTO                     GOTO       GOTO            GOTO            GOTO       GOTO\n   GOTO                     GOTO       GOTO            GOTO            GOTO       GOTO\n   GOTO       GOTO GOTO     GOTO       GOTO            GOTO            GOTO       GOTO\n   GOTO            GOTO     GOTO       GOTO            GOTO            GOTO       GOTO\n    GOTO GOTO GOTO GOTO        GOTO GOTO               GOTO               GOTO GOTO\n");
    goto return_4;    

    return_0:;

    goto intro;
    return_1:;

    goto greeting;
    return_2:;

    goto prompt_1;
    return_3:;

    goto prompt_2;
    return_4:;

    goto end_worst;
    return_4:;

    return 0;
}
