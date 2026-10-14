

package frc.robot;

import com.ctre.phoenix6.hardware.TalonFX;

import edu.wpi.first.util.sendable.SendableRegistry; //don't delete, we will come back later
import edu.wpi.first.wpilibj.TimedRobot; //the control dichotomy
import edu.wpi.first.wpilibj.XboxController;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;  //left/right side



public class Robot extends TimedRobot {
  private final DifferentialDrive m_robotDrive;
  
  //Create the variables

  //CONSTANTS
  double K_ROTATION_RATE = .1;
  //one controller
  XboxController driver = new XboxController(0); //creates a new XBC called driver on P0
  XboxController manip= new XboxController(1); // Created a new XBC called manip on P1

  //two motors

  TalonFX leftMotor = new TalonFX(10);
  TalonFX rightMotor = new TalonFX(30);
  TalonFX pivot = new TalonFX(50);

  
  public Robot() {
    // We need to invert one side of the drivetrain so that positive voltages
    // result in both sides moving forward. Depending on how your robot's
    // gearbox is constructed, you might have to invert the left side instead.
  
    m_robotDrive = new DifferentialDrive(leftMotor::set, rightMotor::set);
   
    SendableRegistry.addChild(m_robotDrive, leftMotor);
    SendableRegistry.addChild(m_robotDrive, rightMotor);
  }

  @Override
  public void teleopPeriodic() {
    m_robotDrive.tankDrive(driver.getLeftY(), driver.getRightY());

    if(driver.getAButton()){
      pivot.set(K_ROTATION_RATE);
    }
    else if(driver.getBButton()){
      pivot.set(-K_ROTATION_RATE);
    }
    else{
      pivot.stopMotor();
    }
    
  }
}
