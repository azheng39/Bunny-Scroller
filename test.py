import bunny
import background
import obstacles

def main():

    print(“######## Testing bunny model#########”)
    test_bunny = bunny.Bunny()

    print("=====Stationary Test=====")
    test_bunny.jumpup = False
    print(test_bunny.getCoordinates()) #should be (0,0)
    print(jumptimes) #should equal 2

    print("=====Activate Jump Test=====")
    event.key == pygame.K_UP
    print(test_bunny.jumpup)
    print(test_bunny.jumpup)

    print("=====Jump Changes Vertical Speed Test=====")
    test_bunny.jumpup = True
    print(test_bunny.velocity)

    print("=====First Jump Test=====")
    test_bunny.jumpup = True
    print(test_bunny.getCoordinates())
    print(jumptimes) #should equal 1

    print("=====Second Jump Test=====")
    test_bunny.jumpup = True
    print(test_bunny.jumptimes) #should equal 1
    test_bunny.jumpup = True      
    print(test_bunny.jumptimes) #should equal 0

    print("=====Collision=====")
    test_bunny.colliding = True
    print(test_bunny.getCoordinates())

    

main()
