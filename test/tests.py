code_1 = """
int globalVar = 10;

float32 power(float32 base, int exponent) {
    float32 result = 1.0;
    int i = 0;
    while (i < exponent) {
        result = result * base;
        i = i + 1;
    }
    return result;
}

void printNumbers(int count) {
    int i = 1;
    while (i <= count) {
        print i;
        if ((i / 2 * 2) == i) {  
            print "even";
        } else {
            print "odd";
        }
        i = i + 1;
    }
}

int factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

void main() {
    int localVar = 5;
    print "Global variable:";
    print globalVar;
    print "Local variable:";
    print localVar;
    print "";
    print "-------------------------------------------------------";
    print "";
    print "Testing power function:";
    float32 p = power(2.5, 3);
    print p;

    print "";
    print "-------------------------------------------------------";
    print "";
    print "Testing printNumbers:";
    printNumbers(4);

    print "";
    print "-------------------------------------------------------";
    print "";
    print "Testing factorial:";
    int fact = factorial(5);
    print fact;

    print "";
    print "-------------------------------------------------------";
    print "";
    print "Testing if statement:";
    if (globalVar > localVar) {
        print "Global is greater";
    } else {
        print "Local is greater";
    }

    print "";
    print "-------------------------------------------------------";
    print "";
    print "Testing while loop:";
    int counter = 3;
    while (counter > 0) {
        print counter;
        counter = counter - 1;
    }

    print "Testing comparison:";
    print (5 > 3);
    print (5 == 3);
}

main();
"""

code_2 = """
void testStandardFor() {
    int i;
    for (i = 0; i < 5; i = i + 1) {
        print i;
    }
}

void testExternalVar() {
    int j = 0;
    for (; j < 3; ) {
        print j;
        j = j + 1;
    }
}

void testInfiniteWithBreak() {
    int k = 0;
    for (; ; ) {
        print k;
        k = k + 1;
        if (k >= 2) {
            break;
        }
    }
}

void testMultipleInits() {
    int a = 0;
    int b = 10;
    for (; a < b; ) {
        print a;
        print b;
        a = a + 1;
        b = b - 1;
    }
}

void main() {
    testStandardFor();
    testExternalVar();
    testInfiniteWithBreak();
    testMultipleInits();
}

main();
"""

code_3 = """
struct Point {
    float32 x;
    float32 y;
};

class Circle {
    Point center;
    float32 radius;

    constructor(float32 x, float32 y, float32 r) {
        center.x = x;
        center.y = y;
        radius = r;
    }

    float32 area() {
        return 3.14159 * radius * radius;
    }

    bool contains(Point p) {
        float32 dx = p.x - center.x;
        float32 dy = p.y - center.y;
        return (dx * dx + dy * dy) <= (radius * radius);
    }
};

void main() {
   
    Point p1;
    p1.x = 2.5;
    p1.y = 3.5;


    Circle c1 = new Circle(1.0, 0.0, 5.0);
    print "Circle c1:";
    print c1.center.x;
    print c1.center.y;
    print c1.radius;

    float32 a = c1.area();
    print "Area of c1:";
    print a;

    bool inside = c1.contains(p1);
    print "Is p1 inside c1?";
    print inside;
}

main();
"""

code_struct_test = """
struct Point {
    float32 x;
    float32 y;
};

void main() {
    Point p1;
    print "Initial values:";
    print p1.x;
    print p1.y;

    p1.x = 2.5;
    p1.y = 3.5;
    print "After assignment:";
    print p1.x;
    print p1.y;

    Point p2 = p1;
    p2.x = 5.0;
    print "After copy modification:";
    print p1.x;
    print p2.x;
}

main();
"""
