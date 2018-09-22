# Iwashi

iwashi language.
https://www.youtube.com/watch?v=d_T1StgldnM

## spec
memory size: 2018+

`ptr`: memory pointer. initial is 0. This should be between 0 and 2018.

## instructions
| opcode | function | behavior |
|--------|----------|----------|
|`%d`ねんまえかのことでした| FOCUS `N` | `ptr` := `N` |
|だれかがハサミで| GETC | *ptr := getc() |
|タイムラインをちょんぎった| PUTC | putc(*ptr) |
|そして| GETN | scanf("%d", ptr) |
|あしたときのうがつながった| PUTN | printf("%d", *ptr) |
|あしたのことはしっている| INC | *ptr++ |
|`%s`がつちからはえてくるんだ| JGZ | jump to label:`%s` if *ptr > 0 |
|`%s`にあながあく| LABEL | put label `%s` |
|すのこがきえるんだ| DEC | *ptr-- |
|きのうのきおくはきえたけど| ZERO | *ptr := 0 |
|きえたってこともよくわからないんだ| EXIT | exit() |
|そらのうえから`%s`がたつ| JZ | jump to label:`%s` if *ptr == 0|
|めがみえなくなってきた| NEG | *ptr *= -1 |
|はなはかれず| ADD | *ptr = *(ptr+1) + *(ptr+2) |
|とりはとばずねむる| SUB | *ptr = *(ptr+1) - *(ptr+2) |
|かぜはとまりつめたく| MUL |*ptr = *(ptr+1) * *(ptr+2) |
|つきはみちもかけもせずまわる| DIV |*ptr = *(ptr+1) / *(ptr+2); *(ptr+1) = *(ptr+1) % *(ptr+2) |

## notes
- GETC returns -1 when iwashi fails to read char. (eg. EOF)

## error code
- そんな時代は無い
    memory ptr should be between 0 - 2018

- そんな命令は無い
    invalid opecode
