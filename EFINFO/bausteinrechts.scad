module bausteinlinks(){
    union(){
        cube([3,3,6]);
        translate([-3,0,3])
            cube([3,6,3]);
        }
}
rotate([90,0,0])
    bausteinlinks();