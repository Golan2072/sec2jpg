import pygame
from math import sin, cos, pi
# import stargen
import pygame.freetype
import sec_parser

pygame.init()

map_font = pygame.freetype.Font("Perfect DOS VGA 437.ttf", 18)
starport_font = pygame.freetype.Font("Perfect DOS VGA 437.ttf", 30)
hex_font = pygame.freetype.Font("Perfect DOS VGA 437.ttf", 14)

def draw_regular_polygon(surface, color, vertex_count,
						 radius, position, width):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + r * cos(2 * pi * i / n),
		 y + r * sin(2 * pi * i / n))
        for i in range(n)
    ], width)


def star_renderer (starmap, hex_column, hex_row):
                if hex_column % 2 != 0:
                    if starmap[hex_column][hex_row].startype == "@":
                        pygame.draw.circle(screen, (0, 255, 0), (80*hex_column*1.5, 140*hex_row-60), 20, 0)
                    elif starmap[hex_column][hex_row].startype in ["0", "&", "#"]:
                        pygame.draw.circle(screen, (0, 255, 0), (80*hex_column*1.5, 140*hex_row-60), 20, 2)
                    else:
                        pass
                    map_font.render_to(screen, (80*hex_column*1.5-40, 140*hex_row-10), starmap[hex_column][hex_row].names, (0, 255, 0))
                    starport_font.render_to(screen, (80*hex_column*1.5-5, 140*hex_row-105), starmap[hex_column][hex_row].starport, (0, 255, 0))
                    hex_font.render_to(screen, (80*hex_column*1.5-15, 140*hex_row-125), starmap[hex_column][hex_row].hex, (0, 255, 0))
                    if starmap[hex_column][hex_row].gas_giant == "*":
                        pygame.draw.circle(screen, (0, 255, 0), (80*hex_column*1.5+30, 140*hex_row-100), 6, 0)
                    else:
                        pass
                    if starmap[hex_column][hex_row].scout == "S":
                        draw_regular_polygon(screen, (0, 255, 0), 3, 10, (80*hex_column*1.5-40, 140*hex_row-25), 0)
                    else:
                        pass
                    if starmap[hex_column][hex_row].naval == "N":
                        draw_regular_polygon(screen, (0, 255, 0), 4, 10, (80*hex_column*1.5-40, 140*hex_row-80), 0)
                    else:
                        pass
                if hex_column % 2 == 0:
                    if starmap[hex_column][hex_row].startype == "@":
                        pygame.draw.circle(screen, (0, 255, 0), (80*hex_column*1.5, 140*hex_row+8), 20, 0)
                    elif starmap[hex_column][hex_row].startype in ["0", "&", "#"]:
                        pygame.draw.circle(screen, (0, 255, 0), (80*hex_column*1.5, 140*hex_row+8), 20, 2)
                    else:
                        pass
                    map_font.render_to(screen, (80*hex_column*1.5-40, 140*hex_row+54), starmap[hex_column][hex_row].names, (0, 255, 0))
                    starport_font.render_to(screen, (80*hex_column*1.5-5, 140*hex_row-40), starmap[hex_column][hex_row].starport, (0, 255, 0))
                    if starmap[hex_column][hex_row].gas_giant == "*":
                        pygame.draw.circle(screen, (0, 255, 0), (80*hex_column*1.5+30, 140*hex_row-40), 6, 0)
                    else:
                        pass
                    if starmap[hex_column][hex_row].scout == "S":
                        draw_regular_polygon(screen, (0, 255, 0), 3, 10, (80*hex_column*1.5-40, 140*hex_row+40), 0)
                    else:
                        pass
                    if starmap[hex_column][hex_row].naval == "N":
                        draw_regular_polygon(screen, (0, 255, 0), 4, 10, (80*hex_column*1.5-40, 140*hex_row-20), 0)
                    else:
                        pass



screen = pygame.display.set_mode([1080, 1540])

pygame.display.set_caption('Cepheus Subsector Map')

starmap = sec_parser.parser_function("sector.sec")


screen.fill((0, 0, 0))
starport_font.render_to(screen, (420,1500), "JEWELL SUBSECTOR (B)", (0, 255, 0))
for hex_column in range (1,9):
    if hex_column % 2 != 0:
        for hex_row in range (1, 11):
            draw_regular_polygon(screen, (0, 255, 0), 6, 80, (80*hex_column*1.5, 140*hex_row-60), 2)
    if hex_column % 2 == 0:
        for hex_row in range (1, 11):
            draw_regular_polygon(screen, (0, 255, 0), 6, 80, (80*hex_column*1.5, 140*hex_row+8), 2)
for hex_column in starmap:
    if hex_column % 2 != 0:
        for hex_row in starmap[hex_column]:
            star_renderer(starmap, hex_column, hex_row)
    if hex_column % 2 == 0:
        for hex_row in starmap[hex_column]:
            star_renderer(starmap, hex_column, hex_row)


pygame.display.update()
pygame.image.save(screen, "starmap.jpeg")
pygame.quit()