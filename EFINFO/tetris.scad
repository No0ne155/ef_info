module bausteint(){

    difference(){
        union(){
            cube([3,1,1]);
            translate([1,1,0])
                cube([1,1,1]);
        }
        translate([1.25,0.25,-0.01])
            cube([0.5,0.5,1.04]);
 }
 }

rotate([45,45,45])
    scale(5)
        bausteint();
 
