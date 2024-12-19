import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up the display window
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts for text
font = pygame.font.SysFont('arial', 24)

# Sorting Algorithms

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                draw_bars(arr)  # Update the display after each swap
                pygame.time.delay(10)  # Delay for animation
                check_for_quit()

# Quick Sort Algorithm
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)
    draw_bars(arr)  # Update the display after each partitioning
    pygame.time.delay(10)  # Delay for animation
    check_for_quit()

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

# Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
        draw_bars(arr)  # Update the display after each merge
        pygame.time.delay(10)  # Delay for animation
        check_for_quit()

# Visualization Functions

# Draw the bars representing the array
def draw_bars(arr):
    win.fill(WHITE)  # Only clear the screen once per iteration
    bar_width = WIDTH // len(arr)
    for i in range(len(arr)):
        x = i * bar_width
        y = HEIGHT - arr[i]
        pygame.draw.rect(win, BLUE, (x, y, bar_width, arr[i]))
    pygame.display.update()

# Generate a new random array
def generate_random_array():
    return [random.randint(10, HEIGHT) for _ in range(100)]

# Check if the user wants to quit
def check_for_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

# Main function to run the visualizer
def main():
    running = True
    arr = generate_random_array()  # Generate the initial random array
    draw_bars(arr)  # Initial draw
    
    # Display the options for sorting
    text = font.render("Press 'B' for Bubble Sort, 'Q' for Quick Sort, 'M' for Merge Sort", True, RED)
    win.blit(text, (50, 50))  # Display the text only once at the start
    pygame.display.update()  # Make sure the text stays visible

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_b]:  # Bubble Sort
            bubble_sort(arr)
            break
        if keys[pygame.K_q]:  # Quick Sort
            quick_sort(arr, 0, len(arr) - 1)
            break
        if keys[pygame.K_m]:  # Merge Sort
            merge_sort(arr)
            break

if __name__ == "__main__":
    main()
