from manim_rubikscube import *

from manim import *
import random

COLORS = ["#CDCDCD", "#CD4C22", "#2A5CBF", "#F2E422", "#D92938", "#00FF00"]

class CubeExample(ThreeDScene):
    def construct(self):
        cube = RubiksCube(colors=COLORS).scale(0.3).move_to(ORIGIN)
        self.move_camera(phi=60*DEGREES)
        self.renderer.camera.frame_center = cube.get_center()
        self.show_20_pieces(cube)
        self.show_rotations(cube)
        self.show_parities(cube)
        self.show_binary()
        self.show_piece_to_binary()
        self.show_construct_cube()
        self.show_lots_of_cubes()
    
    def show_20_pieces(self, cube):
        cube_seperated = RubiksCube(colors=COLORS, x_offset=3, y_offset=3, z_offset=3).scale(0.3).move_to(ORIGIN)
        cube.save_state()

        self.play(FadeIn(cube))

        self.begin_ambient_camera_rotation(rate=0.5, about="theta")
        self.begin_ambient_camera_rotation(rate=0.01, about="gamma")
        self.wait(3)

        self.play(Transform(cube, cube_seperated), rate_func=rush_from)
        self.wait(3)

        self.stop_ambient_camera_rotation(about="gamma")

        corners = [cube.cubies[0, 0, 0], cube.cubies[0, 0, 2], cube.cubies[0, 2, 0], cube.cubies[0, 2, 2],
                   cube.cubies[2, 0, 0], cube.cubies[2, 0, 2], cube.cubies[2, 2, 0], cube.cubies[2, 2, 2]]
        
        edges = [cube.cubies[0, 0, 1], cube.cubies[0, 1, 0], cube.cubies[0, 1, 2], cube.cubies[0, 2, 1],
                 cube.cubies[1, 0, 0], cube.cubies[1, 0, 2], cube.cubies[1, 2, 2], cube.cubies[1, 2, 0],
                 cube.cubies[2, 0, 1], cube.cubies[2, 1, 0], cube.cubies[2, 1, 2], cube.cubies[2, 2, 1]]
        
        centers = [cube.cubies[0, 1, 1], cube.cubies[1, 0, 1], cube.cubies[1, 1, 0],
                   cube.cubies[1, 1, 2], cube.cubies[1, 2, 1], cube.cubies[2, 1, 1]]
        self.move_camera(frame_center=cube.get_center(), zoom=0.7)
        self.play(*[edge.animate.shift(3.5*LEFT) for edge in edges], *[corner.animate.shift(3.5*RIGHT) for corner in corners])
        self.wait(3)
        self.play(*[Indicate(center) for center in centers])
        self.wait(4)

        self.move_camera(frame_center=cube.get_center(), zoom=1)
        self.play(Restore(cube), rate_func=rush_from)
        self.wait(5)
        self.begin_ambient_camera_rotation(rate=-0.2, about="theta")
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=-0.2, about="theta")
        self.wait(1)
        self.stop_ambient_camera_rotation(about="theta")
        self.wait(1)

    def show_rotations(self, cube):
        self.add(cube)
        cube_corner_rotate_1 = RubiksCube(colors=COLORS).scale(0.3).move_to(ORIGIN)
        cube_corner_rotate_2 = RubiksCube(colors=COLORS).scale(0.3).move_to(ORIGIN)
        
        cube_corner_rotate_1.set_state("UUBUUUUUURRURRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLRBBBBBBBB")
        cube_corner_rotate_2.set_state("UURUUUUUURRBRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLUBBBBBBBB")
        self.move_camera(frame_center=cube.get_center(), zoom=0.7)
        self.play(FadeIn(cube_corner_rotate_1), cube.animate.shift(3.5*LEFT))
        self.play(FadeIn(cube_corner_rotate_2), cube_corner_rotate_2.animate.shift(3.5*RIGHT))
        self.wait(3)
        self.play(FadeOut(cube_corner_rotate_1), cube_corner_rotate_2.animate.shift(3.5*LEFT))
        self.play(FadeOut(cube_corner_rotate_2), cube.animate.shift(3.5*RIGHT))
        self.move_camera(frame_center=cube.get_center(), zoom=1)
        self.wait(1)
        
        cube_edge_rotate = RubiksCube(colors=COLORS).scale(0.3).move_to(ORIGIN)
        cube_edge_rotate.set_state("UUUUURUUURURRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB")
        self.play(FadeIn(cube_edge_rotate), cube_edge_rotate.animate.shift(1.75*RIGHT), cube.animate.shift(1.75*LEFT))
        self.wait(3)
        self.play(FadeOut(cube_edge_rotate), cube_edge_rotate.animate.shift(1.75*LEFT), cube.animate.shift(1.75*RIGHT))
        self.wait(3)
    
    def show_parities(self, cube):
        self.add(cube)
        cube_unsolved = RubiksCube(colors=COLORS).scale(0.3).move_to(ORIGIN)
        cube_unsolved.set_state("BBFBUBUDFDDURRDDURLLLDFUBFRLLFFDLUFBDUBBLFFUDLRRRBLURR")
        self.play(Transform(cube, cube_unsolved))

        for m in cube.solve_by_kociemba("BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"):
            # Execute the move
            self.play(CubeMove(cube, m), run_time=0.5)
        
        self.wait(3)

        cube_corner_rotate_1 = RubiksCube(colors=COLORS).scale(0.3).move_to(ORIGIN)
        cube_corner_rotate_1.set_state("UUBUUUUUURRURRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLRBBBBBBBB")

        cube_edge_rotate = RubiksCube(colors=COLORS).scale(0.3).move_to(ORIGIN)
        cube_edge_rotate.set_state("UUUUUUUUURFRRRRRRRFRFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB")

        self.move_camera(frame_center=cube.get_center(), zoom=0.7)
        self.play(FadeIn(cube_corner_rotate_1), cube_corner_rotate_1.animate.shift(3.5*LEFT))
        self.play(FadeIn(cube_edge_rotate), cube_edge_rotate.animate.shift(3.5*RIGHT))

        self.wait(3)

        self.play(Rotating(cube_corner_rotate_1, np.array((0, 0, -1))), run_time=2)
        self.play(Rotating(cube, np.array((0, 0, -1))), run_time=2)
        self.play(Rotating(cube_edge_rotate, np.array((0, 0, -1))), run_time=2)

        self.wait(3)
        self.play(*[FadeOut(mobject) for mobject in self.mobjects])
    
    def show_binary(self):
        self.move_camera(frame_center=ORIGIN, zoom=1, phi=0, theta=-PI/2, gamma=0)
        file = SVGMobject("file.svg").set_color(WHITE)
        self.play(FadeIn(file))
        self.wait(2)
        binary_string = "1101010010110101100101011010101101010010101101010101011010101010"
        binary_mobject = Text(binary_string, font_size=48, color=WHITE)
        self.play(Transform(file, binary_mobject))
        self.play(file.animate.shift(3*LEFT), run_time=5)
        self.wait(2)
        bit_heading = Text("bit", font_size=64).shift(3*UP)
        self.play(Circumscribe(file[39]))
        self.play(Circumscribe(file[40]))
        self.play(Write(bit_heading))
        self.wait()
        self.play(FadeOut(file), FadeOut(bit_heading))

        cube_image = ImageMobject('cube.jpg')
        image_heading = Text("256x256", font_size=64).shift(3*UP)
        bit_count = Text("1,572,864 bits", font_size=64, color=YELLOW).shift(2.5*DOWN)
        background_square = Square(side_length=1.9, color=WHITE, fill_opacity=1).move_to(cube_image.get_center())
        self.play(Write(image_heading), FadeIn(background_square), FadeIn(cube_image))
        self.wait(2)
        self.play(Write(bit_count))
        self.wait(2)
        self.play(FadeOut(cube_image), FadeOut(image_heading), FadeOut(bit_count), FadeOut(background_square))
    
    def show_piece_to_binary(self):
        self.move_camera(frame_center=ORIGIN, zoom=1, phi=60*DEGREES, theta=0, gamma=0)
        cube = RubiksCube(colors=COLORS, x_offset=3, y_offset=3, z_offset=3).scale(0.3).move_to(ORIGIN)
        self.move_camera(frame_center=cube.get_center(), theta=-3*PI/4)
        corners = [cube.cubies[0, 0, 0].rotate(PI/2, axis=UP), 
                   cube.cubies[0, 0, 2].rotate(-PI/2, axis=UP).rotate(-PI/2, axis=RIGHT), 
                   cube.cubies[0, 2, 0].rotate(PI, axis=RIGHT), 
                   cube.cubies[0, 2, 2].rotate(PI/2, axis=RIGHT),
                   cube.cubies[2, 0, 0].rotate(PI, axis=UP), 
                   cube.cubies[2, 0, 2].rotate(PI, axis=UP).rotate(-PI/2, axis=RIGHT), 
                   cube.cubies[2, 2, 0].rotate(PI, axis=UP).rotate(PI/2, axis=RIGHT), 
                   cube.cubies[2, 2, 2].rotate(PI, axis=UP).rotate(PI, axis=RIGHT)]
        
        binary_group = VGroup()
        for i, corner in enumerate(corners):
            corner.move_to(ORIGIN+4*LEFT+i*RIGHT)
            binary = Text(f"{bin(i)[2:]}", font_size=64).move_to(corner).rotate(PI/2, axis=np.array((0, 0, -1))).shift(1.5*DOWN)
            binary_group.add(binary)
        
        for i, corner in enumerate(corners[::-1]):
            self.play(FadeIn(corner), FadeIn(binary_group[::-1][i]))
        self.wait(3)

        for i, corner in enumerate(corners):
            self.play(Rotate(corner, angle=-PI/2, axis=UP))
            new_binary = Text(f"{bin(i+8)[2:]}", font_size=64).move_to(corner).rotate(PI/2, axis=np.array((0, 0, -1))).shift(2*DOWN)
            self.play(Rotate(corner, angle=-PI/2, axis=RIGHT), Transform(binary_group[i], new_binary))

        for i, corner in enumerate(corners):
            self.play(Rotate(corner, angle=-PI/2, axis=UP))
            new_binary = Text(f"{bin(i+16)[2:]}", font_size=64).move_to(corner).rotate(PI/2, axis=np.array((0, 0, -1))).shift(2.5*DOWN)
            self.play(Rotate(corner, angle=-PI/2, axis=RIGHT), Transform(binary_group[i], new_binary))
        
        self.wait(3)
        self.play(*[FadeOut(mobject) for mobject in self.mobjects])

    def show_construct_cube(self):
        cube = RubiksCube(colors=COLORS).scale(0.3).move_to(ORIGIN)
        #self.move_camera(frame_center=ORIGIN, zoom=1, phi=60*DEGREES, theta=30*DEGREES, gamma=0)

        state_solvable = "RBLFULFRD" + "RDBRRRUBF" + "LBBLFFBRR" + "UUBUDLLDD" + "FDUFLFDLL" + "DUUDBURBF"
        state = "RBDFULFRD" + "RDLRRRUBF" + "LBBLFFBRR" + "UUBUDLLDD" + "FDUFLFDLL" + "BUUDBURBF"
        cube.set_state(state)

        centers = [cube.cubies[0, 1, 1], cube.cubies[1, 0, 1], cube.cubies[1, 1, 0],
                   cube.cubies[1, 1, 2], cube.cubies[1, 2, 1], cube.cubies[2, 1, 1]]
        
        self.play(*[FadeIn(center) for center in centers])
        order = [-1, -4, -7, -10, -16, -19, -22, -25,
                 -2, -8, -20, -26,
                 -3, -6, -9, -12, -18, -21, -24, -27]
        
        # Have a binary background
        for i in order:
            if i == -1:
                self.move_camera(phi=60*DEGREES, theta=30*DEGREES)
            if i == -20:
                self.move_camera(phi=60*DEGREES, theta=-120*DEGREES)
            if i == -3:
                self.move_camera(phi=60*DEGREES, theta=30*DEGREES)
            if i == -18:
                self.move_camera(phi=60*DEGREES, theta=-120*DEGREES)
            self.play(FadeIn(cube[i]))

        for m in cube.solve_by_kociemba(state_solvable):
            # Execute the move
            self.play(CubeMove(cube, m), run_time=.5)
        
        self.wait(2)
        self.move_camera(phi=240*DEGREES, theta=-120*DEGREES)

        self.wait(3.5)
        cube1 = RubiksCube(colors=COLORS).scale(0.3).move_to(ORIGIN)
        cube1[-3].set_fill(WHITE)
        cube1[-6].set_fill(WHITE)
        cube1[-9].set_fill(WHITE)
        cube1[-12].set_fill(WHITE)
        self.wait(3)
        self.play(FadeOut(cube), FadeIn(cube1))
        self.wait(8)
        self.play(*[FadeOut(mobject) for mobject in self.mobjects])

    def show_lots_of_cubes(self):
        self.move_camera(frame_center=ORIGIN, zoom=1, phi=60*DEGREES, theta=0, gamma=0)
        cubes = VGroup()
        for i in range(4):
            layer = VGroup(*[RubiksCube(colors=COLORS).scale(0.1) for _ in range(25)])
            layer.arrange_in_grid(5, 5, 0.25)
            layer.shift(np.array((0, 0, -1)) * i)  # Adjust the vertical spacing as needed
            cubes.add(layer)
        cubes.move_to(ORIGIN)
        for layer in cubes[::-1]:
            self.play(FadeIn(layer))
        self.wait(3)
        self.play(FadeOut(cubes))
        self.wait(3)        
