module baustein4(){
    union(){
        cube([3,3,6]);
        translate([3,0,3])
            cube([3,3,3]);
        translate([0,3,3])
            cube([3,3,3]);
        }
}
rotate([180,0,0])
translate([0,0,-6])
    baustein4();