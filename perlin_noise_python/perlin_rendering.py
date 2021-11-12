import noise
import numpy as np
import pygame
import random
import math

from PIL import Image


class Perlin_1D():
    def __init__(self, element):
        self.horizontal_points  = 440
        self.vertical_points = 620
     
        self.NormalNoiseSeed = [0] * self.vertical_points
        self.PerlinNoiseSeed = [0] * self.vertical_points

        self.initial_generation()

    def initial_generation(self):
        for i in range(0, self.vertical_points):
            self.NormalNoiseSeed[i] = random.random()


    def calculate_perlin(self, octaves, bias):
        image = Image.new('RGB', (self.vertical_points, self.horizontal_points), (80,80,80))
        pixel_array = image.load()   
        
        self.perlin_noise_algorithm(self.vertical_points, self.NormalNoiseSeed, octaves, bias, self.PerlinNoiseSeed)

        for i in range(self.vertical_points):
            y = math.floor(self.PerlinNoiseSeed[i] * self.horizontal_points * 3/4)
            for j in range(0, y):     
                pixel_array[i,  (self.horizontal_points-1) - j] = (35, 159, 217)

        image.save("map.png")
        
    def perlin_noise_algorithm(self, Count, normalNoise, Octaves, Bias, Output):
        for x in range(Count):
            Noise_sum = 0.0
            Scale_sum = 0.0
            Scale = 1.0

            for o in range(Octaves):
			
                Pitch = int(math.floor( Count/pow(2, o) ))
                Sample_1 = int(math.floor(x / Pitch)) * Pitch 
                Sample_2 = (Sample_1 + Pitch) % Count

                Blend = float(x - Sample_1) / float(Pitch)
                #tutaj robimy interpolację liniową -> przybliżamy wartości szumu na podstawie dwóch znanych
                #wartości Sample_1 i Sample_2
                Sample = float(1.0 - Blend) * normalNoise[Sample_1] + Blend * normalNoise[Sample_2]
            
                Scale_sum += Scale;
                Noise_sum += Scale * Sample
                Scale = Scale / Bias

            Output[x] = Noise_sum / Scale_sum

